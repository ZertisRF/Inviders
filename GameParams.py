'''
Здесь хранится информация о параметрах игры
'''
class GameParams:
    def __init__(self):
        self.width = None
        self.height = None
        self.colour_black = (0, 0, 0)
        self.colour_white = (255, 255, 255)
        self.colour_red = (255, 0, 0)

    def getWidth(self):
        return self.width

    def setWidth(self, width):
        self.width = width

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
