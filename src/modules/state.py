
class State():
    def __init__(self, coordinate_i, coordinate_j, boardState, depth, previousState):
        self.i = coordinate_i
        self.j = coordinate_j
        self.boardState = boardState
        self.depth = depth
        self.previousState = previousState

    def getCoordinateI(self):
        return self.i

    def getCoordinateJ(self):
        return self.j

    def getBoardState(self):
        return self.boardState

    def getDepth(self):
        return self.depth

    def getPreviousState(self):
        return self.previousState

    def setPreviousState(self, state):
        self.previousState = state


def main():
    print("State class")

if __name__ == '__main__':
    main()