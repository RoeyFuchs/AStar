import numpy

class Maze:
    def __init__(self, matrix):
        self.mat = matrix
        self.rows = len(self.mat)
        self.coulmns = len(self.mat[0])

    def getStart(self):
        return self.mat[0][0]


    def getNeighbor(self, node):
        neighbors = []
        if node.getX() > 0:
            neighbors.append(self.mat[node.getX()-1][node.getY()])
        if node.getX() < self.rows-1:
            neighbors.append(self.mat[node.getX()+1][node.getY()])
        if node.getY() > 0:
            neighbors.append(self.mat[node.getX()][node.getY()-1])
        if node.getY() < self.coulmns-1:
            neighbors.append(self.mat[node.getX()][node.getY()+1])
        return neighbors

    def printMaze(self):
        for r in range(self.rows):
            for c in range(self.coulmns):
                print(str(self.mat[r][c].getWight()) + " | ", end='')
            print()

