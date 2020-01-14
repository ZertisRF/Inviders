'''
Создает корабль игрока, следит за тем, чтобы тот не вылетал за края игрового поля
'''

from fly_objects.BaseFlyObject import BaseFlyObject
from Main import player, game_over, weapon_group, all_sprites
from Enemy_1 import Enemy_list
import os
import pygame
width, height = 800, 600


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
    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        super().__init__(x, y, pygame, gameDisplay, gameParams)
        self.image = load_image('player.png', -1)
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x_c = 0
        self.y_c = 0
        self.life = 3

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

    def shoot(self):
        if self.weapon.available is False:
            self.weapon = Weapon(self.x, self.y)

    def damage(self):
        self.life -= 1
        if self.checkDestroy == 0:
            self.image = load_image('boom', -1)
            game_over()

    def update(self, type, key):
        if type == pygame.KEYDOWN:
            if key == pygame.K_LEFT:
                self.x_c -= 5
            if key == pygame.K_RIGHT:
                self.x_c += 5
            if key == pygame.K_UP:
                self.y_c -= 5
            if key == pygame.K_DOWN:
                self.y_c += 5
            if key == pygame.K_SPACE:
                self.shoot()
        if type == pygame.KEYUP:
            self.x_c = 0
            self.y_c = 0


class Weapon(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(weapon_group, all_sprites)
        self.image = load_image('ball', -1)
        self.image = pygame.transform.scale(self.image, (15, 15))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect().move(15 * pos_x, 15 * pos_y)
        self.available = True

    def update(self):
        if self.available:
            for enemy in Enemy_list:
                if not pygame.sprite.collide_mask(self, enemy):
                    self.rect = self.rect.move(0, 1)
                    if (self.rect[0] > width or self.rect[0] < 0) and (self.rect[1] > height or self.rect[1] < 0):
                        self.available = False
                else:
                    player.damage()
