from modules.dfsearch import DFSearch
from modules.board import Board

import numpy as np

def main():

    ## Reading input file ##
    with open('test.txt') as f:
        puzzles = f.readlines()

    ## Running DFS on them ##
    for puzzle in puzzles:
        # Game Setup
        puzzleIndex = puzzles.index(puzzle)
        print("Puzzle #: ", puzzleIndex)
        print(puzzle)

        elements = puzzle.split()
        board_size = int(elements[0])
        max_depth = int(elements[1])
        boardValues = list(elements[3])

        counter = 0

        board = np.zeros(shape=(board_size, board_size))
        for i in range(board_size):
            for j in range(board_size):
                board[i][j] = boardValues[counter]
                counter += 1

        # Board Setup
        myBoard = Board(board_size)

        myBoard.setBoard(board)
        myBoard.initializeBoardOnes()
        myBoard.initializeBoardZeros()

        # DFS setup
        dfs = DFSearch(max_depth, puzzleIndex)

        print("Initial Board")
        print(myBoard.getBoard())

        dfs.run(myBoard)






if __name__ == '__main__':
    main()