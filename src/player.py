from src.entity import PhysicsEntity


class Player(PhysicsEntity):
    def __init__(self, tile_map, key_handler, assets, camera, pos):
        custom_collision_size = (9, 22)
        image_duration = 20

        super().__init__(assets, camera, pos, image_duration=image_duration, custom_collision_size=custom_collision_size)

        self.tile_map = tile_map
        self.key_handler = key_handler
        self.speed = 100
        self.acceleration[1] = 400
        self.air_time = 0
        self.jumps = 1
        self.auto_flip = 1
        self.render_rect = False

        for player in self.tile_map.extract([('player', 0)], keep=False):
            self.pos = player['pos']

    def update(self, dt):
        self.apply_force(dt, ((self.key_handler.actions['right'].is_held - self.key_handler.actions['left'].is_held) * self.speed, 0))
        
        if self.key_handler.actions['space'].is_pressed:
            if self.jumps > 0:
                self.velocity[1] = -225
                self.air_time = 0.1
                self.jumps -= 1

        if self.air_time > 0.1:
            if self.velocity[1] < 0:
                self.set_action('jump')
                self.animation.loop = False
            else:
                self.set_action('fall')
                self.animation.loop = False
        else:
            if self.next_movement[0] != 0:
                self.set_action('run')
                self.animation.loop = True
            else:
                self.set_action('idle')
                self.animation.loop = True
        
        self.physics_update(dt, self.tile_map)

        if self.collision['down']:
            self.air_time = 0
            self.jumps = 1
            self.velocity[1] = 0
        else:
            self.air_time += dt

        super().update(dt)