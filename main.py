import pygame 
import time

from src.utils.debug import debug
from src.utils.key_handler import KeyHandler
from src.entity import EntityPhysics
from src.sprite_sheet import *
from src.tile_map import TileMap

from src.constants import PLAYER


class Game:
    def __init__(self):
        pygame.init()

        self.window = pygame.display.set_mode((1280, 720))
        self.canvas = pygame.Surface((320, 180))
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0

        self.key_handler = KeyHandler()
        self.player = EntityPhysics(self, PLAYER, (30, 30), (32, 32))
        self.tile_map = TileMap(self)
    
    def run(self):
        self.prev_time = time.time()
        
        while self.running:
            self.update_delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        self.running = False
            
            self.update()
            self.render()
            self.debug_info()
            # i will consider removing the fps limit later on 
            self.clock.tick(60)

    def render(self):
        self.canvas.fill((220, 100, 20))  
        self.tile_map.render(self.canvas)  
        self.player.render(self.canvas)
        self.window.blit(pygame.transform.scale(self.canvas, self.window.get_size()), (0, 0))

    def update_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def update(self):
        self.key_handler.update()
        self.player.update(self.delta_time, (self.key_handler.actions['right'] - self.key_handler.actions['left'], self.key_handler.actions['down'] - self.key_handler.actions['up']))
        pygame.display.update()

    def debug_info(self):
        debug(f'{1 / self.delta_time:.1f}' if self.delta_time > 0 else 0)
        debug(self.key_handler.actions, y=35)


if __name__ == "__main__":
    game = Game()
    game.run()