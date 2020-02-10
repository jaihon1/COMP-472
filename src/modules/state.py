
class State():
    def __init__(self, coordinate_i, coordinate_j, boardState, depth, previousState):
        self.i = coordinate_i
        self.j = coordinate_j
        self.boardState = boardState
        self.depth = depth
        self.previousState = previousState

    def getAlphabeticalCoordinateI(self):
        numericalCoordinate = self.i
        switcher = {
            0: 'A',
            1: 'B',
            2: 'C',
            3: 'D',
            4: 'E',
            5: 'F',
            6: 'G',
            7: 'H',
            8: 'I',
            9: 'J',
            10: 'K'
        }
        return switcher.get(numericalCoordinate, "Invalid coordinate")

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
