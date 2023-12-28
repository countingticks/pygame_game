import pygame

from src.animation import Animation


class Entity:
    def __init__(self, entity_type, pos):
        self.type = entity_type
        self.pos = list(pos)
        self.size = (32, 32) # we will take this info from a config later on
        self.size_collision = (22, 26)
        self.size_offset = ((self.size[0] - self.size_collision[0]) / 2, (self.size[1] - self.size_collision[1]))
        self.action = None

        self.opacity = 255
        self.scale = [1, 1]
        self.rotation = 0
        self.auto_flip = 0
        self.flip = [False, False]

        self.visible = True
        self.render_rect = False
        self.animation = Animation(self.type, image_duration=20)

    @property
    def rect(self):
        return pygame.Rect(*self.pos, *self.size)
    
    @property
    def collision_rect(self):
        diff = ((self.size[0] - self.size_collision[0]), (self.size[1] - self.size_collision[1]))
        tmp_pos = (self.pos[0] + diff[0] / 2, self.pos[1] + diff[1])
        return pygame.Rect(*tmp_pos, *self.size_collision)
    
    @property
    def center(self):
        return self.rect.center
    
    def set_action(self, action):
        if self.action == action:
            return
        self.action = action    
    
    def update(self, dt):
        self.animation.update(self.action, dt)

    def render(self, surface):
        if self.visible:
            self.animation.render(surface, self.action, self.flip, self.pos)
            if self.render_rect:
                pygame.draw.rect(surface, (255, 255, 0), self.rect, 1)
                pygame.draw.rect(surface, (255, 255, 255), self.collision_rect, 1)
            

class PhysicsEntity(Entity): 
    def __init__(self, entity_type, pos):
        super().__init__(entity_type, pos)
        self.collision = {'up': False, 'down': False, 'left': False, 'right': False}

        self.velocity = [0, 0]
        self.velocity_max = (100, 500)

        self.next_movement = [0, 0]
        self.acceleration = [0, 0]

    def physics_update(self, dt, tile_map): 
        if self.next_movement[0] * self.auto_flip > 0:
            self.flip[0] = False
        elif self.next_movement[0] * self.auto_flip < 0:
            self.flip[0] = True

        self.velocity[0] += self.acceleration[0] * dt
        self.velocity[1] += self.acceleration[1] * dt

        self.velocity[0] = max(-self.velocity_max[0], min(self.velocity[0], self.velocity_max[0]))
        self.velocity[1] = max(-self.velocity_max[1], min(self.velocity[1], self.velocity_max[1]))
        
        self.next_movement[0] += self.velocity[0] * dt
        self.next_movement[1] += self.velocity[1] * dt

        self.physics_move(tile_map, self.next_movement)
        
        if self.collision['down'] or self.collision['up']:
            self.velocity[1] = 0

        self.next_movement = [0, 0]

    def physics_move(self, tile_map, movement):
        self.pos[0] += movement[0]
        self.physics_processor((movement[0], 0), tile_map)
        self.pos[1] += movement[1]
        self.physics_processor((0, movement[1]), tile_map)

    def physics_processor(self, movement, tile_map):
        self.collision = {'up': False, 'down': False, 'left': False, 'right': False}

        entity_rect = self.collision_rect
        for rect in tile_map.collision_tiles_around(self.pos):
            if entity_rect.colliderect(rect):
                if movement[0] > 0:
                    entity_rect.right = rect.left
                    self.collision['right'] = True
                if movement[0] < 0:
                    entity_rect.left = rect.right
                    self.collision['left'] = True
                if movement[1] > 0:
                    entity_rect.bottom = rect.top
                    self.collision['down'] = True
                if movement[1] < 0:
                    entity_rect.top = rect.bottom
                    self.collision['up'] = True

                if entity_rect.x != self.collision_rect.x:
                    self.pos[0] = entity_rect.x - self.size_offset[0]
                if entity_rect.y != self.collision_rect.y:
                    self.pos[1] = entity_rect.y - self.size_offset[1]
                entity_rect = self.collision_rect


        # if (movement[0]):
        #     if movement[0] == 1:
        #         self.velocity[0] = min(self.velocity[0] + self.acceleration[0] * dt, self.velocity_max[0])
        #     else:
        #         self.velocity[0] = -min(-self.velocity[0] + self.acceleration[0] * dt, self.velocity_max[0])
        # else:
        #     if self.velocity[0] > 0:
        #         self.velocity[0] = max(self.velocity[0] - self.deceleration[0] * dt, 0)
        #     else:
        #         self.velocity[0] = -max(-self.velocity[0] - self.deceleration[0] * dt, 0)

        # self.pos[0] += self.velocity[0] * dt
        # entity_rect = self.rect
        # for rect in tile_map.collision_tiles_around(self.pos):
        #     if entity_rect.colliderect(rect):
        #         if self.velocity[0] > 0:
        #             entity_rect.right = rect.left
        #             self.collision['right'] = True
        #         if self.velocity[0] < 0:
        #             entity_rect.left = rect.right
        #             self.collision['left'] = True
        #         self.pos[0] = entity_rect.x

        # self.velocity[1] = min(self.velocity[1] + 10 * dt, 10)
        # self.pos[1] += self.velocity[1]
        # entity_rect = self.rect
        # for rect in tile_map.collision_tiles_around(self.pos):
        #     if entity_rect.colliderect(rect):
        #         if self.velocity[1] > 0:
        #             entity_rect.bottom = rect.top
        #             self.collision['down'] = True
        #         if self.velocity[1] < 0:
        #             entity_rect.top = rect.bottom
        #             self.collision['up'] = True
        #         self.pos[1] = entity_rect.y

        # if self.collision['down'] or self.collision['up']:
        #     self.velocity[1] = 0

        # if self.velocity[1] > 0:
        #     self.action = 'fall'
        # elif self.velocity[1] < 0:
        #     self.action = 'jump'
        # else: 
        #     if self.velocity[0] != 0:
        #         self.action = 'run'
        #     else:
        #         self.action = 'idle'

    def apply_force(self, dt, vec):
        self.next_movement[0] += vec[0] * dt
        self.next_movement[1] += vec[1] * dt
