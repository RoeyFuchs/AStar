from Node import Node
from AStar import AStar
from MazeGenerator import MazeGenerator


def main():
    print("Hello World!")
    x = MazeGenerator(1, 100).createRandom(5, 10)
    y = AStar(x)
    y.solve(x.mat[3][3])


if __name__ == "__main__":
    main()
