'''
Класс, хранящий в себе информацию о противнике
'''
from Inviders.fly_objects.BaseFlyObject import BaseFlyObject


class Enemy_1(BaseFlyObject):
    life = 100

    def __init__(self, pygame, gameDisplay, gameParams):
        super().__init__(None, None, pygame, gameDisplay, gameParams)
        self.image = pygame.image.load('fly_objects/Enemy_1.jpg')

    def checkDestroy(self):
        return self.life <= 0
