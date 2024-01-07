from src.entity import PhysicsEntity


class Player(PhysicsEntity):
    def __init__(self, game, assets, pos):
        super().__init__(assets, pos)

        self.game = game
        self.speed = 100
        self.acceleration[1] = 400
        self.air_time = 0
        self.jumps = 1
        self.auto_flip = 1
        self.render_rect = False

    def update(self, dt, tile_map):
        self.apply_force(dt, ((self.game.key_handler.actions['right'].is_held - self.game.key_handler.actions['left'].is_held) * self.speed, 0))
        
        if self.game.key_handler.actions['space'].is_pressed:
            if self.jumps > 0:
                self.velocity[1] = -225
                self.air_time = 0.1
                self.jumps -= 1

        if self.air_time > 0.1:
            if self.velocity[1] < 0:
                self.set_action('jump')
            else:
                self.set_action('fall')
        else:
            if self.next_movement[0] != 0:
                self.set_action('run')
            else:
                self.set_action('idle')
        
        self.physics_update(dt, tile_map)

        if self.collision['down']:
            self.air_time = 0
            self.jumps = 1
            self.velocity[1] = 0
        else:
            self.air_time += dt

        super().update(dt)