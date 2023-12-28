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
        'groups': ['grass', 'dirt'],
        'width': 32,
        'height': 32,
    },
    'grass': {'images': None, 'frames': 1},
    'dirt': {'images': None, 'frames': 1},
}

CLOUDS = {
    'sheet': {
        'path': BASE_PATH + 'clouds/sprite_sheet.png',
        'groups': ['cloud1', 'cloud2'],        
    },
    'cloud1': {'images': None, 'frames': 1, 'width': 55, 'height': 20},
    'cloud2': {'images': None, 'frames': 1, 'width': 39, 'height': 14},
}

BACKGROUND = {
    'path': BASE_PATH + 'background/sprite.png',
    'image': None,
}