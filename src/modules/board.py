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

    def getFlatBoard(self):
        return self.board.flatten()

    # def buildBoard(self, board, size):
    #     np.

    def setBoard(self, board):
        self.board = board

    def initializeBoardRandom(self):
        board = np.random.randint(2, size=(self.rows, self.cols))
        self.board = board

    def initializeBoardZeros(self):
        board = np.zeros(shape=(self.rows, self.cols))
        self.boardZeros = board

    def initializeBoardOnes(self):
        board = np.ones(shape=(self.rows, self.cols))
        self.boardOnes = board

    def draw(self):
        print(self.board)

    def verify(self):
        result = np.array_equal(self.board, self.boardZeros)

        return result

    def move(self, i, j):
        if i > (self.rows - 1) or i < 0 or j > (self.cols - 1) or j < 0:
            # Illegal move
            print("Illegal move.")
        else:
            # Legal move
            # print("Legal move.")
            # Corners
            if i == 0 and j == 0:
                # print("Top left")
                self.board[0][0] = (self.board[0][0] + 1) % 2
                self.board[0][1] = (self.board[0][1] + 1) % 2
                self.board[1][0] = (self.board[1][0] + 1) % 2

            elif i == 0 and j == (self.cols - 1):
                # print("Top right")
                self.board[0][self.cols - 1] = (self.board[0][self.cols - 1] + 1) % 2
                self.board[0][self.cols - 2] = (self.board[0][self.cols - 2] + 1) % 2
                self.board[1][self.cols - 1] = (self.board[1][self.cols - 1] + 1) % 2

            elif i == (self.rows - 1) and j == 0:
                # print("Botton left")
                self.board[self.rows - 1][0] = (self.board[self.rows - 1][0] + 1) % 2
                self.board[self.rows - 1][1] = (self.board[self.rows - 1][1] + 1) % 2
                self.board[self.rows - 2][0] = (self.board[self.rows - 2][0] + 1) % 2

            elif i == (self.rows - 1) and j == (self.cols - 1):
                # print("Botton right")
                self.board[self.rows - 1][self.cols - 1] = (self.board[self.rows - 1][self.cols - 1] + 1) % 2
                self.board[self.rows - 1][self.cols - 2] = (self.board[self.rows - 1][self.cols - 2] + 1) % 2
                self.board[self.rows - 2][self.cols - 1] = (self.board[self.rows - 2][self.cols - 1] + 1) % 2

            else:
                # print("Not corner")
                if i == 0:
                    # print("Top row")
                    self.board[i][j] = (self.board[i][j] + 1) % 2
                    self.board[i][j + 1] = (self.board[i][j + 1] + 1) % 2
                    self.board[i][j - 1] = (self.board[i][j - 1] + 1) % 2
                    self.board[i + 1][j] = (self.board[i + 1][j] + 1) % 2

                elif i == (self.rows - 1):
                    # print("Bottom row")
                    self.board[i][j] = (self.board[i][j] + 1) % 2
                    self.board[i][j + 1] = (self.board[i][j + 1] + 1) % 2
                    self.board[i][j - 1] = (self.board[i][j - 1] + 1) % 2
                    self.board[i - 1][j] = (self.board[i - 1][j] + 1) % 2

                elif j == 0:
                    # print("Left col")
                    self.board[i][j] = (self.board[i][j] + 1) % 2
                    self.board[i + 1][j] = (self.board[i + 1][j] + 1) % 2
                    self.board[i - 1][j] = (self.board[i - 1][j] + 1) % 2
                    self.board[i][j + 1] = (self.board[i][j + 1] + 1) % 2

                elif j == (self.cols - 1):
                    # print("Right col")
                    self.board[i][j] = (self.board[i][j] + 1) % 2
                    self.board[i + 1][j] = (self.board[i + 1][j] + 1) % 2
                    self.board[i - 1][j] = (self.board[i - 1][j] + 1) % 2
                    self.board[i][j - 1] = (self.board[i][j - 1] + 1) % 2

                else:
                    # print("Inside")
                    self.board[i][j] = (self.board[i][j] + 1) % 2
                    self.board[i + 1][j] = (self.board[i + 1][j] + 1) % 2
                    self.board[i - 1][j] = (self.board[i - 1][j] + 1) % 2
                    self.board[i][j + 1] = (self.board[i][j + 1] + 1) % 2
                    self.board[i][j - 1] = (self.board[i][j - 1] + 1) % 2



def main():
    print("Board class")

if __name__ == '__main__':
    main()