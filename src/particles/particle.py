from src.animation import Animation


class Particle:
    def __init__(self, assets, camera, pos, velocity=[0, 0], frame=0, image_duration=20, loop=False):
        self.assets = assets
        self.pos = list(pos)
        self.velocity = list(velocity)
        self.frame = frame
        self.animation = Animation(self.assets, camera, image_duration=image_duration, loop=loop)
        self.animation.frame = frame

    def update(self, dt):
        kill = False
        if self.animation.done:
            kill = True

        self.pos[0] += self.velocity[0] * dt
        self.pos[1] += self.velocity[1] * dt

        self.animation.update(dt)
        return kill
    
    def render(self, surface, offset=(0, 0)):
        pos = (self.pos[0] - offset[0] - self.assets['dimensions'][0] // 2, self.pos[1] - offset[1] - self.assets['dimensions'][1] // 2)
        self.animation.render(surface, pos)
