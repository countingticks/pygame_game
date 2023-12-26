from src.config import TERRAIN
from src.sprite_sheet import load_sprite_sheet

class TileMap:
    def __init__(self, game, tile_size=32):
        self.game = game
        self.tile_size = tile_size
        self.tile_map = {}
        self.off_grid_tiles = []

        load_sprite_sheet(TERRAIN)

        for i in range(10):
            self.tile_map[str(3 + i) + ';2'] = {'type': 'grass', 'variant': 1, 'pos': (3 + i, 2)}
            self.tile_map['2;' + str(1 + i)] = {'type': 'stone', 'variant': 1, 'pos': (2, 1 + i)}

    def render(self, surface):
        for loc in self.tile_map:
            tile = self.tile_map[loc]
            surface.blit(TERRAIN[tile['type']]['images'][tile['variant'] - 1], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))