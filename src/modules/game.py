import numpy as np

from .board import Board

def main():
    print("This is the game")

    rows = 4
    cols = 4

    myBoard = Board(rows)

    print(myBoard.initializeBoardRandom())
    print(myBoard.initializeBoardOnes())
    print(myBoard.initializeBoardZeros())

    print(myBoard.verify())

    myBoard.move(3, 2)

if __name__ == '__main__':
    main()

