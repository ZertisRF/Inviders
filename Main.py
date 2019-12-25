import pygame
import time

from Inviders.GameParams import GameParams
from Inviders.fly_objects.SpaceShip import SpaceShip
from Inviders.fly_objects.Enemy_1 import Enemy_1

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
    x_enemy_1 = (gameParams.getWight() * 0.45)
    y_enemy_1 = 0
    spaceShip = SpaceShip(x, y, pygame, gameDisplay, gameParams)
    enemy_1 = Enemy_1(x_enemy_1, y_enemy_1, pygame, gameDisplay, gameParams)
    Exit = False
    x_c = 0
    y_c = 0
    x_c_enemy_1 = 0
    y_c_enemy_1 = 0
    Life_emeny_1 = True
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
            if Life_emeny_1 == True:
                y_c_enemy_1 += 1
        gameDisplay.fill(colour_white)
        spaceShip.changeCoord(x_c, y_c)
        spaceShip.display()
        enemy_1.changeCoord(x_c_enemy_1, y_c_enemy_1)
        enemy_1.display()
        pygame.display.update()
        clock.tick(60)


game()
pygame.quit()
quit()
