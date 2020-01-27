import numpy as np

# --Description--
# NxN Board
# Initial state is random
# Winning -> all white (ones)

class Board():
    def __init__(self, size):
        self.rows = size
        self.cols = size
        self.board = None
        self.boardZeros = None
        self.boardOnes = None

    def getRows(self):
        return self.rows

    def getCols(self):
        return self.cols

    def getBoard(self):
        return self.board

    def setBoard(self, board):
        self.board = board

    def initializeBoardRandom(self):
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

    def move(self, i, j):
        if i > (self.rows - 1) or i < 0 or j > (self.cols - 1) or j < 0:
            # Illegal move
            print("Illegal move.")
        else:
            # Legal move
            print("Legal move.")
            # Corners
            if i == 0 and j == 0:
                print("Top left")
            elif i == 0 and j == (self.cols - 1):
                print("Top right")
            elif i == (self.rows - 1) and j == 0:
                print("Botton left")
            elif i == (self.rows - 1) and j == (self.cols - 1):
                print("Botton right")
            else:
                print("Not corner")
                if i == 0:
                    print("Top row")
                elif i == (self.rows - 1):
                    print("Bottom row")
                elif j == 0:
                    print("Left col")
                elif j == (self.cols - 1):
                    print("Right col")
                else:
                    print("Inside")



def main():
    print("Board class")

if __name__ == '__main__':
    main()