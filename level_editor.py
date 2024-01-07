import pygame 
import time

from src.utils.debug import debug
from src.utils.input_handler import InputHandler
from src.sprite_sheet import *
from src.tile_map import TileMap

from src.config import TERRAIN, DECORATION

from collections import deque


class Editor:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Level Editor')

        self.window = pygame.display.set_mode((1280, 720))
        self.canvas = pygame.Surface((569, 320))
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0
        self.fps = 0
        self.frames_log = deque(maxlen=60)

        self.key_handler = InputHandler()
        self.tile_map = TileMap(self, 'src/levels/map.json', tile_size=[16, 16])

        self.scroll = [0, 0]
        self.render_scale = (self.window.get_width() / self.canvas.get_width(), self.window.get_height() / self.canvas.get_height())
        self.tile_pos = None
        self.mouse_pos = None
        self.on_grid = True
        self.asset_group = 0
        self.tile_group = 0
        self.tile_variant = 0

        self.assets = {}
        self.load_assets()

    def run(self):
        self.prev_time = time.time()
        
        while self.running:
            self.tile_map.auto_tile()

            self.calculate_delta_time()
            self.calculate_fps()
            self.quit_game()
            self.place_tiles()
            self.update()
            self.render()
            self.save_map()
            self.debug_info()
            self.clock.tick(60)

        pygame.quit()
   
    def update(self):
        self.key_handler.update()
        self.update_current_tile()
        self.update_placement_mode()
        self.update_scroll()
        pygame.display.update()

    def render(self):
        self.canvas.fill((100, 100, 100))
        self.render_tile_map()
        self.render_cursor_indicator()
        self.render_tile_selection_menu()

        self.window.blit(pygame.transform.scale(self.canvas, self.window.get_size()), (0, 0))

    def update_current_tile(self):
        if self.key_handler.actions['e'].is_pressed:
            self.tile_group = 0
            self.tile_variant = 0
            self.asset_group -= 1
            if self.asset_group < 0:
                self.asset_group = len(self.assets['groups']) - 1

        if self.key_handler.actions['r'].is_pressed:
            self.tile_group = 0
            self.tile_variant = 0
            self.asset_group += 1
            if self.asset_group >= len(self.assets['groups']):
                self.asset_group = 0

        if self.key_handler.actions['mouse_down'].in_use:
            if self.key_handler.actions['shift'].is_held:
                self.tile_group += 1
                self.tile_variant = 0
                current_asset_group = self.assets['groups'][self.asset_group]
                if self.tile_group >= len(self.assets[current_asset_group]['groups']):
                    self.tile_group = 0
            else:
                self.tile_variant += 1
                current_asset_group = self.assets['groups'][self.asset_group]
                current_tile_group = self.assets[current_asset_group]['groups'][self.tile_group]
                if self.tile_variant >= len(self.assets[current_asset_group][current_tile_group]['images']):
                    self.tile_variant = 0

        if self.key_handler.actions['mouse_up'].in_use:
            if self.key_handler.actions['shift'].is_held:
                self.tile_group -= 1
                self.tile_variant = 0
                current_asset_group = self.assets['groups'][self.asset_group]
                if self.tile_group < 0:
                    self.tile_group = len(self.assets[current_asset_group]['groups']) - 1
            else:
                self.tile_variant -= 1
                current_asset_group = self.assets['groups'][self.asset_group]
                current_tile_group = self.assets[current_asset_group]['groups'][self.tile_group]
                if self.tile_variant < 0:
                    self.tile_variant = len(self.assets[current_asset_group][current_tile_group]['images']) - 1

    def update_placement_mode(self):
        if self.key_handler.actions['g'].is_pressed:
            self.on_grid = not self.on_grid

    def update_scroll(self):
        self.scroll[0] += self.key_handler.actions['right'].is_held * 5
        self.scroll[0] -= self.key_handler.actions['left'].is_held * 5

        self.scroll[1] += self.key_handler.actions['down'].is_held * 5
        self.scroll[1] -= self.key_handler.actions['up'].is_held * 5

    def render_tile_map(self):
        render_offset = (int(self.scroll[0]), int(self.scroll[1]))
        self.tile_map.render(self.canvas, offset=render_offset)  

    def render_cursor_indicator(self):
        current_asset_group = self.assets['groups'][self.asset_group]
        current_tile_group = self.assets[current_asset_group]['groups'][self.tile_group]
        current_image = self.assets[current_asset_group][current_tile_group]['images'][self.tile_variant].copy()
        current_image.set_alpha(150)
        if self.on_grid:
            self.canvas.blit(current_image, (self.tile_pos[0] * self.tile_map.tile_size[0] - self.scroll[0], self.tile_pos[1] * self.tile_map.tile_size[1] - self.scroll[1]))
        else:
            self.canvas.blit(current_image, (self.mouse_pos[0], self.mouse_pos[1]))

    def render_tile_selection_menu(self):
        background = pygame.Surface((50, 320))
        background.set_alpha(175)
        background.fill((50, 50, 50))
        self.canvas.blit(background, (0, 0))

        y_offset = 45

        current_asset_group = self.assets['groups'][self.asset_group]
        current_tile_group = self.assets[current_asset_group]['groups'][self.tile_group]

        self.canvas.blit(self.assets[current_asset_group][current_tile_group]['sprite_sheet'], (5, y_offset))
        self.canvas.blit(self.assets[current_asset_group][current_tile_group]['images'][self.tile_variant], (26, y_offset))

        current_tile_dimensions = self.assets[current_asset_group][current_tile_group]['dimensions']
        pygame.draw.rect(self.canvas, (255, 255, 255), (5, y_offset + current_tile_dimensions[1] * self.tile_variant, current_tile_dimensions[0], current_tile_dimensions[1]), 1)

    def place_tiles(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_pos = (self.mouse_pos[0] / self.render_scale[0], self.mouse_pos[1] / self.render_scale[0])
        self.tile_pos = (int((self.mouse_pos[0] + self.scroll[0]) // self.tile_map.tile_size[0]), int((self.mouse_pos[1] + self.scroll[1]) // self.tile_map.tile_size[1]))

        if self.key_handler.actions['mouse_left'].is_held and self.on_grid:
            self.tile_map.tile_map[str(self.tile_pos[0]) + ';' + str(self.tile_pos[1])] = {'group': self.assets['groups'][self.asset_group], 'type': self.assets[self.assets['groups'][self.asset_group]]['groups'][self.tile_group], 'variant': self.tile_variant, 'pos': self.tile_pos}
        elif self.key_handler.actions['mouse_left'].is_pressed and not self.on_grid:
            self.tile_map.off_grid_tiles.append({'group': self.assets['groups'][self.asset_group], 'type': self.assets[self.assets['groups'][self.asset_group]]['groups'][self.tile_group], 'variant': self.tile_variant, 'pos': (self.mouse_pos[0] + self.scroll[0], self.mouse_pos[1] + self.scroll[1])})

        if self.key_handler.actions['mouse_right'].is_held:
            tile_location = str(self.tile_pos[0]) + ';' + str(self.tile_pos[1])
            if tile_location in self.tile_map.tile_map:
                del self.tile_map.tile_map[tile_location]
            
            for tile in self.tile_map.off_grid_tiles.copy():
                tile_image = self.assets[tile['group']][tile['type']]['images'][tile['variant']]
                tile_rect = pygame.Rect(tile['pos'][0] - self.scroll[0], tile['pos'][1] - self.scroll[1], tile_image.get_width(), tile_image.get_height())
                if tile_rect.collidepoint(self.mouse_pos):
                    self.tile_map.off_grid_tiles.remove(tile)
                 
    def load_assets(self):
        assets_groups = {'terrain': TERRAIN, 'decoration': DECORATION}
        self.assets['groups'] = []

        for group in assets_groups:
            load_sprite_sheet_test(assets_groups[group])
            self.assets['groups'].append(group)
            self.assets[group] = {}
            self.assets[group]['groups'] = assets_groups[group]['groups']

            for asset in assets_groups[group]['groups']:
                self.assets[group][asset] = {}
                self.assets[group][asset]['sprite_sheet'] = assets_groups[group][asset]['sprite_sheet']
                self.assets[group][asset]['images'] = assets_groups[group][asset]['images']
                self.assets[group][asset]['dimensions'] = assets_groups[group][asset]['dimensions']

    def calculate_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def calculate_fps(self):
        self.frames_log.append(self.delta_time)
        self.fps = len(self.frames_log) / sum(self.frames_log) if sum(self.frames_log) > 0 else 0

    def save_map(self):
        if self.key_handler.actions['o'].is_pressed:
            self.tile_map.save('src/levels/map.json')

    def quit_game(self):
        if self.key_handler.actions['quit'].is_pressed:
            self.running = False

    def debug_info(self):
        debug(f"fps: {self.fps:.1f}", y=10)
        debug(f"q:quit; w,a,s,d: movement; g: toggle offgrid; e,r: navigate asset type; o: save", y=35)
        debug(f"asset group: {self.assets['groups'][self.asset_group]}", y=60)


if __name__ == "__main__":
    Editor().run()