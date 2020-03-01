
class State():
    def __init__(self, coordinate_i, coordinate_j, boardState, depth, previousState, algorithm):
        self.i = coordinate_i
        self.j = coordinate_j
        self.boardState = boardState
        self.depth = depth
        self.previousState = previousState
        self.algorithm = algorithm
        self.cost = self.getCost()
        self.gCost = 0
        self.hCost = 0

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
            11: ' ',
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

    def getCost(self):
        if (self.algorithm == 'BFS'):
            cost = 0
            for i in self.getBoardState().flatten().tolist():
                if (i == 1):
                    cost = cost + 1
            return cost
        else:
            # f(n) = g(n) + h(n)
            # g(n):
            gCost = self.depth
            # h(n): number of 1s on the board
            hCost = 0
            for i in self.getBoardState().flatten().tolist():
                if (i == 1):
                    hCost = hCost + 1
            cost = gCost + hCost
            self.gCost = gCost
            self.hCost = hCost
            return cost
    
    def getFCost(self):
        print('g(n):', self.gCost)
        print('h(n):', self.hCost)

def main():
    print("State class")

if __name__ == '__main__':
    main()