import numpy as np

# --Description--
# NxN Board
# Initial state is random
# Winning -> all white (ones)

class Board():
    def __init__(self, shape):
        self.rows = shape
        self.cols = shape
        self.board = None
        self.boardZeros = None
        self.boardOnes = None

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def initializeBoard(self):
        board = np.random.randint(2, size=(self.rows, self.cols))

        self.board = board
        return self.board

    def initializeBoardZeros(self):
        board = np.zeros(shape=(self.rows, self.cols))
        self.boardZeros = board

        return self.boardZeros

    def initializeBoardOnes(self):
        board = np.ones(shape=(self.rows, self.cols))

        self.boardOnes = board
        return self.boardOnes

    def verify(self):
        result = np.array_equal(self.board, self.boardOnes)

        return result


def main():
    print("Board class")

if __name__ == '__main__':
    main()