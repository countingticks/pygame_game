import pygame

class KeyHandler:
    def __init__(self):
        self.actions = { 
            "up": False,
            "down": False,
            "left": False,
            "right": False,
            "space": False,
            "quit": False
        }

    def update(self):
        key = pygame.key.get_pressed()

        self.actions["up"] = key[pygame.K_w]
        self.actions["down"] = key[pygame.K_s]
        self.actions["left"] = key[pygame.K_a]
        self.actions["right"] = key[pygame.K_d]
        self.actions["space"] = key[pygame.K_SPACE]
        self.actions["quit"] = key[pygame.K_q]
