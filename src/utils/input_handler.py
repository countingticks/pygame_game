import pygame


class KeyState:
    def __init__(self):
        self._pressed = False
        self._released = False
        self._held = False
        self._key_state = False
        self._key_set = False
    
    @property
    def is_pressed(self):
        return self._pressed

    @property
    def is_released(self):
        return self._released
    
    @property
    def is_held(self):
        return self._held
    
    def set_key_state(self, state):
        if state != self._key_state:
            self._key_set = False
        self._key_state = state
    
    def update(self):
        if self._key_state is True:
            self._pressed = not self._key_set
            self._held = True
        else:
            self._released = not self._key_set and self._held
            self._pressed = False
            self._held = False

        self._key_set = self._key_state


class WheelState:
    def __init__(self):
        self._in_use = False
        self._state = False

    @property
    def in_use(self):
        return self._in_use
    
    def set_in_use(self):
        self._state = True
    
    def update(self):
        self._in_use = False
        
        if self._state is True:
            self._in_use = True
            self._state = False


class InputHandler:
    def __init__(self):
        self.actions = { 
            "up": KeyState(),
            "down": KeyState(),
            "left": KeyState(),
            "right": KeyState(),
            "e": KeyState(),
            "r": KeyState(),
            "g": KeyState(),
            "o": KeyState(),
            "space": KeyState(),
            "shift": KeyState(),
            "quit": KeyState(),
            "mouse_left": KeyState(),
            "mouse_right": KeyState(),
            "mouse_up": WheelState(),
            "mouse_down": WheelState()
        }

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.actions["quit"].set_key_state(True)
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    self.actions["up"].set_key_state(True)
                if event.key == pygame.K_s:
                    self.actions["down"].set_key_state(True)
                if event.key == pygame.K_a:
                    self.actions["left"].set_key_state(True)
                if event.key == pygame.K_d:
                    self.actions["right"].set_key_state(True)
                if event.key == pygame.K_e:
                    self.actions["e"].set_key_state(True)
                if event.key == pygame.K_r:
                    self.actions["r"].set_key_state(True)
                if event.key == pygame.K_g:
                    self.actions["g"].set_key_state(True)
                if event.key == pygame.K_o:
                    self.actions["o"].set_key_state(True)
                if event.key == pygame.K_SPACE:
                    self.actions["space"].set_key_state(True)
                if event.key == pygame.K_LSHIFT:
                    self.actions["shift"].set_key_state(True)
                if event.key == pygame.K_q:
                    self.actions["quit"].set_key_state(True)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.actions["mouse_left"].set_key_state(True)
                if event.button == 3:
                    self.actions["mouse_right"].set_key_state(True)
                if event.button == 4:
                    self.actions["mouse_up"].set_in_use()
                if event.button == 5:
                    self.actions["mouse_down"].set_in_use()
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.actions["up"].set_key_state(False)
                if event.key == pygame.K_s:
                    self.actions["down"].set_key_state(False)
                if event.key == pygame.K_a:
                    self.actions["left"].set_key_state(False)
                if event.key == pygame.K_d:
                    self.actions["right"].set_key_state(False)
                if event.key == pygame.K_e:
                    self.actions["e"].set_key_state(False)
                if event.key == pygame.K_r:
                    self.actions["r"].set_key_state(False)
                if event.key == pygame.K_g:
                    self.actions["g"].set_key_state(False)
                if event.key == pygame.K_o:
                    self.actions["o"].set_key_state(False)
                if event.key == pygame.K_SPACE:
                    self.actions["space"].set_key_state(False)
                if event.key == pygame.K_LSHIFT:
                    self.actions["shift"].set_key_state(False)

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.actions["mouse_left"].set_key_state(False)
                if event.button == 3:
                    self.actions["mouse_right"].set_key_state(False)

        for action in self.actions:
            self.actions[action].update()
