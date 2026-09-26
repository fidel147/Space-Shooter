from settings import *
from player import *
from explosion import AnimatedExplosion

"""

This script is written by Fidele ZOGBE, a CS student.
It showed how OOP and pygame are powerful for game genering.
Thank ClearCode for showing your code as reference.

"""

class Game:

    def __init__(self):

        pygame.init()
        self.root = pygame.display.set_mode((screen_config['width'], 
                                             screen_config['height']))
        self.clock = pygame.time.Clock()
        screen_config['game_music'].set_volume(0.4)
        screen_config['game_music'].play()

        #groups
        self.all_sprites = pygame.sprite.Group()
        self.meteor_sprites = pygame.sprite.Group()
        self.laser_sprites = pygame.sprite.Group()

        pygame.display.set_caption(screen_config['title'])

        #stars positions
        self.__pos = [(randint(0, 
                               screen_config['width']), 
                               randint(0, screen_config['height'])) for _ in range(50)]
        
        #display the stars
        for pos in self.__pos:
            Parent(self.root, 
                    pygame.image.load(star_config['image'])\
                        .convert_alpha(),
                        pos, self.all_sprites)
            
        #player label
        image = pygame.image.load(player_config['image'])\
            .convert_alpha()
        self.player = Player(self.root, image, 
                             (screen_config['width']/2, 
                                                                 screen_config['height']/2),
                                                                 self.all_sprites, self.laser_sprites)


        self.is_running = True

        #font display
        self.font = pygame.font.Font(score_config['image'], score_config['size'])

        #create meteor event
        self.meteor_event = pygame.event.custom_type()
        pygame.time.set_timer(self.meteor_event, 500)

    def collision(self):
        if collison_sprites:=pygame.sprite\
            .spritecollide(self.player, self.meteor_sprites, True, pygame.sprite.collide_mask):
                        player_config['damage_sound'].play()
                        self.is_running = False
        
        for laser in self.laser_sprites:
            if collided_sprites := pygame.sprite\
                .spritecollide(laser, 
                                                                self.meteor_sprites, True, pygame.sprite.collide_mask):
                laser.kill()
                AnimatedExplosion(explosion_config['frames'], laser.rect.midtop, self.all_sprites)

    def display_score(self):
        current_time = pygame.time.get_ticks()//100
        text_surf = self.font.render(str(current_time), True, score_config['color'])
        text_rect = text_surf.get_frect(midbottom = (screen_config['width']/2, screen_config['height'] - 50))
        self.root.blit(text_surf, text_rect)
        pygame.draw.rect(self.root, (240, 240, 240), text_rect.inflate(20, 20).move(0, -8), 5, 10)

    def run(self):
        while self.is_running:

            dt = self.clock.tick() / 1000
            #pygame event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False
                if event.type == self.meteor_event:
                    pos = (randint(0, screen_config['width']), randint(-300, -100))
                    Meteor(pygame.image.load(meteor_config['image'])\
                           .convert_alpha(),
                           pos, (self.all_sprites, self.meteor_sprites))
            #config the screen and update it
            self.all_sprites.update(dt)

            #collisions sprites
            self.collision()
            self.root.fill(screen_config['color'])
            self.display_score()
            self.all_sprites.draw(self.root)
            pygame.display.update()

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run()         