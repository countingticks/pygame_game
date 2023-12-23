import pygame 
import time

from src.key_handler import KeyHandler

class Game:
    def __init__(self):
        pygame.init()

        self.canvas = pygame.Surface((800, 600))
        self.window = pygame.display.set_mode((1920, 1080))
        self.clock = pygame.time.Clock()

        self.running = True
        self.delta_time = 0
        
        self.key_handler = KeyHandler()
    
    def run(self):
        self.prev_time = time.time()
        
        while self.running:
            self.update_delta_time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.render()

            print(self.key_handler.get_actions())

            self.update()
            self.clock.tick(60)

    def render(self):
        self.canvas.fill((0, 0, 0))    
        pygame.draw.rect(self.canvas, (255, 255, 255), (20, 20, 60, 60))
        self.window.blit(self.canvas, (0, 0))

    def update_delta_time(self):
        current_time = time.time()
        self.delta_time = current_time - self.prev_time
        self.prev_time = current_time

    def update(self):
        self.key_handler.update()
        pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()