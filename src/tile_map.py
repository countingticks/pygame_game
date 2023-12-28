import pygame

from src.config import TERRAIN
from src.sprite_sheet import load_sprite_sheet


NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
COLLISION_TILES = {'grass', 'stone'}

class TileMap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []

        load_sprite_sheet(TERRAIN)

        for i in range(10):
            self.tile_map[str(5 + i) + ';0'] = {'type': 'grass', 'variant': 1, 'pos': (5 + i, 0)}
            self.tile_map[str(5 + i) + ';2'] = {'type': 'grass', 'variant': 1, 'pos': (5 + i, 2)}
            self.tile_map[str(1 + i) + ';3'] = {'type': 'grass', 'variant': 1, 'pos': (1 + i, 3)}
            # self.tile_map['2;' + str(0 + i)] = {'type': 'stone', 'variant': 1, 'pos': (2, 0 + i)}

    def tiles_around(self, pos):
        tiles = []
        tile_pos = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        for offset in NEIGHBOR_OFFSETS:
            check_location = str(tile_pos[0] + offset[0]) + ';' + str(tile_pos[1] + offset[1])
            if check_location in self.tile_map:
                tiles.append(self.tile_map[check_location])
        return tiles
    
    def collision_tiles_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in COLLISION_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        return rects

    def render(self, surface):
        for tile in self.off_grid_tiles:
            surface.blit(TERRAIN[tile['type']]['images'][tile['variant'] - 1], tile['pos'])
        
        for loc in self.tile_map:
            tile = self.tile_map[loc]
            surface.blit(TERRAIN[tile['type']]['images'][tile['variant'] - 1], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))