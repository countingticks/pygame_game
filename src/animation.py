import math
import pygame

from src.sprite_sheet import *


class Animation: 
    def __init__(self, entity, image_duration=20, loop=True):
        self.entity = entity
        self.image_duration = image_duration
        self.loop = loop
        self.done = False
        self.previous_action = None
        self.frame = 0

        load_sprite_sheet(self.entity)

    def update(self, action, dt):
        if self.previous_action != action:
            self.frame = 0
            self.previous_action = action

        for group in self.entity['sheet']['groups']:
            if (action == group):
                if self.loop: 
                    self.frame = (self.frame + self.image_duration * dt) % self.entity[action]['frames']
                else:
                    self.frame = min(self.frame + self.image_duration * dt, self.entity[action]['frames'] - 1)
                    if self.frame >= self.entity[action]['frames'] - 1:
                        self.done = True

    def render(self, surface, action, flip, pos):
        surface.blit(pygame.transform.flip(self.entity[action]['images'][int(self.frame)], *flip), pos)