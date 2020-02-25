from modules.dfsearch import DFSearch
from modules.bfsearch import BFSearch
# from modules.aStarsearch import AStarSearch
from modules.board import Board

import numpy as np

def main():

    ## Get file name
    filename = input('Enter the puzzles filename: ')

    ## Reading input file ##
    with open(filename) as f:
        puzzles = f.readlines()

    ## Setup ##
    for puzzle in puzzles:
        # Boards Setup
        puzzleIndex = puzzles.index(puzzle)
        print("Puzzle #: ", puzzleIndex)
        print(puzzle)

        elements = puzzle.split()
        board_size = int(elements[0])
        max_depth = int(elements[1])
        max_search_length = int(elements[2])
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

        # Get search algorithm from user
        algo = input('What algorithm do you wish to use ? ')

        if (algo=='DFS'):
            # DFS setup
            game = DFSearch(max_depth, puzzleIndex)
        elif (algo == 'BFS'):
            # BFS setup
            game = BFSearch(max_search_length)
        # elif (algo == 'A*'):
            # A* setup
            # game = AStarSearch(max_search_length)
        else:
            print('Algorithm not supported')

        print("Initial Board")
        print(myBoard.getBoard())

        game.run(myBoard)



if __name__ == '__main__':
    main()