from Main import load_image
import pygame


weapon_group = pygame.sprite.Group()

class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, screen):
        super().__init__(weapon_group)
        self.image = load_image('ball.png', -1)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.vy = 10

    def update(self):
        self.vy = -self.vy
        self.rect.y = self.y