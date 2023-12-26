BASE_PATH = "data/"

PLAYER = {
    'sheet': {
        'path': BASE_PATH + 'character/sprite_sheet.png',
        'groups': ['idle', 'run', 'jump', 'fall'],
        'width': 32,
        'height': 32,
    },
    'idle': {'images': None, 'frames': 11},
    'run': {'images': None, 'frames': 12},
    'jump': {'images': None, 'frames': 1},
    'fall': {'images': None, 'frames': 1},
}

TERRAIN = {
    'sheet': {
        'path': BASE_PATH + 'terrain/sprite_sheet.png',
        'groups': ['grass', 'sky', 'stone', 'dirt'],
        'width': 32,
        'height': 32,
    },
    'grass': {'images': None, 'frames': 1},
    'sky': {'images': None, 'frames': 1},
    'stone': {'images': None, 'frames': 1},
    'dirt': {'images': None, 'frames': 1},
}