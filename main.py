from Node import Node
from AStar import AStar
from MazeGenerator import MazeGenerator


def main():
    x = MazeGenerator(10, 100).createRandom(5, 10)
    x.printMaze()
    y = AStar(x)
    solved = y.solve(x.mat[2][2])
    print(solved)


if __name__ == "__main__":
    main()
