BASE_PATH = "data/"

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

PLAYER = {
    'groups': ['idle', 'run', 'jump', 'fall'],
    'idle': {
        'path': BASE_PATH + 'character/idle_sprite_sheet.png',
        'dimensions': [15, 25],
        'variants': 17,
        'sprite_sheet': None,
        'images': []
    },
    'run': {
        'path': BASE_PATH + 'character/run_sprite_sheet.png',
        'dimensions': [15, 25],
        'variants': 13,
        'sprite_sheet': None,
        'images': []
    },
    'jump': {
        'path': BASE_PATH + 'character/jump_sprite_sheet.png',
        'dimensions': [15, 25],
        'variants': 5,
        'sprite_sheet': None,
        'images': []
    },
    'fall': {
        'path': BASE_PATH + 'character/fall_sprite_sheet.png',
        'dimensions': [15, 25],
        'variants': 5,
        'sprite_sheet': None,
        'images': []
    },
}

TERRAIN = {
    'groups': ['grass', 'stone'],
    'grass': {
        'path': BASE_PATH + 'terrain/grass_sprite_sheet.png',
        'dimensions': [16, 16],
        'variants': 11,
        'sprite_sheet': None,
        'images': []
    },
    'stone': {
        'path': BASE_PATH + 'terrain/stone_sprite_sheet.png',
        'dimensions': [16, 16],
        'variants': 17,
        'sprite_sheet': None,
        'images': []
    }
}

DECORATION = {
    'groups': ['plant', 'extra', 'tree'],
    'plant': {
        'path': BASE_PATH + 'decoration/plant_sprite_sheet.png',
        'dimensions': [12, 40],
        'variants': 1,
        'sprite_sheet': None,
        'images': []
    },
    'extra': {
        'path': BASE_PATH + 'decoration/extra_sprite_sheet.png',
        'dimensions': [16, 16],
        'variants': 4,
        'sprite_sheet': None,
        'images': []
    },
    'tree': {
        'path': BASE_PATH + 'decoration/tree_sprite_sheet.png',
        'dimensions': [33, 44],
        'variants': 1,
        'sprite_sheet': None,
        'images': []
    }
}

SPAWNER = {
    'groups': ['player'],
    'player': {
        'path': BASE_PATH + 'spawner/player_sprite_sheet.png',
        'dimensions': [15, 25],
        'variants': 1,
        'sprite_sheet': None,
        'images': []
    }
}

PARTICLE = {
    'groups': ['leaf'],
    'leaf': {
        'path': BASE_PATH + 'particle/leaf_sprite_sheet.png',
        'dimensions': [8, 8],
        'variants': 18,
        'sprite_sheet': None,
        'images': []
    }
}


# TILE MAP
NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]

COLLISION_TILES = {'grass', 'stone'}

AUTO_TILE_GROUPS = {'grass', 'stone'}

AUTO_TILE_MAP = {
    tuple(sorted([(1, 0)])): 0,
    tuple(sorted([(1, 0), (1, -1)])): 0,
    tuple(sorted([(0, 1), (-1, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1)])): 0,
    tuple(sorted([(1, 0), (1, 1)])): 0,
    tuple(sorted([(1, 0), (1, 1), (0, 1)])): 0,
    tuple(sorted([(1, -1), (1, 0), (1, 1)])): 0,
    tuple(sorted([(1, 0), (0, 1), (-1, 1)])): 0,
    tuple(sorted([(1, 0), (1, 1), (0, 1), (-1, 1)])): 0,
    tuple(sorted([(1, -1), (1, 0), (1, 1), (0, 1)])): 0,
    tuple(sorted([(1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)])): 0,

    tuple(sorted([(-1, 0)])): 1,
    tuple(sorted([(-1, 0), (-1, -1)])): 1,
    tuple(sorted([(0, 1), (1, 1)])): 1,
    tuple(sorted([(-1, 0), (0, 1)])): 1,
    tuple(sorted([(-1, 0), (-1, 1)])): 1,
    tuple(sorted([(-1, 0), (-1, 1), (0, 1)])): 1,
    tuple(sorted([(-1, -1), (-1, 0), (-1, 1)])): 1,
    tuple(sorted([(-1, 0), (0, 1), (1, 1)])): 1,
    tuple(sorted([(-1, 0), (-1, 1), (0, 1), (1, 1)])): 1,
    tuple(sorted([(-1, -1), (-1, 0), (-1, 1), (0, 1)])): 1,
    tuple(sorted([(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)])): 1,

    tuple(sorted([(0, 1)])): 2,
    tuple(sorted([(0, 1), (1, 1), (-1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (0, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (1, -1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, -1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, -1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (0, 1), (1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (0, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (0, 1), (1, 1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (-1, -1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, -1)])): 2,
    tuple(sorted([(1, 0), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, -1), (-1, -1)])): 2,

    tuple(sorted([(-1, 0), (0, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (0, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (0, 1), (1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (0, 1), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (1, 1), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (1, 0), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (0, 1), (1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (0, 1), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (0, 1), (1, 0), (1, -1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)])): 3,
    tuple(sorted([(-1, 0), (0, -1), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)])): 3,

    tuple(sorted([(1, 0), (0, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (0, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (-1, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (0, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (-1, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (0, 1), (-1, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (0, 1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (-1, 1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 0), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (0, 1), (-1, 1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (0, 1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (0, 1), (-1, 1), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (0, 1), (-1, 1), (1, 0), (-1, -1)])): 4,
    tuple(sorted([(1, 0), (0, -1), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1)])): 4,

    tuple(sorted([(0, 1), (0, -1), (1, -1), (1, 0), (1, 1)])): 5,
    tuple(sorted([(0, 1), (0, -1), (1, 1), (1, 0), (1, -1), (-1, -1)])): 5,
    tuple(sorted([(0, 1), (0, -1), (-1, 1), (1, -1), (1, 0), (1, 1)])): 5,
    
    tuple(sorted([(0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)])): 6,
    tuple(sorted([(0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1), (1, -1)])): 6,
    tuple(sorted([(0, 1), (0, -1), (1, 1), (-1, -1), (-1, 0), (-1, 1)])): 6,

    tuple(sorted([(1, 0), (0, -1), (1, -1)])): 7,
    tuple(sorted([(1, 0), (0, -1), (1, -1), (-1, -1)])): 7,
    tuple(sorted([(1, 0), (0, -1), (1, -1), (1, 1)])): 7,
    tuple(sorted([(1, 0), (0, -1), (1, -1), (-1, -1), (1, 1)])): 7,

    tuple(sorted([(-1, 0), (0, -1), (-1, -1)])): 8,
    tuple(sorted([(-1, 0), (0, -1), (-1, -1), (1, -1)])): 8,
    tuple(sorted([(-1, 0), (0, -1), (-1, -1), (-1, 1)])): 8,
    tuple(sorted([(-1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)])): 8,

    tuple(sorted([(-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1)])): 9,
    tuple(sorted([(-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1), (1, 1)])): 9,
    tuple(sorted([(-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1)])): 9,
    tuple(sorted([(-1, 0), (1, 0), (0, -1), (-1, -1), (1, -1), (-1, 1), (1, 1)])): 9,

    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (-1, -1), (-1, 1)])): 10,
    tuple(sorted([(0, 1), (0, -1), (1, 0), (-1, 0), (1, -1), (1, 1), (-1, -1), (-1, 1)])): 10,
}
