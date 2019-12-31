"""
Рисует объекты, передынные Content'ом
"""
class Painter:
    def __init__(self, startTime, contents):
        self.startTime = startTime
        self.contents = {}
        self.initContents(contents)

    def initContents(self, contents):
        for content in contents:
            self.contents[content.getId] = content


    def draw(self, currentTime):
        for content in self.contents.values():
            if content.ended():
                self.contents.pop(content.getId())
            elif self.checkTime(content, currentTime):
                content.draw()

    def checkTime(self, content, currentTime):
        return (self.startTime + content.getInterval()) > currentTime
