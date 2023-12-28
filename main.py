import pygame 
import time

from src.utils.debug import debug
from src.utils.key_handler import KeyHandler
from src.player import Player
from src.sprite_sheet import *
from src.tile_map import TileMap
from src.camera import Camera
from src.config import PLAYER
from src.background.background import Background

from collections import deque


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame game')

        self.window = pygame.display.set_mode((1280, 720))
        self.canvas = pygame.Surface((569, 320))
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0
        self.fps = 0
        self.frames_log = deque(maxlen=60)

        self.key_handler = KeyHandler()
        self.player = Player(self, PLAYER, (30, 30))
        self.tile_map = TileMap(self, tile_size=[32, 32])
        self.camera = Camera(self.canvas.get_size(), slowness=0.3)
        self.camera.set_target(self.player)
        self.background = Background()

    def run(self):
        self.prev_time = time.time()
        
        while self.running:
            self.calculate_delta_time()
            self.calculate_fps()
            self.handle_events()
            self.update()
            self.render()
            self.debug_info()
            self.clock.tick(60)

        pygame.quit()

    def update(self):
        self.key_handler.update()
        self.background.update(self.delta_time)
        self.player.update(self.delta_time, self.tile_map)
        self.camera.update(self.delta_time)
        pygame.display.update()

    def render(self):
        self.background.render(self.canvas, offset=self.camera)
        self.tile_map.render(self.canvas, offset=self.camera)  
        self.player.render(self.canvas, offset=self.camera)
        self.window.blit(pygame.transform.scale(self.canvas, self.window.get_size()), (0, 0))

    def calculate_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def calculate_fps(self):
        self.frames_log.append(self.delta_time)
        self.fps = len(self.frames_log) / sum(self.frames_log) if sum(self.frames_log) > 0 else 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        if self.key_handler.actions['quit']:
            self.running = False

    def debug_info(self):
        debug(f'fps: {self.fps:.1f}', y=10)
        debug(f'keys: {self.key_handler.actions}', y=35)
        debug(f'collision: {self.tile_map.collision_tiles_around(self.player.pos)}', y=60)
        debug(f'velocity: x[{self.player.velocity[0]:.2f}], y[{self.player.velocity[1]:.2f}]', y=85)


if __name__ == "__main__":
    game = Game().run()