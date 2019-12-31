'''
Здесь храниться информация о параметрах игры
'''
class GameParams:
    def __init__(self):
        self.wight = None
        self.height = None
        self.colour_black = (0, 0, 0)
        self.colour_white = (255, 255, 255)
        self.colour_red = (255, 0, 0)

    def getWight(self):
        return self.wight

    def setWight(self, wight):
        self.wight = wight

    def getHeight(self):
        return self.height

    def setHeight(self, height):
        self.height = height
