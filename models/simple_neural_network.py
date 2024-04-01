import numpy
from data_processing import DataProcessor
#from sklearn.preprocessing import OneHotEncoder
import tensorflow
import sqlite3
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Input

'''
target_encoder = OneHotEncoder(sparse_output=False, categories=[[0, 1, 2]])
target_encoder.fit(numpy.array([0, 1, 2]).reshape(-1, 1))
'''
input_size = 280


class SimpleNeuralNetwork(DataProcessor):
    #target_encoder = target_encoder
    early_stopping = EarlyStopping(
        monitor='val_loss',
        patience=3,
        verbose=1,
        restore_best_weights=True,
        min_delta=0.01
    )

    def __init__(self, target=None, weights=None):
        self.normalizer = tensorflow.keras.layers.Normalization(axis=-1)

        self.model = Sequential([
            Input(shape=(input_size,)),
            self.normalizer,
            Dense(200, activation='relu'),
            Dense(200, activation='relu'),
            Dense(100, activation='relu'),
            Dense(3, activation='softmax')
        ])
        self.target = target

        if weights:
            self.model.load_weights(weights)

    '''
    def train_from_game_logs(self, game_logs):
        model_data = self.process_multiple_game_logs(game_logs)
        train = model_data.drop(self.target, axis=1).to_numpy()
        target = self.target_encoder.transform(model_data[self.target].astype(numpy.int8).to_numpy().reshape(-1, 1))
        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        self.model.fit(
            train,
            target,
            epochs=3,
            batch_size=32,
            validation_split=0.1,
            callbacks=[self.early_stopping],
            verbose=1
        )
    '''

    def split_features_and_target(self, *row):
        *features, target, _ = row  # Unpack row, discard the last element, and separate target
        target = tensorflow.one_hot(target, depth=3)
        return tensorflow.stack(features), target

    def train_from_database(self):
        batch_size = 32*4
        database_uri = 'file:database.db?mode=ro'
        query = '''
            select * 
            from
                (
                select *
                from games
                order by iteration
                limit 10000000
                ) t
            order by random()
            ;
        '''

        with sqlite3.connect('database.db') as connection:
            cursor = connection.cursor()
            cursor.execute(f'SELECT COUNT(*) FROM games limit 10000000')
            data_size = cursor.fetchone()[0]
            trainning_size = int(data_size * 0.9 / 32) * 32
            validation_size = data_size - trainning_size

        dataset = tensorflow.data.experimental.SqlDataset("sqlite", database_uri, query, (tensorflow.int8,) * (input_size + 2)) \
            .map(self.split_features_and_target, num_parallel_calls=tensorflow.data.AUTOTUNE)

        normalization_dataset = dataset.take(1000).map(lambda x, y: x)

        self.normalizer.adapt(normalization_dataset)

        train_dataset = dataset.take(trainning_size) \
            .repeat(10) \
            .batch(batch_size, drop_remainder=True) \
            .prefetch(tensorflow.data.AUTOTUNE)
        validation_dataset = dataset.skip(trainning_size) \
            .repeat(10) \
            .batch(batch_size, drop_remainder=True) \
            .prefetch(tensorflow.data.AUTOTUNE)

        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )
        self.model.fit(
            train_dataset,
            epochs=1,
            steps_per_epoch=int(trainning_size/batch_size),
            validation_data=validation_dataset,
            validation_steps=int(validation_size/batch_size),
            #callbacks=[self.early_stopping],
            verbose=1
        )

    @tensorflow.function(
        input_signature=[tensorflow.TensorSpec(shape=[None, input_size], dtype=tensorflow.int8)]
    )
    def predict_tf_function(self, input_data):
        return self.model(input_data, training=False)

    def predict(self, status):
        processed_status = self.process_game_log(status).drop(self.target, axis=1).to_numpy()
        input_tensor = tensorflow.convert_to_tensor(processed_status, dtype=tensorflow.int8)
        return self.predict_tf_function(input_tensor)

