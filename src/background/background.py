import pygame

from src.config import BACKGROUND
from src.sprite_sheet import load_image
from src.background.clouds import Clouds


class Background:
    def __init__(self, clouds_count=16):        
        self.clouds = Clouds(count=clouds_count)
        load_image(BACKGROUND)

    def update(self, dt):
        self.clouds.update(dt)
    
    def render(self, surface, offset=(0, 0)):
        surface.blit(pygame.transform.scale(BACKGROUND['image'], surface.get_size()), (0, 0))
        self.clouds.render(surface, offset=offset) 