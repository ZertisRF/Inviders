import random

from fly_objects.Enemy_1 import Enemy_1
from contents.Content import Content
from movement.Conduct import Conduct
from movement.LineMovement import LineMovement
from movement.Trajectory import Trajectory


class FirstStage:
    def __init__(self, pygame, gameDisplay, gameParams):
        self.pygame = pygame
        self.gameParams = gameParams
        self.gameDisplay = gameDisplay

    def loadStageContent(self):
        contents = []
        for i in range(5, 35, 5):
            contents.append(self.getContent('Base_enemy', 'Left_movement', i))
        for i in range(2, 32, 5):
            contents.append(self.getContent('Base_enemy', 'Right_movement', i))
        for i in range(4, 35, 5):
            contents.append(self.getContent('Base_enemy', 'Left_movement', i))
        for i in range(3, 32, 5):
            contents.append(self.getContent('Base_enemy', 'Right_movement', i))
        return contents

    def getContent(self, enemyName, conductName, time):
        enemy = self.getEnemy(enemyName)
        conduct = self.getConduct(conductName)
        return Content(enemy, conduct, time)


    def getEnemy(self, enemyName):
        if enemyName == 'Base_enemy':
            return Enemy_1(self.pygame, self.gameDisplay, self.gameParams)


    def getConduct(self, conductName):
        if conductName == 'Left_movement':
            return Conduct(self.getLeftTrajectories())
        elif conductName == 'Right_movement':
            return Conduct(self.getRightTrajectories())

    def getLeftTrajectories(self):
        lineM = LineMovement(random.randrange(75, 100), 250)
        lineM2 = LineMovement(random.randrange(115, 150), 250)
        lineM3 = LineMovement(random.randrange(165, 195), 250)
        lineM4 = LineMovement(random.randrange(210, 240), 250)
        movements = []
        movements.append(lineM)
        movements.append(lineM2)
        movements.append(lineM3)
        movements.append(lineM4)
        trajectory = Trajectory(self.gameParams, movements, (random.randrange(400, self.gameParams.getWidth() - 150), -50), incr=4)
        trajectories = []
        trajectories.append(trajectory)
        return trajectories

    def getRightTrajectories(self):
        lineM = LineMovement(random.randrange(75, 100), 250)
        lineM2 = LineMovement(random.randrange(30, 60), 250)
        lineM3 = LineMovement(random.randrange(0, 15), 250)
        lineM4 = LineMovement(random.randrange(300, 330), 250)
        movements = []
        movements.append(lineM)
        movements.append(lineM2)
        movements.append(lineM3)
        movements.append(lineM4)
        trajectory = Trajectory(self.gameParams, movements, (random.randrange(150, self.gameParams.getWidth() - 400), -50), incr=4)
        trajectories = []
        trajectories.append(trajectory)
        return trajectories
