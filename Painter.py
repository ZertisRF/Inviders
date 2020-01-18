"""
Рисует объекты, передынные Content'ом
"""
class Painter:
    def __init__(self, startTime, contents):
        self.startTime = startTime
        self.contents = contents

    def draw(self, currentTime):
        for content in self.contents.values():
            if not content.ended() and self.checkTime(content, currentTime):
                content.draw()

    def checkTime(self, content, currentTime):
        checkTime = currentTime - self.startTime >= content.getInterval()
        return checkTime
