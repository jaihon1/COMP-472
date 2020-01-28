
class State():
    def __init__(self, coordinate_i, coordinate_j, boardState, depth):
        self.i = coordinate_i
        self.j = coordinate_j
        self.state = boardState
        self.depth = depth

    def getCoordinateI(self):
        return self.i

    def getCoordinateJ(self):
        return self.j

    def getState(self):
        return self.state

    def getDepth(self):
        return self.depth

def main():
    print("State class")

if __name__ == '__main__':
    main()