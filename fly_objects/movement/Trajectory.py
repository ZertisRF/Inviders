class Trajectory:
    def __init__(self, gameParams, function, coords, incrLimit, incr=1):
        self.incr = incr
        self.gameParams = gameParams
        self.function = function
        self.incrLimit = incrLimit
        self.incrStart = 0
        self.x = coords[0]
        self.y = coords[1]
        self.beginCoords = False

    def getNewCoords(self):
        self.incrStart += self.incr
        self.x += self.incr
        self.y = self.function(self.x)
        return self.x, self.y

    def setCoords(self, x, y):
        self.x = x
        self.y = y

    def setIncrements(self, incr):
        self.incr = incr

    def setBeginCoords(self, coords):
        if not self.beginCoords:
            self.x = coords[0]
            self.y = coords[1]
            self.beginCoords = True

    def getEndCoords(self):
        return self.x, self.y

    def notEnded(self):
        return self.incrStart > self.incrLimit
