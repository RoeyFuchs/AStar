import random
from Node import Node
from Maze import Maze


class MazeGenerator:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        pass
    def createRandom(self, rows, columns):
        mat = [[0 for x in range(columns)] for y in range(rows)]
        for r in range(rows):
            for c in range(columns):
                mat[r][c] = Node(random.randint(self.min, self.max))
        return Maze(mat)