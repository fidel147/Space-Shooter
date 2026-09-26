from os import walk
from os.path import join
import pygame
from random import randint, uniform

pygame.mixer.init()

screen_config = {
    'width': 1200,
    'height': 650,
    'color': '#3a2e3f',
    'title': 'space shooter'.title(),
    'game_music': pygame.mixer.Sound(join('audio', 'game_music.wav'))
}

player_config = {
    'image': join('images', 'player.png'),
    'speed': 300,
    'damage_sound': pygame.mixer.Sound(join('audio', 'damage.ogg')),
}

score_config = {
    'image' : join('images', 'Oxanium-Bold.ttf'),
    'size': 20,
    'color': (240, 240, 240),
}

laser_config = {
    'image': join('images', 'laser.png'),
    'speed': 400,
    'sound': pygame.mixer.Sound(join('audio', 'laser.wav')),
}

meteor_config = {
    'image': join('images', 'meteor.png'), 
    'speed': randint(300, 400),
    'rotation_speed': randint(40, 80),
}

star_config = {
    'image': join('images', 'star.png') # /home/zogbefidele/Desktop/Space_Shooter/images/star.png
}

explosion_config = {
    'frames': [pygame.image\
               .load(join('images', 'explosion', f'{i}.png')) for i in range(21)],
    'speed': randint(20, 25),
    'explosion_sound': pygame.mixer.Sound(join('audio', 'explosion.wav'))
}
