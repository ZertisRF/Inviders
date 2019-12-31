'''
Создает корабль игрока, следит за тем, чтобы тот не вылетал за края игрового поля
'''
from Inviders.fly_objects.BaseFlyObject import BaseFlyObject


class SpaceShip(BaseFlyObject):
    life = 100

    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        super().__init__(x, y, pygame, gameDisplay, gameParams)
        self.image = pygame.image.load('fly_objects/space_destroyer.jpg')

    def checkDestroy(self):
        return self.life <= 0

    def changeCoord(self, x_c, y_c):
        if self.y < self.gameParams.getHeight() - 50 and self.y > 0:
            change = self.y + y_c
            if change > self.gameParams.getHeight() - 50:
                self.y += self.gameParams.getHeight() - 50
            elif change < 0:
                self.y = 0
            else:
                self.y += y_c
        else:
            self.y -= y_c
        if self.x < self.gameParams.getWight() - 50 and self.x > 0:
            change = self.x + x_c
            if change > self.gameParams.getWight() - 50:
                self.x += self.gameParams.getWight() - 50
            elif change < 0:
                self.x = 0
            else:
                self.x += x_c
        elif self.x > self.gameParams.getWight() - 80:
            self.x -= 20
        elif self.x >= 0:
            self.x += 10
