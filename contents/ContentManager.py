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
        otherCoords = content.getCoords()
        if coords != None and otherCoords != None:
            x = coords[0]
            y = coords[1]
            sh = content.getFlyObject().getSize()[0]
            h = content.getFlyObject().getSize()[1]
            otherCoords = content.getCoords()
            x1 = otherCoords[0]
            y1 = otherCoords[1]
            sh1 = otherContent.getFlyObject().getSize()[0]
            h1 = otherContent.getFlyObject().getSize()[1]
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
        else:
            return False


    def analize(self):
        contents = [x for x in self.getContent().values()]
        for i in range(len(contents) - 1):
            for j in range(i + 1, len(contents)):
                if self.checkCondition(contents[i], contents[j]):
                    crossed = self.checkCrossedContent(contents[i], contents[j])
                    if crossed:
                        contents[i].getFlyObject().crashAction(contents[j].getFlyObject().getCrashStranges())
                        contents[j].getFlyObject().crashAction(contents[i].getFlyObject().getCrashStranges())


    def update(self):
        pass
        #for item in weapon_group:
            #if self.checkCrossedContent(*, *):  что указать в скобках?
                # здесь должна вызываться функция взрыва (Enemy_1.boom()) для врага и добавляться очки игроку

    def checkCondition(self, cont_1, cont_2):
        return cont_1.notEnded() and cont_2.notEnded() \
               and cont_1.getFlyObject().getType() != cont_2.getFlyObject().getType()
