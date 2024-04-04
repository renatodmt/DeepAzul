from deepazul.data_processing import DataProcessor
import tensorflow
import sqlite3
from tensorflow.keras.models import load_model, Sequential
from tensorflow.keras.layers import Dense, Input

'''
target_encoder = OneHotEncoder(sparse_output=False, categories=[[0, 1, 2]])
target_encoder.fit(numpy.array([0, 1, 2]).reshape(-1, 1))
'''
input_size = 280


class SimpleNeuralNetwork(DataProcessor):
    def __init__(self, target=None, weights=None):
        self.model = Sequential([
            Input(shape=(input_size,)),
            Dense(200, activation='relu'),
            Dense(200, activation='relu'),
            Dense(100, activation='relu'),
            Dense(3, activation='softmax')
        ])
        self.target = target

        if weights:
            self.model.load_weights(weights)

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
            trainning_size = int(data_size / batch_size) * batch_size

        dataset = tensorflow.data.experimental.SqlDataset("sqlite", database_uri, query, (tensorflow.int8,) * (input_size + 2)) \
            .map(self.split_features_and_target, num_parallel_calls=tensorflow.data.AUTOTUNE)

        train_dataset = dataset.take(trainning_size) \
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

