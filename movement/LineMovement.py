'''
Вычисляет таейкторию полета для врагов по углу и гипотинузе
'''
import math

class LineMovement:
    def __init__(self, alpha, length):
        self.startLength = 0
        self.length = abs(length)
        self.alpha = alpha


    def calculate(self, coords, incr):
        self.startLength += abs(incr)
        self.x = math.cos(math.radians(self.alpha)) * incr
        self.y = math.sin(math.radians(self.alpha)) * incr
        self.coords = coords[0] + self.x, coords[1] + self.y
        return self.coords

    def ended(self):
        return self.startLength > self.length

    def getEndCoords(self):
        return self.coords

