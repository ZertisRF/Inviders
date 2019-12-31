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
        self.x = math.cos(self.alpha) * incr
        self.y = math.sin(self.alpha) * incr
        return coords[0] + self.x, coords[1] + self.y

    def ended(self):
        return self.startLength > self.length

