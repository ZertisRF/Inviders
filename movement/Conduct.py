"""
Создает модель поведения объекта, состоит траекторий
"""
class Conduct:
    def __init__(self, trajectories):
        self.trajectories = list(trajectories)
        self.isLive = True
        self.currentCoords = None

    def getCoords(self):
        for trajectory in self.trajectories:
            if not trajectory.ended():
                self.isLive = True
                self.currentCoords = trajectory.getNewCoords()
                return self.currentCoords
            else:
                continue

    def isAlive(self):
        self.isLive = not self.trajectories[len(self.trajectories)-1].ended()
        return self.isLive

    def ended(self):
        self.isLive = not self.trajectories[len(self.trajectories)-1].ended()
        return not self.isLive

    def getCurrentCoords(self):
        return self.currentCoords
