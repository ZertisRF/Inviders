"""
Создает модель поведения объекта, состоит траекторий
"""
class Conduct:
    def __init__(self, trajectories):
        self.trajectories = list(trajectories)
        self.isLive = True

    def getCoords(self):
        coords = None
        for trajectory in self.trajectories:
            if trajectory.ended():
                 coords = trajectory.getEndCoords()
                 self.isAlive = False
            elif coords:
                trajectory.setBeginCoords(coords)
                self.isAlive = True
                return trajectory.getNewCoords()
            else:
                return trajectory.getNewCoords()

    def isAlive(self):
        return self.isLive

    def ended(self):
        return not self.isLive
