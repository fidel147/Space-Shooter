from settings import *

class AnimatedExplosion(pygame.sprite.Sprite):

    def __init__(self, frames, pos, groups):
        super().__init__(groups)
        self.frames_index, self.frames = 0, frames
        self.image = self.frames[0]
        self.rect = self.image.get_frect(center = pos)
        explosion_config['explosion_sound'].play()

    def explosion(self, dt):
        self.frames_index += explosion_config['speed'] * dt

        if self.frames_index < len(self.frames):
            self.image = self.frames[int(self.frames_index)]
        else:
            self.kill()

    def update(self, dt):
        self.explosion(dt)