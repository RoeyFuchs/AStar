import queue as Q


class AStar:
    def __init__(self, maze):
        self.maze = maze
        self.closedSet = []
        self.openset = Q.PriorityQueue()
        startingPoint = maze.getStart()
        self.openset.put(startingPoint)
        startingPoint.setG(0)

    def solve(self, goal):
        self.maze.getStart().setF(self.maze.getStart().getH(goal))
        while self.openset.qsize() != 0:
            current = self.openset.get()
            if current == goal:
                return current.getPath()
            self.closedSet.append(current)
            x = self.maze.getNeighbor(current)
            for neighbr in x:
                if neighbr in self.closedSet:
                    continue
                tentative_gScore = current.getG() + neighbr.getWight()
                if tentative_gScore < neighbr.getG():
                    neighbr.setCameFrom(current)
                    neighbr.setG(tentative_gScore)
                    neighbr.setF(neighbr.getG() + neighbr.getH(goal))
                    if neighbr not in self.openset.queue:
                        self.openset.put(neighbr)

        return None



