from BaseFlyObject import BaseFlyObject
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


class EnergyStrike(BaseFlyObject):
    def __init__(self, pygame, gameDisplay, gameParams):
            super().__init__(None, None, pygame, gameDisplay, gameParams)
            self.image = load_image('ball.png', -1)
            self.image = pygame.transform.scale(self.image, (30, 30))
            self.mask = pygame.mask.from_surface(self.image)
            self.type = 'enemy'
            self.wight = 10
            self.height = 10
            self.life = 1
            self.type = 'friend'
            self.counter = 0

    def desroyed(self):
        return self.life <= 0

    def getSize(self):
        return self.wight, self.height

    def crashAction(self, strenght):
        self.life -= strenght
        self.counter += 100

    def getCrashStranges(self):
        return 50
