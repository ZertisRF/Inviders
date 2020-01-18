from GameParams import GameParams
gameParams = GameParams()


class ContentManager:
    def __init__(self):
        self.content = {}

    def getContent(self):
        return self.content

    def setContents(self, contents):
        for content in contents:
            self.content[content.getId()] = content
            self.content[content.getId()].counter = 0

    def clearContent(self):
        keys = [x for x in self.content.keys()]
        for key in keys:
            if self.content[key].ended():
                self.content.pop(key)

    def checkCrossedContent(self, content, otherContent):
        coords = content.getCoords()
        otherCoords = otherContent.getCoords()
        if coords != None and otherCoords != None:
            x, y = coords
            sh, h = content.getFlyObject().getSize()
            x1, y1 = otherCoords
            sh1, h1 = otherContent.getFlyObject().getSize()
            ax1, ay1, ax2, ay2 = [ int(i) for i in [x, y, sh, h]]
            ax2 = ax1 + ax2
            ay2 = ay1 + ay2
            bx1, by1, bx2, by2 = [ int(i) for i in [x1, y1, sh1, h1]]
            bx2 = bx1 + bx2
            by2 = by1 + by2
            s1 = ( ax1>=bx1 and ax1<=bx2 ) or ( ax2>=bx1 and ax2<=bx2 )
            s2 = ( ay1>=by1 and ay1<=by2 ) or ( ay2>=by1 and ay2<=by2 )
            s3 = ( bx1>=ax1 and bx1<=ax2 ) or ( bx2>=ax1 and bx2<=ax2 )
            s4 = ( by1>=ay1 and by1<=ay2 ) or ( by2>=ay1 and by2<=ay2 )
            if ((s1 and s2) or (s3 and s4)) or ((s1 and s4) or (s3 and s2)):
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
                        gameParams.count += 100
        gameParams.count_enemies += 1

    def checkCondition(self, cont_1, cont_2):
        return cont_1.notEnded() and cont_2.notEnded() \
               and cont_1.getFlyObject().getType() != cont_2.getFlyObject().getType()
