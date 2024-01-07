from src.particles.leaf import Leaf


class Particles:
    def __init__(self, tile_map, assets):
        self.tile_map = tile_map
        self.assets = assets

        self.leaf_particle = Leaf(self.tile_map, self.assets['leaf'], image_duration=4, loop=False)

    def update(self, dt):
        self.leaf_particle.update(dt)

    def render(self, surface, offset=(0, 0)):
        self.leaf_particle.render(surface, offset)
