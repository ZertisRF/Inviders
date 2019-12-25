class BaseFlyObject:
    def __init__(self, x, y, pygame, gameDisplay, gameParams):
        self.x = x
        self.y = y
        self.pygame = pygame
        self.gameDisplay = gameDisplay
        self.gameParams = gameParams
        self.image = None

    def update(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def event(self, event):
        self.event = event

    def display(self):
        self.gameDisplay.blit(self.image, (self.x, self.y))

    def changeCoord(self, x_c, y_c):
        self.x += x_c
        self.y += y_c

    #def checkDestroy(self):



