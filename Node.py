import math

class Node:
    def __init__(self, wight, x, y):
        self.wight=wight
        self.x = x
        self.y = y
        self.cameFrom = None
        self.g = float("inf")
        self.f = float("inf")

    def getWight(self):
        return self.wight

    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setCameFrom(self, node):
        self.cameFrom = node

    def setG(self, g):
        self.g = g
    def setF(self, f):
        self.f = f
    def getG(self):
        return self.g
    def getF(self):
        return self.f
    def getH(self, goal):
        return math.sqrt((self.getX() - goal.getX())**2 + (self.getY() - goal.getY())**2)

    def __gt__(self, node):
        return self.getF() < node.getF()
    def __eq__(self, node):
        return self.getF() == node.getF()

    def getCoord(self):
        return (self.getX(), self.getY())

    def getPath(self):
        if self.cameFrom is None:
            return [self.getCoord()]
        else:
            return (self.cameFrom.getPath()) + [self.getCoord()]