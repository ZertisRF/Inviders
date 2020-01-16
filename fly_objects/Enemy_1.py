'''
Класс, хранящий в себе информацию о противнике
'''

from fly_objects.BaseFlyObject import BaseFlyObject
from Main import load_image


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