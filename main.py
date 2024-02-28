import pygame 
import time

from src.utils.debug import debug
from src.utils.input_handler import InputHandler
from src.player import Player
from src.particles.particles import Particles
from src.sprite_sheet import *
from src.tile_map import TileMap
from src.camera import Camera
from src.config import PLAYER, TERRAIN, DECORATION, PARTICLE, SPAWNER
from src.background.background import Background

from collections import deque


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame game')

        self.window = pygame.display.set_mode((1280, 720))
        self.canvas = pygame.Surface((426, 240)) # 426 240 # 569 320
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0
        self.fps = 0
        self.frames_log = deque(maxlen=60)

        self.assets = {}
        self.load_assets()

        self.key_handler = InputHandler()
        self.camera = Camera(self.canvas.get_size(), slowness=0.3)
        self.tile_map = TileMap(self.camera, self.assets, 'src/levels/map.json', tile_size=[16, 16])
        self.player = Player(self.tile_map, self.key_handler, self.assets['player'], self.camera, (150, 10))
        self.particles = Particles(self.tile_map, self.assets['particle'], self.camera)
        self.background = Background()

        self.camera.set_target(self.player)

    def run(self):
        self.prev_time = time.time()
        
        while self.running:
            self.calculate_delta_time()
            self.calculate_fps()
            self.quit_game()
            self.update()
            self.render()
            self.debug_info()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        self.key_handler.update()
        self.background.update(self.delta_time)
        self.player.update(self.delta_time)
        self.camera.update(self.delta_time)
        self.particles.update(self.delta_time)
        pygame.display.update()

    def render(self):
        self.background.render(self.canvas, offset=self.camera)
        self.tile_map.render(self.canvas, offset=self.camera)  
        self.particles.render(self.canvas, offset=self.camera)
        self.player.render(self.canvas, offset=self.camera)
        self.window.blit(pygame.transform.scale(self.canvas, self.window.get_size()), (0, 0))

    def load_assets(self):
        assets_groups = {'player': PLAYER, 'terrain': TERRAIN, 'decoration': DECORATION, 'spawner': SPAWNER, 'particle': PARTICLE}
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
                self.assets[group][asset]['variants'] = assets_groups[group][asset]['variants']

    def calculate_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def calculate_fps(self):
        self.frames_log.append(self.delta_time)
        self.fps = len(self.frames_log) / sum(self.frames_log) if sum(self.frames_log) > 0 else 0

    def quit_game(self):
        if self.key_handler.actions['quit'].is_pressed:
            self.running = False

    def debug_info(self):
        debug(f'fps: {self.fps:.1f}', y=10)
        debug(f'collision: {self.tile_map.collision_tiles_around(self.player.pos)}', y=35)


if __name__ == "__main__":
    Game().run()