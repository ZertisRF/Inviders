class Conduct:
    def __init__(self, trajectories):
        self.trajectories = list(trajectories)

    def getCoords(self):
        coords = None
        for trajectory in self.trajectories:
            if not trajectory.notEnded():
                coords = trajectory.getEndCoords()
            elif coords:
                trajectory.setBeginCoords(coords)
                return trajectory.getNewCoords()
            else:
                return trajectory.getNewCoords()
