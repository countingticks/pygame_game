import pygame 
import random
import math

from src.particles.particle import Particle


class Leaf:
    def __init__(self, tile_map, assets, camera, image_duration, loop=False):
        self.tile_map = tile_map
        self.assets = assets
        self.camera = camera
        self.image_duration = image_duration
        self.loop = loop
        self.leaves = []

        for tree in self.tile_map.extract([('tree', 0)], keep=True):
            self.leaves.append(pygame.Rect(4 + tree['pos'][0], 4 + tree['pos'][1], 23, 12))

        self.particles = []

    def update(self, dt):
        for rect in self.leaves:
            if random.random() * 49999 <= rect.width * rect.height:
                pos = (rect.x + random.random() * rect.width, rect.y + random.random() * rect.height)
                self.particles.append(Particle(self.assets, self.camera, pos, velocity=[-10, 30], frame=random.randint(0, 5), image_duration=self.image_duration, loop=self.loop))

        for particle in self.particles.copy():
            kill = particle.update(dt)
            amplify = 10 * random.random() + 15
            speed = 0.3 * random.random() + 0.4
            particle.pos[0] += math.sin(particle.animation.frame * speed) * amplify * dt
            
            if kill:
                self.particles.remove(particle)

    def render(self, surface, offset=(0, 0)):
        for particle in self.particles:
            particle.render(surface, offset)