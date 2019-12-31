import pygame
import time

from Inviders.GameParams import GameParams
from Inviders.fly_objects.SpaceShip import SpaceShip
from Inviders.painter.Painter import Painter

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
    from Inviders.contents.pilot.pilot import getPilotContent
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
        gameDisplay.fill(colour_white)
        spaceShip.changeCoord(x_c, y_c)
        spaceShip.display((spaceShip.get_x(), spaceShip.get_y()))
        painter.draw(time.time())
        pygame.display.update()
        clock.tick(60)


game()
pygame.quit()
quit()
