from settings import *

class Parent(pygame.sprite.Sprite):

    def __init__(self, root, image, pos, groups):
        super().__init__(groups)
        self.root = root
        self.image = image
        self.rect = self.image.get_frect(center = pos)

class Player(Parent):

    def __init__(self, root, image, pos , groups, laser_sprites):
        super().__init__(root, image, pos, groups)
        self.direction = pygame.Vector2()
        self.speed = player_config['speed']
        self.all_sprites = groups
        self.image_back = image
        self.laser_sprites = laser_sprites

        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 400
        

    def update(self, dt):
        self.get_pressed(dt)
        self.recent_keys()

    def get_pressed(self, dt):
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction else self.direction
        self.rect.center += self.speed * self.direction * dt

    def recent_keys(self):
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE] and self.can_shoot:
            Laser(self.rect.midtop, 
                  pygame.image.load(laser_config['image'])\
                    .convert_alpha(), 
                  (self.all_sprites, self.laser_sprites))
            self.can_shoot = False
            laser_config['sound'].play()
            self.image = pygame.transform.grayscale(self.image)
            self.laser_shoot_time = pygame.time.get_ticks()
        self.laser_timer()

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_shoot_time >= self.cooldown_duration:
                self.can_shoot = True
                self.image = self.image_back
        
class Laser(pygame.sprite.Sprite):

    def __init__(self, pos, image, groups):
        super().__init__(groups)
        self.image = image
        self.image = pygame.transform.scale(self.image, (15, 30))
        self.rect = self.image.get_frect(midbottom = pos)

    def update(self, dt):
        self.rect.centery -= laser_config['speed'] * dt
        if self.rect.bottom < 0:
            self.kill()

class Meteor(pygame.sprite.Sprite):

    def __init__(self, image, pos, groups):
        super().__init__(groups)
        self.image_surf = image
        self.image = self.image_surf
        self.rect = self.image.get_frect(center = pos)
        self.start_time = pygame.time.get_ticks()
        self.lifetime = 3000
        self.direction = pygame.Vector2(uniform(-0.5, 0.5), 1)
        self.rotaion_speed = meteor_config['rotation_speed']
        self.rotaion = 0

    def motion(self, dt):
        self.rect.center += meteor_config['speed'] * dt * self.direction

        if pygame.time.get_ticks() - self.start_time >= self.lifetime:
            self.kill()

        self.rotaion += self.rotaion_speed * dt
        self.image = pygame.transform.rotozoom(self.image_surf, self.rotaion, 1)
        self.rect = self.image.get_frect(center = self.rect.center)

    def update(self, dt):
        self.motion(dt)