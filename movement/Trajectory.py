"""
Траектория полёты объекта, состоит из объектов расчёта следующего положения
"""
class Trajectory:
    def __init__(self, gameParams, movements, coords, incr=1):
        self.incr = incr
        self.gameParams = gameParams
        self.movements = movements
        self.Ended = False
        self.coords = coords
        self.beginCoords = False

    def getNewCoords(self):
        for movement in self.movements:
            if not movement.ended():
                self.coords = movement.calculate(self.coords, self.incr)
                return self.coords
            else:
                continue

    def setCoords(self, x, y):
        self.coords[0] = x
        self.coords[1] = y

    def setIncrements(self, incr):
        self.incr = incr

    def setBeginCoords(self, coords):
        if not self.beginCoords:
            self.coords = coords
            self.beginCoords = True

    def getEndCoords(self):
        return self.coords

    def notEnded(self):
        if len(self.movements) > 0:
            self.Ended = self.movements[len(self.movements)-1].ended()
        return not self.Ended

    def ended(self):
        if len(self.movements) > 0:
            self.Ended = self.movements[len(self.movements)-1].ended()
        return self.Ended
