import numpy as np

TOGGLE_HEURISTIC_1 = True
TOGGLE_HEURISTIC_2 = False

class State():
    def __init__(self, coordinate_i, coordinate_j, boardState, depth, previousState):
        self.i = coordinate_i
        self.j = coordinate_j
        self.boardState = boardState
        self.depth = depth
        self.previousState = previousState
        self.cost = self.getCost()
        self.totalCost = depth + self.getCost()

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
            10: 'K',
            11: '',
        }
        return switcher.get(numericalCoordinate)

    def getCoordinateI(self):
        return self.i

    def getCoordinateJ(self):
        return self.j

    def getBoardState(self):
        return self.boardState

    def getBoardStateToPrint(self):
        integerArray = self.boardState.flatten().astype(int)
        output = '\t'
        output += ' '.join(map(str, integerArray))
        return output

    def getDepth(self):
        return self.depth

    def getPreviousState(self):
        return self.previousState

    def setPreviousState(self, state):
        self.previousState = state

    def getTotalCost(self):
        return self.totalCost

    def getCost(self):
        if TOGGLE_HEURISTIC_1:
            cost = 0
            # Counting number of 1's in the current state
            for i in self.getBoardState().flatten().tolist():
                if (i == 1):
                    cost = cost + 1
            return cost

        if TOGGLE_HEURISTIC_2:
            if self.previousState:
                cost = self.boardState.size

                # Get matrix difference between parent and child matrices
                changes = np.subtract(self.boardState, self.previousState.getBoardState())

                #Give score
                for i in changes.flatten().tolist():
                    # Give negative reward: It was updated from 0 -> 1
                    if (i == 1):
                        cost = cost + 2
                    # Give positive reward: It was updated from 1 -> 0
                    if (i == -1):
                        cost = cost - 1

                return cost
            else:
                return 0


def main():
    print("State class")

if __name__ == '__main__':
    main()
