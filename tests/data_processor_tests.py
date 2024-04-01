import unittest
import json
from data_processing import DataProcessor
from game_controller import AzulGameController

test_cases = [
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 0
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col1_point_prediction': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row1_col0_point_prediction': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row0_col1_point_prediction': 4
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row1_col0_point_prediction': 7
        }
    },
    {
        'type': 'test_features',
        'status': {
        'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                ],
        ]
        },
        'output': {
            'board_player0_row2_col2_point_prediction': 12
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
        ]
        },
        'output': {
            'board_player0_row0_col0_point_prediction': 11
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'expected_difference_score_round_end': 0
        }
    },
    {
        'type': 'test_features',
        'status': {
            'scores': [2, 0]
        },
        'output': {
            'expected_difference_score_round_end': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
            'scores': [2, 0],
            'floor_lines': [['red'], []]
        },
        'output': {
            'expected_difference_score_round_end': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'pattern_lines': [
                [
                    {'color': 'red', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'expected_difference_score_round_end': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'pattern_lines': [
                [
                    {'color': 'red', 'used': 1},
                    {'color': 'orange', 'used': 2},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'expected_difference_score_round_end': 3
        }
    },
    {
        'type': 'test_features',
        'status': {
            'pattern_lines': [
                [
                    {'color': 'red', 'used': 1},
                    {'color': 'orange', 'used': 2},
                    {'color': 'blue', 'used': 3},
                    {'color': 'white', 'used': 4},
                    {'color': 'black', 'used': 5}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'expected_difference_score_round_end': 22
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'expected_difference_score_round_end': -10
        }
    },
    {
        'type': 'test_features',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'white']],
        },
        'output': {
            'total_factories_and_center_colorblue': 3
        }
    },
    {
        'type': 'test_features',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'black']],
        },
        'output': {
            'total_factories_and_center_colorblack': 4
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'avaiable_space_player0_colororange': 15
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'avaiable_space_player0_colororange': 15
        }
    },
    {
        'type': 'test_features',
        'status': {
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 2},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'avaiable_space_player0_colorblue': 13
        }
    },
    {
        'type': 'test_features',
        'status': {
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 2},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'avaiable_space_player0_colorblue': 10
        }
    },
    {
        'type': 'test_features',
        'status': {
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 2},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'avaiable_space_player0_colorblue': 6
        }
    },
    {
        'type': 'test_features',
        'status': {
            'scores': [2, 0]
        },
        'output': {
            'expected_difference_score_all_pattern_lines_completed': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
            'scores': [0, 0],
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': 'red', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'expected_difference_score_all_pattern_lines_completed': -1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'scores': [0, 0],
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
        },
        'output': {
            'expected_difference_score_all_pattern_lines_completed': -1
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'completed_rows_player0': 0
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_rows_player0': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_rows_player0': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'completed_columns_player0': 0
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': True}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_columns_player0': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_columns_player0': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'completed_colors_player0': 0
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': True}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_colors_player0': 1
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},{'color': 'white', 'filled': True}],
                        [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True}, {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'completed_colors_player0': 2
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'titles_to_complete_player0_row1': 10
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'titles_to_complete_player0_row1': 8
        }
    },
    {
        'type': 'test_features',
        'status': {
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        },
        'output': {
            'titles_to_complete_player1_row1': 9
        }
    },
    {
        'type': 'test_features',
        'status': {
        },
        'output': {
            'titles_to_complete_player0_colorblue': 15
        }
    },
    {
        'type': 'test_features',
        'status': {
            'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},{'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True}],
                        [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False}]
                    ],
            ]
        },
        'output': {
            'titles_to_complete_player0_colorblue': 11
        }
    },
    {
        'type': 'test_features',
        'status': {
           'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        },
        'output': {
            'titles_to_complete_player1_colorblue': 14
        }
    },
]
with open('test_cases.json', 'w') as f:
    json.dump(test_cases, f, indent=4)


class DataProcessorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('test_cases.json', 'r') as file:
            cls.test_data = json.load(file)

    def setUp(self):
        self.maxDiff = None

    def test_features(self):
        data_processor = DataProcessor()
        for test_index, test in enumerate(self.test_data, start=1):
            with self.subTest(test_case=f"Test Case {test_index}"):
                if test['type'] == 'test_features':
                    game_controller = AzulGameController()
                    for key, value in test['status'].items():
                        setattr(game_controller.status, key, value)
                    results = data_processor.get_features_from_game_log(status=game_controller.status)
                    for key, value in test['output'].items():
                        with self.subTest(attribute=key):
                            self.assertEqual(results[key], value)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
