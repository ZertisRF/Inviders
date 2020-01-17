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


class Weapon(pygame.sprite.Sprite):
    def __init__(self, x, y, group):
        super().__init__(group)
        self.image = load_image('ball.png', -1)
        self.image = pygame.transform.scale(self.image, (30, 30))
        self.rect = pygame.Rect(x, y, 30, 30)
        self.x = x
        self.y = y
        self.vy = 20

    def update(self):
        self.y -= self.vy
        self.rect = self.rect.move(0, -self.vy)