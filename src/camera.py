class Camera:
    def __init__(self, size, pos=(0, 0), slowness=1):
        self.pos = list(pos)
        self.size = size
        self.slowness = slowness

        self.int_pos = (int(self.pos[0]), int(self.pos[1]))
        self.target_entity = None
        self.target_pos = None

    def __getitem__(self, item):
        return self.int_pos[item]

    @property
    def target(self):
        if self.target_entity:
            return (self.target_entity.center[0] - self.size[0] // 2, self.target_entity.center[1] - self.size[1] // 2)
        elif self.target_pos:
            return (self.target_pos[0] - self.size[0] // 2, self.target_pos[0] - self.size[1] // 2)

    def set_target(self, target):
        if hasattr(target, 'center'):
            self.target_entity = target
            self.target_pos = None
        elif target:
            self.target_pos = tuple(target)
            self.target_entity = None
        else:
            self.target_pos = None
            self.target_entity = None

    def update(self, dt):
        target = self.target
        if target:
            self.pos[0] = self.smooth_approach(dt, self.pos[0], target[0], slowness=self.slowness)
            self.pos[1] = self.smooth_approach(dt, self.pos[1], target[1], slowness=self.slowness)

        self.int_pos = (int(self.pos[0]), int(self.pos[1]))

    def smooth_approach(self, dt, val, target, slowness=1):
        val += (target - val) / slowness * min(dt, slowness)
        return val