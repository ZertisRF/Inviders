'''
Создает корабль игрока, следит за тем, чтобы тот не вылетал за края игрового поля
'''

from fly_objects.BaseFlyObject import BaseFlyObject
from fly_objects.Enemy_1 import Enemy_1
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


class SpaceShip(BaseFlyObject):
    life = 100

    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        super().__init__(x, y, pygame, gameDisplay, gameParams)
        self.image = load_image('player.png', -1)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x_c = 0
        self.y_c = 0
        self.type = 'friend'
        self.wight = 70
        self.height = 70

    def checkDestroy(self):
        return self.life <= 0

    def changeCoord(self, x_c, y_c):
        if 0 < self.y < self.gameParams.getHeight() - 50:
            change = self.y + y_c
            if change > self.gameParams.getHeight() - 50:
                self.y += self.gameParams.getHeight() - 50
            elif change < 0:
                self.y = 0
            else:
                self.y += y_c
        elif self.y > self.gameParams.getHeight() - 80:
            self.y -= 20
        elif self.y >= 0:
            self.y += 10
        if 0 < self.x < self.gameParams.getWidth() - 50:
            change = self.x + x_c
            if change > self.gameParams.getWidth() - 50:
                self.x += self.gameParams.getWidth() - 50
            elif change < 0:
                self.x = 0
            else:
                self.x += x_c
        elif self.x > self.gameParams.getWidth() - 80:
            self.x -= 20
        elif self.x >= 0:
            self.x += 10

    def destroy(self):
        self.image = pygame.image.load('fly_objects/boom.png')

    def update(self, type, key):
        '''
        if pygame.sprite.collide_mask(self, Enemy_1):
            self.life -= 10
            print(-10)
        '''
        if type == pygame.KEYDOWN:
            if key == pygame.K_LEFT:
                self.x_c -= 5
            if key == pygame.K_RIGHT:
                self.x_c += 5
            if key == pygame.K_UP:
                self.y_c -= 5
            if key == pygame.K_DOWN:
                self.y_c += 5
        if type == pygame.KEYUP:
            self.x_c = 0
            self.y_c = 0
