"""
Создает модель поведения объекта, состоит траекторий
"""
class Conduct:
    def __init__(self, trajectories):
        self.trajectories = list(trajectories)
        self.isLive = True

    def getCoords(self):
        for trajectory in self.trajectories:
            if not trajectory.ended():
                self.isLive = True
                return trajectory.getNewCoords()
            else:
                continue

    def isAlive(self):
        self.isLive = not self.trajectories[len(self.trajectories)-1].ended()
        return self.isLive

    def ended(self):
        self.isLive = not self.trajectories[len(self.trajectories)-1].ended()
        return not self.isLive
