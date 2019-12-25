from Inviders.fly_objects.BaseFlyObject import BaseFlyObject


class Enemy_1(BaseFlyObject):
    life = 100

    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        super().__init__(x, y, pygame, gameDisplay, gameParams)
        self.image = pygame.image.load('fly_objects/Enemy_1.jpg')

    def checkDestroy(self):
        return self.life <= 0
