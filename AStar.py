import queue as Q


class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.closedSet = []
        self.openset = Q.PriorityQueue()
        self.openset.put(maze.getStart())

    def solve(self, goal):
        while self.openset.qsize() != 0:
            current = self.openset.get()
            if current == goal:
                return
                # we found!
                #TO DO return something
            self.closedSet.append(current)
            x = self.maze.getNeighbor(current)
            for neighbr in x:




