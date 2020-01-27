import numpy as np

from .board import Board

def main():

    rows = 4
    cols = 4

    myBoard = Board(rows)

    myBoard.initializeBoardRandom()
    myBoard.initializeBoardOnes()
    myBoard.initializeBoardZeros()

    myBoard.draw();
    print(myBoard.verify())

    myBoard.move(1, 1)
    myBoard.draw()
    print(myBoard.verify())

    myBoard.move(1, 1)
    myBoard.draw()
    print(myBoard.verify())


if __name__ == '__main__':
    main()

