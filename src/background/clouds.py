import random

from src.config import CLOUDS
from src.sprite_sheet import load_sprite_sheet


class Cloud:
    def __init__(self, pos, image, speed, depth):
        self.pos = list(pos)
        self.image = image
        self.speed = speed
        self.depth = depth

    def update(self, dt):
        self.pos[0] += self.speed * dt

    def render(self, surface, offset=(0, 0)):
        render_pos = (self.pos[0] - offset[0] * self.depth, self.pos[1] - offset[1] * self.depth)
        surface.blit(self.image, (render_pos[0] % (surface.get_width() + self.image.get_width()) - self.image.get_width(), render_pos[1] % (surface.get_height() + self.image.get_height()) - self.image.get_height()))


class Clouds:
    def __init__(self, count=16):
        self.clouds = []

        load_sprite_sheet(CLOUDS)

        for _ in range(count):
            self.clouds.append(Cloud((random.random() * 99999, random.random() * 99999), CLOUDS[random.choice(CLOUDS['sheet']['groups'])]['images'][0], random.random() * 2 + 0.5, random.random() * 0.6 + 0.2))

        self.clouds.sort(key=lambda x: x.depth)

    def update(self, dt):
        for cloud in self.clouds:
            cloud.update(dt)

    def render(self, surface, offset=(0, 0)):
        for cloud in self.clouds:
            cloud.render(surface, offset=offset)