import pygame 
import time

from src.utils.debug import debug
from src.utils.key_handler import KeyHandler
from src.entity import EntityPhysics
from src.sprite_sheet import *
from src.tile_map import TileMap
from src.config import PLAYER

from collections import deque


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame game')

        self.window = pygame.display.set_mode((1280, 720))
        self.canvas = pygame.Surface((320, 180))
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0
        self.fps = 0
        self.frames_log = deque(maxlen=60)

        self.key_handler = KeyHandler()
        self.player = EntityPhysics(self, PLAYER, (30, 30), (32, 32))
        self.tile_map = TileMap(self)
    
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
        self.player.update(self.delta_time, (self.key_handler.actions['right'] - self.key_handler.actions['left'], self.key_handler.actions['down'] - self.key_handler.actions['up']))
        pygame.display.update()

    def render(self):
        self.canvas.fill((220, 100, 20))  
        self.tile_map.render(self.canvas)  
        self.player.render(self.canvas)
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
        debug(f'{self.fps:.1f}')
        debug(self.key_handler.actions, y=35)


if __name__ == "__main__":
    game = Game().run()