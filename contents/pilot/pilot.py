'''
Рисует полет противника по заданным траекториям
'''
from Inviders.contents.Content import Content
from Inviders.fly_objects.Enemy_1 import Enemy_1
from Inviders.movement.Conduct import Conduct
from Inviders.movement.LineMovement import LineMovement
from Inviders.movement.Trajectory import Trajectory


def getPilotContent(pygame, gameDisplay, gameParams):
    enemy = Enemy_1(pygame, gameDisplay, gameParams)
    lineM = LineMovement(90, 300)
    movements = []
    movements.append(lineM)
    trajectory = Trajectory(gameParams, movements, (gameParams.getWight() // 2,-50))
    trajectories = []
    trajectories.append(trajectory)
    conduct = Conduct(trajectories)
    content = Content(enemy, conduct, 5)
    contents = []
    contents.append(content)
    return contents
