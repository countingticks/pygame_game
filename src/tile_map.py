import json
import pygame

from src.config import AUTO_TILE_GROUPS, AUTO_TILE_MAP, COLLISION_TILES, NEIGHBOR_OFFSETS


class TileMap:
    def __init__(self, camera, assets, path, tile_size=(16, 16)):
        self.camera = camera
        self.assets = assets
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []

        try:
            self.load(path)
        except FileNotFoundError:
            pass 

    def render(self, surface, offset=(0, 0)):
        for tile in self.off_grid_tiles:
            off_grid_image = self.assets[tile['group']][tile['type']]['images'][tile['variant']]

            if self.camera == None:
                off_grid_pos = (int(tile['pos'][0]) - offset[0], int(tile['pos'][1]) - offset[1])
                surface.blit(off_grid_image, off_grid_pos)
            elif self.camera.rect.x - off_grid_image.get_width() < tile['pos'][0] < self.camera.rect.x + self.camera.rect.width and self.camera.rect.y - off_grid_image.get_height() < tile['pos'][1] < self.camera.rect.y + self.camera.rect.height:
                off_grid_pos = (int(tile['pos'][0]) - offset[0], int(tile['pos'][1]) - offset[1])
                surface.blit(off_grid_image, off_grid_pos)
            
        for x in range(offset[0] // self.tile_size[0], (offset[0] + surface.get_width()) // self.tile_size[0] + 1):
            for y in range(offset[1] // self.tile_size[1], (offset[1] + surface.get_height()) // self.tile_size[1] + 1):
                check_location = str(x) + ';' + str(y)
                if check_location in self.tile_map:
                    tile = self.tile_map[check_location]
                    surface.blit(self.assets[tile['group']][tile['type']]['images'][tile['variant']], (tile['pos'][0] * self.tile_size[0] - offset[0], tile['pos'][1] * self.tile_size[1] - offset[1]))

    def tiles_around(self, pos):
        tiles = []
        tile_pos = (int(pos[0] // self.tile_size[0]), int(pos[1] // self.tile_size[1]))
        for offset in NEIGHBOR_OFFSETS:
            check_location = str(tile_pos[0] + offset[0]) + ';' + str(tile_pos[1] + offset[1])
            if check_location in self.tile_map:
                tiles.append(self.tile_map[check_location])
        return tiles
    
    def collision_tiles_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            if tile['type'] in COLLISION_TILES:
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size[0], tile['pos'][1] * self.tile_size[1], self.tile_size[0], self.tile_size[1]))
        return rects

    def auto_tile(self):
        for location in self.tile_map:
            tile = self.tile_map[location]
            neighbors = set()

            for offset in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
                check_location = str(tile['pos'][0] + offset[0]) + ";" + str(tile['pos'][1] + offset[1])
                if check_location in self.tile_map:
                    if self.tile_map[check_location]['type'] == tile['type']:
                        neighbors.add(offset)
            
            neighbors = tuple(sorted(neighbors))
            if tile['type'] in AUTO_TILE_GROUPS and neighbors in AUTO_TILE_MAP:
                tile['variant'] = AUTO_TILE_MAP[neighbors]

    def extract(self, id_pairs, keep=False):
        matches = []

        for tile in self.off_grid_tiles.copy():
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile)
                if not keep:
                    self.off_grid_tiles.remove(tile)
            
        for location in self.tile_map:
            tile = self.tile_map[location]
            if (tile['type'], tile['variant']) in id_pairs:
                matches.append(tile.copy())
                matches[-1]['pos'] = matches[-1]['pos'].copy()
                matches[-1]['pos'][0] *= self.tile_size[0]
                matches[-1]['pos'][1] *= self.tile_size[1]
                if not keep:
                    del self.tile_map[location]

        return matches

    def save(self, path):
        f = open(path, 'w')
        json.dump({'tile_map': self.tile_map, 'tile_size': self.tile_size, 'off_grid_tiles': self.off_grid_tiles}, f)
        f.close()

    def load(self, path):
        f = open(path, 'r')
        data = json.load(f)
        f.close()

        self.tile_map = data['tile_map']
        self.tile_size = data['tile_size']
        self.off_grid_tiles = data['off_grid_tiles']