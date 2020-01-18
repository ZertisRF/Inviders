"""
Компоновка объекта, его поведения и времени появления
"""
import time

class Content:
    def __init__(self, flyObject, conduct, interval):
        self.flyObject = flyObject
        self.conduct = conduct
        self.interval = interval
        self.id = time.time()

    def getId(self):
        return self.id

    def getInterval(self):
        return self.interval

    def draw(self):
        self.flyObject.display(self.conduct.getCoords())

    def ended(self):
        return self.flyObject.desroyed() or self.conduct.ended()

    def notEnded(self):
        return not self.ended()

    def getFlyObject(self):
        return self.flyObject

    def getCoords(self):
        return self.conduct.getCurrentCoords()
