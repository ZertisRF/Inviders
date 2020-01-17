'''
Класс, хранящий в себе информацию о противнике
'''

from fly_objects.BaseFlyObject import BaseFlyObject
import os
import pygame

def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Enemy_1(BaseFlyObject):
    def __init__(self, pygame, gameDisplay, gameParams):
        super().__init__(None, None, pygame, gameDisplay, gameParams)
        self.image = load_image('enemy.png', -1)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.mask = pygame.mask.from_surface(self.image)
        self.type = 'enemy'
        self.wight = 50
        self.height = 50

    def boom(self):
        self.image = load_image('boom', -1)