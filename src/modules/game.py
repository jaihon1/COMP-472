import numpy as np

from .board import Board

def main():
    print("This is the game")

    rows = 4
    cols = 4

    myBoard = Board(rows)
    myBoard.initializeBoard()

    print(myBoard.initializeBoard())
    print(myBoard.initializeBoardOnes())
    print(myBoard.initializeBoardZeros())

    print(myBoard.verify())

if __name__ == '__main__':
    main()

