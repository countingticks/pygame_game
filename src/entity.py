import pygame

from src.animation import Animation
from src.sprite_sheet import *


class EntityPhysics: 
    def __init__(self, game, entity, pos, size):
        self.game = game
        self.entity = entity
        self.pos = pygame.Vector2(pos)
        self.size = size

        load_sprite_sheet(self.entity)

        self.player_animation = Animation(self.entity, image_duration=20)
        self.action = None

        self.velocity = pygame.Vector2(0, 0)
        self.direction = pygame.Vector2(0, 0)
        self.speed = 100
        self.acceleration = 200
        self.deceleration = 300

    def update(self, dt, movement=(0, 0)):
        if (movement[0]):
            self.direction.x = movement[0]
            if self.direction.x == 1:
                self.velocity.x = min(self.velocity.x + self.acceleration * dt, self.speed)
            else:
                self.velocity.x = -min(-self.velocity.x + self.acceleration * dt, self.speed)
        else:
            if self.velocity.x > 0:
                self.velocity.x = max(self.velocity.x - self.deceleration * dt, 0)
            else:
                self.velocity.x = -max(-self.velocity.x - self.deceleration * dt, 0)

        self.pos.x += self.velocity.x * dt

        if self.velocity.x != 0:
            self.action = 'run'
        else:
            self.action = 'idle'

        self.player_animation.update(self.action, dt)

        # jump
        #     if self.velocity.x > 0:
        #         self.velocity.x = max(value - self.deceleration * dt, 0)
        #     else:
        #         self.velocity.x = -max(value + self.deceleration * dt, 0)

    def render(self, surface):
        self.player_animation.render(surface, self.action, self.direction.x, self.pos)
