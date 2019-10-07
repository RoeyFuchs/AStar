import numpy

class Maze:
    def __init__(self, matrix):
        self.mat = matrix
        self.rows = len(self.mat)
        self.coulmns = len(self.mat[0])
        print("HEY")

    def getStart(self):
        return self.mat[0][0]


    def getNeighbor(self, node):
        neighbors = []
        x = self.index_2d(self.mat, node)
        if x[0] > 0:
            neighbors.append(self.mat[x[0]-1][x[1]])
        if x[0] < self.rows:
            neighbors.append(self.mat[x[0]+1][x[1]])
        if x[1] > 0:
            neighbors.append(self.mat[x[0]][x[1]-1])
        if x[1] < self.coulmns:
            neighbors.append(self.mat[x[0]][x[1]+1])
        return neighbors


    def index_2d(self, data, search):
        for i, e in enumerate(data):
            try:
                return i, e.index(search)
            except ValueError:
                pass
        raise ValueError("{} is not in list".format(repr(search)))

