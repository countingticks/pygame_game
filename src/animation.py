import pygame

from src.sprite_sheet import *


class Animation: 
    def __init__(self, entity, camera, image_duration=20, loop=True):
        self.entity = entity
        self.camera = camera
        self.image_duration = image_duration
        self.loop = loop
        self.done = False
        self.previous_group = None
        self.frame = 0

    def update(self, dt, selected_group=None):
        if self.previous_group != selected_group:
            self.frame = 0
            self.previous_group = selected_group

        if selected_group == None:
            self.change_frame(self.entity, dt)
        else:
            for group in self.entity['groups']:
                if (selected_group == group):
                    self.change_frame(self.entity[selected_group], dt)

    def render(self, surface, pos, selected_group=None, flip=(False, False)):
        if selected_group == None:
            image = pygame.transform.flip(self.entity['images'][int(self.frame)], *flip)
            self.blit_image(surface, image, pos)
        else:
            image = pygame.transform.flip(self.entity[selected_group]['images'][int(self.frame)], *flip)
            self.blit_image(surface, image, pos)
    
    def blit_image(self, surface, image, pos):
        if -image.get_width() < pos[0] < self.camera.rect.width and -image.get_height() < pos[1] < self.camera.rect.height:
            surface.blit(image, pos)

    def change_frame(self, entity, dt):
        if self.loop: 
            self.frame = (self.frame + self.image_duration * dt) % entity['variants']
        else:
            self.frame = min(self.frame + self.image_duration * dt, entity['variants'] - 1)
            if self.frame >= entity['variants'] - 1:
                self.done = True
                