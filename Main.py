import pygame
import time
import os
import sys

from GameParams import GameParams
from fly_objects.SpaceShip import SpaceShip
from painter.Painter import Painter
from contents.pilot.FirstStage import FirstStage
from contents.ContentManager import ContentManager

pygame.init()
gameParams = GameParams()
gameParams.setHeight(600)
gameParams.setWidth(800)
colour_black = (0, 0, 0)
colour_white = (255, 255, 255)
colour_red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((gameParams.getWidth(), gameParams.getHeight()))
pygame.display.set_caption('Space_Race')
clock = pygame.time.Clock()
space_w = 50
width, height = 800, 600
FPS = 50


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


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():
    intro_text = ["INVADERS", "",
                  "Нажмите, чтобы начать"]

    clock = pygame.time.Clock()
    starter_background = pygame.transform.scale(load_image('starter_background.jpg'), (width, height))
    gameDisplay.blit(starter_background, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('white'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        gameDisplay.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                return
        pygame.display.flip()
        clock.tick(FPS)

fon = pygame.sprite.Group()
background = pygame.sprite.Sprite()
background.image = load_image("background.jpg")
background.rect = background.image.get_rect()
background.rect.x = 0
background.rect.y = 0
fon.add(background)
all_sprites = pygame.sprite.Group()
weapon_group = pygame.sprite.Group()

x = (gameParams.getWidth() * 0.45)
y = (gameParams.getHeight() * 0.8)
player = SpaceShip(x, y, pygame, gameDisplay, gameParams)
running = True
firstStage = FirstStage(pygame, gameDisplay, gameParams)
contentManager = ContentManager()
contentManager.setContents(firstStage.loadStageContent())
painter = Painter(time.time(), contentManager.getContent())
start_screen()
while running:
    for event in pygame.event.get():
        gameDisplay.fill(colour_white)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.update(event.type, event.key)
        if event.type == pygame.KEYUP:
            player.update(event.type, event.key)
    fon.draw(gameDisplay)
    player.changeCoord(player.x_c, player.y_c)
    player.display((player.get_x(), player.get_y()))
    painter.draw(time.time())
    contentManager.clearContent()
    pygame.display.update()
    clock.tick(60)
pygame.quit()
