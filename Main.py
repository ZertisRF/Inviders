import pygame
import time
import os

from GameParams import GameParams
from fly_objects.SpaceShip import SpaceShip
from painter.Painter import Painter
from contents.pilot.pilot import getPilotContent

pygame.init()
gameParams = GameParams()
gameParams.setHeight(600)
gameParams.setWight(800)
colour_black = (0, 0, 0)
colour_white = (255, 255, 255)
colour_red = (255, 0, 0)
gameDisplay = pygame.display.set_mode((gameParams.getWight(), gameParams.getHeight()))
pygame.display.set_caption('Space_Race')
clock = pygame.time.Clock()
space_w = 50
width, height = 600, 800


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


fon = pygame.sprite.Group()
background = pygame.sprite.Sprite()
background.image = load_image("background.jpg")
background = pygame.transform.scale(load_image('background.jpg'), (width, height))
background.rect = background.image.get_rect()
background.rect.x = 0
background.rect.y = 0
fon.add(background)


def text_objects(text, font):
    textSurf = font.render(text, True, colour_black)
    return textSurf, textSurf.get_rect()


def m_display(text):
    Text = pygame.font.Font('freesansbold.ttf', 50)
    TextS, TextR = text_objects(text, Text)
    TextR.center = ((gameParams.getWight() / 2), (gameParams.getHeight() / 2))
    gameDisplay.blit(TextS, TextR)
    pygame.display.update()
    time.sleep(3)
    game()


def destroy():
    m_display('Your spaceship destroyed!')


def game():
    x = (gameParams.getWight() * 0.45)
    y = (gameParams.getHeight() * 0.8)
    spaceShip = SpaceShip(x, y, pygame, gameDisplay, gameParams)
    Exit = False
    x_c = 0
    y_c = 0
    painter = Painter(time.time(), getPilotContent(pygame, gameDisplay, gameParams))
    while not Exit:
        for event in pygame.event.get():
            gameDisplay.fill(colour_white)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_c += -5
                elif event.key == pygame.K_RIGHT:
                    x_c += 5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_c -= 5
                elif event.key == pygame.K_DOWN:
                    y_c += 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT \
                        or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_c = 0
                    y_c = 0
        fon.draw(gameDisplay)
        spaceShip.changeCoord(x_c, y_c)
        spaceShip.display((spaceShip.get_x(), spaceShip.get_y()))
        painter.draw(time.time())
        painter.clearContent()
        pygame.display.update()
        clock.tick(60)


game()
pygame.quit()
quit()
