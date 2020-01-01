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
            self.contents[content.getId()] = content


    def draw(self, currentTime):
        for content in self.contents.values():
            if not content.ended() and self.checkTime(content, currentTime):
                content.draw()

    def clearContent(self):
        keys = [x for x in self.contents.keys()]
        for key in keys:
            if self.contents[key].ended():
                self.contents.pop(key)


    def checkTime(self, content, currentTime):
        checkTime = currentTime - self.startTime >= content.getInterval()
        return checkTime
