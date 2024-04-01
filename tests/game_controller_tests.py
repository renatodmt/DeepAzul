import json
import unittest
from game_controller import AzulGameController

test_cases = [
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        },
        'move': {'local': 1, 'color': 'orange', 'pattern_line': 5},
        'output': {
            'factories': [
                [],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 5},
        'output': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 1, 'white': 0, 'first_player_token': False}
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 5},
        'output': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 1, 'white': 0, 'first_player_token': False}
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 1, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': True}
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 5},
        'output': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False}
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        },
        'move': {'local': 5, 'color': 'blue', 'pattern_line': 5},
        'output': {
            'player_turn': 1
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ],
            'player_turn': 1
        },
        'move': {'local': 5, 'color': 'blue', 'pattern_line': 5},
        'output': {
            'player_turn': 0
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'player_turn': 0
        },
        'move': {'local': 5, 'color': 'white', 'pattern_line': 1},
        'output': {
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
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
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ],
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 1}
                ]
            ],
            'player_turn': 1
        },
        'move': {'local': 3, 'color': 'orange', 'pattern_line': 4},
        'output': {
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 3}
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 3}
                ]
            ]
        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 2},
        'output': {
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': 'black', 'used': 3},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 3}
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ]
        },
        'move': {'local': 2, 'color': 'black', 'pattern_line': 5},
        'output': {
            'center': {'blue': 1, 'orange': 2, 'red': 1, 'black': 3, 'white': 0, 'first_player_token': False}
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'factories': [
                ['orange', 'white', 'white', 'black'],
                ['black', 'red', 'orange', 'blue'],
                ['orange', 'white', 'orange', 'white'],
                ['white', 'blue', 'blue', 'white'],
                ['black', 'white', 'blue', 'red']
            ],
            'floor_lines': [[], []]
        },
        'move': {'local': 1, 'color': 'black', 'pattern_line': 5},
        'output': {
            'floor_lines': [['black'], []]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': True},
            'player_turn': 0,
            'floor_lines': [['red'], ['orange']]
        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 5},
        'output': {
            'center': {'blue': 0, 'orange': 1, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'floor_lines': [['red', 'first_player_token', 'black', 'black', 'black'], ['orange']]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 3, 'red': 0, 'black': 0, 'white': 1, 'first_player_token': False},
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 3}
                ]
            ],
            'player_turn': 1,
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 4},
        'output': {
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'white', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 5}
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 3, 'red': 0, 'black': 1, 'white': 0, 'first_player_token': False},
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
                    {'color': 'orange', 'used': 1},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'player_turn': 1,
            'floor_lines': [[], []]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 1},
        'output': {
            'floor_lines': [[], ['orange', 'orange']]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 3, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 1},
        'output': {
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 3, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 4},
        'output': {
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': 'orange', 'used': 3}
                ],
                [
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 3, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 1},
        'output': {
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 2, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0]
        },
        'move': {'local': 0, 'color': 'orange', 'pattern_line': 1},
        'output': {
            'scores': [1, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0]
        },
        'move': {'local': 0, 'color': 'red', 'pattern_line': 0},
        'output': {
            'scores': [2, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [1, 0]
        },
        'move': {'local': 0, 'color': 'red', 'pattern_line': 0},
        'output': {
            'scores': [2, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [1, 0]
        },
        'move': {'local': 0, 'color': 'red', 'pattern_line': 0},
        'output': {
            'scores': [4, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [1, 0]
        },
        'move': {'local': 0, 'color': 'red', 'pattern_line': 0},
        'output': {
            'scores': [3, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [3, 0]
        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 2},
        'output': {
            'scores': [6, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
            'floor_lines': [['first_player_token'], ['red']]
        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 2},
        'output': {
                'floor_lines': [[], []]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [3, 0],
            'floor_lines': [['first_player_token'], []]

        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 2},
        'output': {
            'scores': [5, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 3, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [3, 0],
            'floor_lines': [['first_player_token', 'red', 'red'], []]

        },
        'move': {'local': 0, 'color': 'black', 'pattern_line': 2},
        'output': {
            'scores': [2, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 2, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'player_turn': 1,
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0],
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 1},
        'output': {
            'scores': [0, 4]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [2, 0],
            'floor_lines': [['first_player_token', 'red', 'red'], []]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 1},
        'output': {
            'scores': [0, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [15, 0],
            'floor_lines': [
                ['first_player_token', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red'], []]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 1},
        'output': {
            'scores': [1, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 1},
        'output': {
            'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': True},
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'floor_lines': [['first_player_token'], []],
            'player_turn': 0
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 1},
        'output': {
            'player_turn': 0
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'game_end': False
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 0},
        'output': {
            'game_end': True
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 0},
        'output': {
            'scores': [7, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': True}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': True}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 0},
        'output': {
            'scores': [19, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
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
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0},
                    {'color': None, 'used': 0}
                ]
            ],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
            'scores': [0, 0]
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 0},
        'output': {
            'scores': [19, 0]
        }
    },
    {
        'type': 'status_update_after_move',
        'status': {
            'center': {'blue': 1, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': False},
            'factories': [[], [], [], [], []],
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'red', 'used': 1},
                    {'color': 'white', 'used': 3},
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
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
        },
        'move': {'local': 0, 'color': 'blue', 'pattern_line': 0},
        'output': {
            'discarded_titles': {'blue': 0, 'orange': 0, 'red': 0, 'black': 0, 'white': 2}
        }
    },
    {
        'type': 'game_simulation',
        'manual_factories': [
            [['red', 'red', 'white', 'white'], ['red', 'red', 'white', 'blue'], ['red', 'orange', 'blue', 'black'],
             ['blue', 'blue', 'red', 'white'], ['black', 'black', 'orange', 'blue']],
            [['orange', 'orange', 'white', 'blue'], ['orange', 'red', 'black', 'blue'],
             ['orange', 'red', 'red', 'blue'], ['blue', 'blue', 'blue', 'white'],
             ['orange', 'orange', 'orange', 'red']],
            [['red', 'black', 'black', 'white'], ['white', 'white', 'blue', 'red'],
             ['white', 'orange', 'red', 'blue'], ['black', 'orange', 'white', 'red'],
             ['black', 'black', 'red', 'white']],
            [['white', 'orange', 'black', 'red'], ['orange', 'black', 'red', 'blue'],
             ['blue', 'orange', 'red', 'black'], ['orange', 'orange', 'white', 'red'],
             ['blue', 'blue', 'blue', 'black']],
            [['white', 'white', 'black', 'black'], ['orange', 'black', 'black', 'white'],
             ['white', 'black', 'white', 'orange'], ['black', 'red', 'blue', 'orange'],
             ['orange', 'black', 'white', 'blue']],
            []
        ],
        'commands': [
            {'local': 2, 'color': 'red', 'pattern_line': 3},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0}
                    ]
                ]
            },
            {'local': 5, 'color': 'black', 'pattern_line': 4},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 0, 'color': 'blue', 'pattern_line': 1},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': None, 'used': 0},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 4, 'color': 'blue', 'pattern_line': 2},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': None, 'used': 0},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 0, 'color': 'white', 'pattern_line': 2},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': 'white', 'used': 2},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 3, 'color': 'blue', 'pattern_line': 2},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': 'white', 'used': 2},
                        {'color': 'red', 'used': 2},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 3},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 1, 'color': 'red', 'pattern_line': 3},
            {
                'factories': [[], [], [], [], []],
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': 'white', 'used': 2},
                        {'color': 'red', 'used': 4},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': None, 'used': 0},
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 3},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 0, 'color': 'orange', 'pattern_line': 1},
            {'local': 0, 'color': 'white', 'pattern_line': 2},
            {'local': 0, 'color': 'black', 'pattern_line': 0},
            {
                'pattern_lines': [
                    [
                        {'color': None, 'used': 0},
                        {'color': 'blue', 'used': 2},
                        {'color': 'white', 'used': 3},
                        {'color': 'red', 'used': 4},
                        {'color': None, 'used': 0}
                    ],
                    [
                        {'color': 'black', 'used': 1},
                        {'color': 'orange', 'used': 2},
                        {'color': 'blue', 'used': 3},
                        {'color': None, 'used': 0},
                        {'color': 'black', 'used': 2}
                    ]
                ]
            },
            {'local': 0, 'color': 'red', 'pattern_line': 0},
            {
                'center': {'blue': 0, 'orange': 0, 'red': 0, 'black': 0, 'white': 0, 'first_player_token': True},
                'scores': [1, 4],
                'boards': [
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                         {'color': 'red', 'filled': True}, {'color': 'black', 'filled': False},
                         {'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': True},
                         {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                         {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                         {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                         {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': True}, {'color': 'black', 'filled': False},
                         {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                         {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                         {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                         {'color': 'blue', 'filled': False}]
                    ],
                    [
                        [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                         {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True},
                         {'color': 'white', 'filled': False}],
                        [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                         {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': False},
                         {'color': 'black', 'filled': False}],
                        [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                         {'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': False},
                         {'color': 'red', 'filled': False}],
                        [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                         {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                         {'color': 'orange', 'filled': False}],
                        [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                         {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                         {'color': 'blue', 'filled': False}]
                    ]
                ]
            },
            {'local': 5, 'color': 'orange', 'pattern_line': 4},
            {'local': 1, 'color': 'orange', 'pattern_line': 2},
            {'local': 4, 'color': 'blue', 'pattern_line': 2},
            {'local': 0, 'color': 'red', 'pattern_line': 0},
            {'local': 0, 'color': 'white', 'pattern_line': 1},
            {'local': 2, 'color': 'orange', 'pattern_line': 2},
            {'local': 3, 'color': 'orange', 'pattern_line': 0},
            {'local': 0, 'color': 'black', 'pattern_line': 4},
            {'local': 0, 'color': 'blue', 'pattern_line': 3},
            {'local': 0, 'color': 'red', 'pattern_line': 1},
            {'scores': [10, 16]},
            {'local': 5, 'color': 'black', 'pattern_line': 1},
            {'local': 1, 'color': 'black', 'pattern_line': 2},
            {'local': 4, 'color': 'black', 'pattern_line': 4},
            {'local': 0, 'color': 'red', 'pattern_line': 1},
            {'local': 3, 'color': 'orange', 'pattern_line': 0},
            {'local': 2, 'color': 'blue', 'pattern_line': 3},
            {'local': 0, 'color': 'white', 'pattern_line': 3},
            {'local': 0, 'color': 'blue', 'pattern_line': 0},
            {'local': 0, 'color': 'orange', 'pattern_line': 5},
            {'local': 0, 'color': 'red', 'pattern_line': 5},
            {'scores': [11, 22]},
            {'local': 4, 'color': 'orange', 'pattern_line': 4},
            {'local': 0, 'color': 'white', 'pattern_line': 0},
            {'local': 5, 'color': 'black', 'pattern_line': 2},
            {'local': 2, 'color': 'orange', 'pattern_line': 3},
            {'local': 0, 'color': 'black', 'pattern_line': 0},
            {'local': 1, 'color': 'black', 'pattern_line': 4},
            {'local': 3, 'color': 'orange', 'pattern_line': 1},
            {'local': 0, 'color': 'orange', 'pattern_line': 3},
            {'local': 0, 'color': 'white', 'pattern_line': 5},
            {'local': 0, 'color': 'red', 'pattern_line': 2},
            {'local': 0, 'color': 'black', 'pattern_line': 5},
            {'local': 0, 'color': 'blue', 'pattern_line': 1},
            {'scores': [27, 37]},
            {'local': 1, 'color': 'white', 'pattern_line': 1},
            {'local': 2, 'color': 'black', 'pattern_line': 3},
            {'local': 4, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'white', 'pattern_line': 0},
            {'local': 3, 'color': 'white', 'pattern_line': 2},
            {'local': 0, 'color': 'orange', 'pattern_line': 2},
            {'local': 0, 'color': 'white', 'pattern_line': 2},
            {'local': 0, 'color': 'black', 'pattern_line': 3},
            {'local': 0, 'color': 'red', 'pattern_line': 4},
            {'local': 0, 'color': 'blue', 'pattern_line': 4},
            {'scores': [47, 67]},
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'blue']]
        },
        'output': [
            {'local': 5, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'blue', 'pattern_line': 1},
            {'local': 5, 'color': 'blue', 'pattern_line': 2},
            {'local': 5, 'color': 'blue', 'pattern_line': 3},
            {'local': 5, 'color': 'blue', 'pattern_line': 4},
            {'local': 5, 'color': 'blue', 'pattern_line': 5}
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'blue']],
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'red', 'used': 1},
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
        'output': [
            {'local': 5, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'blue', 'pattern_line': 2},
            {'local': 5, 'color': 'blue', 'pattern_line': 3},
            {'local': 5, 'color': 'blue', 'pattern_line': 4},
            {'local': 5, 'color': 'blue', 'pattern_line': 5}
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'blue']],
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 1},
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
        'output': [
            {'local': 5, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'blue', 'pattern_line': 1},
            {'local': 5, 'color': 'blue', 'pattern_line': 2},
            {'local': 5, 'color': 'blue', 'pattern_line': 3},
            {'local': 5, 'color': 'blue', 'pattern_line': 4},
            {'local': 5, 'color': 'blue', 'pattern_line': 5}
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'blue']],
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
        'output': [
            {'local': 5, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'blue', 'pattern_line': 2},
            {'local': 5, 'color': 'blue', 'pattern_line': 3},
            {'local': 5, 'color': 'blue', 'pattern_line': 4},
            {'local': 5, 'color': 'blue', 'pattern_line': 5}
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], []],
            'center': {'blue': 0, 'orange': 1, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'pattern_lines': [
                [
                    {'color': None, 'used': 0},
                    {'color': 'blue', 'used': 2},
                    {'color': 'red', 'used': 1},
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
        'output': [
            {'local': 0, 'color': 'red', 'pattern_line': 0},
            {'local': 0, 'color': 'red', 'pattern_line': 2},
            {'local': 0, 'color': 'red', 'pattern_line': 3},
            {'local': 0, 'color': 'red', 'pattern_line': 4},
            {'local': 0, 'color': 'red', 'pattern_line': 5},
            {'local': 0, 'color': 'orange', 'pattern_line': 0},
            {'local': 0, 'color': 'orange', 'pattern_line': 3},
            {'local': 0, 'color': 'orange', 'pattern_line': 4},
            {'local': 0, 'color': 'orange', 'pattern_line': 5},
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], ['blue', 'blue', 'blue', 'blue']],
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
        'output': [
            {'local': 5, 'color': 'blue', 'pattern_line': 0},
            {'local': 5, 'color': 'blue', 'pattern_line': 2},
            {'local': 5, 'color': 'blue', 'pattern_line': 3},
            {'local': 5, 'color': 'blue', 'pattern_line': 4},
            {'local': 5, 'color': 'blue', 'pattern_line': 5}
        ]
    },
    {
        'type': 'valid_moves',
        'status': {
            'factories': [[], [], [], [], []],
            'center': {'blue': 0, 'orange': 0, 'red': 1, 'black': 0, 'white': 0, 'first_player_token': False},
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
        },
        'output': [
            {'local': 0, 'color': 'red', 'pattern_line': 0},
            {'local': 0, 'color': 'red', 'pattern_line': 1},
            {'local': 0, 'color': 'red', 'pattern_line': 2},
            {'local': 0, 'color': 'red', 'pattern_line': 3},
            {'local': 0, 'color': 'red', 'pattern_line': 5},
        ]
    },
    {
        'type': 'game_winner',
        'status': {'scores': [1, 0]},
        'output': 0
    },
    {
        'type': 'game_winner',
        'status': {'scores': [0, 1]},
        'output': 1
    },
    {
        'type': 'game_winner',
        'status': {
            'scores': [0, 0],
            'boards': [
                [
                    [{'color': 'blue', 'filled': True}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
        },
        'output': 0
    },
    {
        'type': 'game_winner',
        'status': {
            'scores': [0, 0],
            'boards': [
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': True},
                     {'color': 'red', 'filled': True}, {'color': 'black', 'filled': True},
                     {'color': 'white', 'filled': True}],
                    [{'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': True},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': True},
                     {'color': 'blue', 'filled': False}]
                ],
                [
                    [{'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}],
                    [{'color': 'white', 'filled': True}, {'color': 'blue', 'filled': True},
                     {'color': 'orange', 'filled': True}, {'color': 'red', 'filled': True},
                     {'color': 'black', 'filled': True}],
                    [{'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}, {'color': 'orange', 'filled': False},
                     {'color': 'red', 'filled': False}],
                    [{'color': 'red', 'filled': False}, {'color': 'black', 'filled': False},
                     {'color': 'white', 'filled': False}, {'color': 'blue', 'filled': False},
                     {'color': 'orange', 'filled': False}],
                    [{'color': 'orange', 'filled': False}, {'color': 'red', 'filled': False},
                     {'color': 'black', 'filled': False}, {'color': 'white', 'filled': False},
                     {'color': 'blue', 'filled': False}]
                ]
            ],
        },
        'output': 1
    },
    {
        'type': 'game_winner',
        'status': {'scores': [0, 0]},
        'output': 2
    },
]
with open('test_cases.json', 'w') as f:
    json.dump(test_cases, f, indent=4)


class AzulGameControllerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open('test_cases.json', 'r') as file:
            cls.test_data = json.load(file)

    def setUp(self):
        self.maxDiff = None

    def test_status_updates_after_move(self):
        for test_index, test in enumerate(self.test_data, start=1):
            with self.subTest(test_case=f"Test Case {test_index}"):
                if test['type'] == 'status_update_after_move':
                    game_controller = AzulGameController()
                    for key, value in test['status'].items():
                        setattr(game_controller.status, key, value)
                    game_controller.make_move(test['move'])
                    for key, value in test['output'].items():
                        with self.subTest(attribute=key):
                            self.assertEqual(getattr(game_controller.status, key), value)

    def test_game_simulation(self):
        for test_index, test in enumerate(self.test_data, start=1):
            with self.subTest(test_case=f"Test Case {test_index}"):
                if test['type'] == 'game_simulation':
                    game_controller = AzulGameController(manual_factories=test['manual_factories'], factories_strategy='all_at_start')
                    for command in test['commands']:
                        if 'local' in command:
                            game_controller.make_move(command)
                        else:
                            for key, value in command.items():
                                with self.subTest(attribute=key):
                                    self.assertEqual(getattr(game_controller.status, key), value)

    def test_valid_moves(self):
        for test_index, test in enumerate(self.test_data, start=1):
            with self.subTest(test_case=f"Test Case {test_index}"):
                if test['type'] == 'valid_moves':
                    game_controller = AzulGameController()
                    for key, value in test['status'].items():
                        setattr(game_controller.status, key, value)
                    with self.subTest():
                        self.assertCountEqual(game_controller.check_valid_moves(), test['output'])

    def test_game_winner(self):
        for test_index, test in enumerate(self.test_data, start=1):
            with self.subTest(test_case=f"Test Case {test_index}"):
                if test['type'] == 'game_winner':
                    game_controller = AzulGameController()
                    for key, value in test['status'].items():
                        setattr(game_controller.status, key, value)
                    game_controller.check_game_winner()
                    with self.subTest():
                        self.assertEqual(game_controller.status.winner, test['output'])


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
