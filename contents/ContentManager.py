from fly_objects.Weapon import weapon_group

class ContentManager:
    def __init__(self):
        self.content = {}

    def getContent(self):
        return self.content

    def setContents(self, contents):
        for content in contents:
            self.content[content.getId()] = content

    def clearContent(self):
        keys = [x for x in self.content.keys()]
        for key in keys:
            if self.content[key].ended():
                self.content.pop(key)

    def checkCrossedContent(self, content, otherContent):
        coords = content.getCoords()
        x = coords[0]
        y = coords[1]
        sh = content.getFlyObject.getSize()[0]
        h = content.getFlyObject.getSize()[1]
        otherCoords = content.getCoords()
        x1 = otherCoords[0]
        y1 = otherCoords[1]
        sh1 = otherContent.getFlyObject.getSize()[0]
        h1 = otherContent.getFlyObject.getSize()[1]
        if x <= x1 and y <= y1:
            if x1 <= x + sh and y1 <= y + h:
                return True
            else:
                return False
        elif x <= x1 and y >= y1:
            if x1 <= x + sh and y1 <= y + h:
                return True
            else:
                return False
        elif x >= x1 and y <= y1:
            if x <= x1 + sh1 and y1 <= y + h:
                return True
            else:
                return False
        elif x >= x1 and y >= y1:
            if x1 <= x + sh1 and y <= y1 + h1:
                return True
            else:
                return False

    def update(self):
        for item in weapon_group:
            #if self.checkCrossedContent(*, *):  что указать в скобках?
                # здесь должна вызываться функция взрыва (Enemy_1.boom()) для врага и добавляться очки игроку

