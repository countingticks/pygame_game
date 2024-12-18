import pygame

from src.animation import Animation


class Entity:
    def __init__(self, assets, camera, pos, image_duration=20, custom_collision_size=None):
        self.assets = assets
        self.pos = list(pos)
        self.size = self.assets['idle']['dimensions']
        self.custom_collision_size = self.size if custom_collision_size is None else custom_collision_size
        self.offset_size = ((self.size[0] - self.custom_collision_size[0]) // 2, (self.size[1] - self.custom_collision_size[1]))
        self.action = None

        self.opacity = 255
        self.scale = [1, 1]
        self.rotation = 0
        self.auto_flip = 0
        self.flip = [False, False]

        self.visible = True
        self.render_rect = False
        self.animation = Animation(self.assets, camera, image_duration=image_duration)

    @property
    def rect(self):
        return pygame.Rect(*self.pos, *self.size)
    
    @property
    def collision_rect(self):
        if self.custom_collision_size == None or self.custom_collision_size == self.size:
            return self.rect
        
        difference = ((self.size[0] - self.custom_collision_size[0]), (self.size[1] - self.custom_collision_size[1]))
        buffer = (self.pos[0] + difference[0] / 2, self.pos[1] + difference[1])

        return pygame.Rect(*buffer, *self.custom_collision_size)
    
    @property
    def center(self):
        return self.rect.center
    
    @property
    def collision_center(self):
        return self.collision_rect.center
    
    def set_action(self, action):
        if self.action == action:
            return
        self.action = action    
    
    def update(self, dt):
        self.animation.update(dt, self.action)

    def render(self, surface, offset=(0, 0)):
        if self.visible:
            self.animation.render(surface, (self.pos[0] - offset[0], self.pos[1] - offset[1]), selected_group=self.action, flip=self.flip)
            if self.render_rect:
                pygame.draw.rect(surface, (255, 255, 0), (self.rect.x - offset[0], self.rect.y - offset[1], self.rect.width, self.rect.height), 1)
                pygame.draw.rect(surface, (255, 255, 255), (self.collision_rect.x - offset[0], self.collision_rect.y - offset[1], self.collision_rect.width, self.collision_rect.height), 1)
                pygame.draw.circle(surface, (255, 0, 0), (self.collision_center[0] - offset[0], self.collision_center[1] - offset[1]), 2)


class PhysicsEntity(Entity): 
    def __init__(self, assets, camera, pos, image_duration=20, custom_collision_size=None):
        super().__init__(assets, camera, pos, image_duration, custom_collision_size)
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
        for rect in tile_map.collision_tiles_around(self.collision_center):
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
                    self.pos[0] = entity_rect.x - self.offset_size[0]
                if entity_rect.y != self.collision_rect.y:
                    self.pos[1] = entity_rect.y - self.offset_size[1]
                entity_rect = self.collision_rect

    def apply_force(self, dt, vec):
        self.next_movement[0] += vec[0] * dt
        self.next_movement[1] += vec[1] * dt
