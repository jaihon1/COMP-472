from modules.dfsearch import DFSearch
from modules.board import Board

def main():
    board_size = 3
    max_depth = 3

    # Board Setup
    myBoard = Board(board_size)

    myBoard.initializeBoardRandom()
    myBoard.initializeBoardOnes()
    myBoard.initializeBoardZeros()

    # DFS setup
    dfs = DFSearch(max_depth)

    print("Initial Board")
    print(myBoard.getBoard())

    dfs.run(myBoard)


if __name__ == '__main__':
    main()