import time
import sys
import pygame
import os

from SpaceShip import SpaceShip
from Painter import Painter
from FirstStage import FirstStage
from ContentManager import ContentManager, gameParams
from Content import Content
from EnergyStrike import EnergyStrike
from os import path
from pygame import mixer

file = 'music.mp3'
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play(-1)

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


pygame.init()
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
energyStrike = EnergyStrike(pygame, gameDisplay, gameParams)


def draw():
    font = pygame.font.Font(None, 50)
    text = font.render(str(gameParams.count), 1, (100, 255, 100))
    text_x = 700
    text_y = 0
    gameDisplay.blit(text, (text_x, text_y))

def draw_window():
    font = pygame.font.Font(None, 50)
    text = font.render('Congratulations, you killed ' + str(gameParams.count // 100) + ' enemies', 1, (100, 255, 100))
    text_x = 75
    text_y = 200
    gameDisplay.blit(text, (text_x, text_y))

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

start_screen()
x = (gameParams.getWidth() * 0.45)
y = (gameParams.getHeight() * 0.8)
player = SpaceShip(x, y, pygame, gameDisplay, gameParams)
running = True
firstStage = FirstStage(pygame, gameDisplay, gameParams)
contentManager = ContentManager()
contentManager.setContents(firstStage.loadStageContent())
painter = Painter(time.time(), contentManager.getContent())


def getShootContent(player):
    strike = EnergyStrike(pygame, gameDisplay, gameParams)
    shootContent = Content(strike, firstStage.getShootConduct((player.get_x() + 20, player.get_y() - 5)), 1)
    return [shootContent]


while running:
    for event in pygame.event.get():
        gameDisplay.fill(colour_white)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            player.update(event.type, event.key)
            if event.key == pygame.K_SPACE:
                contentManager.setContents(getShootContent(player))
        if event.type == pygame.KEYUP:
            player.update(event.type, event.key)
    fon.draw(gameDisplay)
    player.changeCoord(player.x_c, player.y_c)
    player.display((player.get_x(), player.get_y()))
    painter.draw(time.time())
    contentManager.analize()
    draw()
    if gameParams.count_enemies >= 2200:
        draw_window()
    contentManager.clearContent()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
