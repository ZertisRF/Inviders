"""
Создает базовый класс для всех летающих объектов
"""


class BaseFlyObject:
    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.gameDisplay = gameDisplay
        self.gameParams = gameParams
        self.image = None
        self.wight = 0
        self.height = 0
        self.type = None

    def update(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def event(self, event):
        self.event = event

    def display(self, coords):
        self.gameDisplay.blit(self.image, coords)

    def changeCoord(self, x_c, y_c):
        self.x += x_c
        self.y += y_c

    def desroyed(self):
        return False

    def getSize(self):
        return self.wight, self.height

    def getType(self):
        return self.type

    def crashAction(self, strength):
        pass

    def getCrashStranges(self):
        return None
