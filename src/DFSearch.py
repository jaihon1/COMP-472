import numpy as np
from modules.board import Board
from modules.move import Move

class DFSearch():
    def __init__(self):
        self.openList = [] # A stack
        self.closeList = [] # A queue

    def pushOpenList(self, value):
        self.openList.append(value)

    def popOpenList(self):
        return self.openList.pop()

    def addCloseList(self, value):
        self.closeList.append(value)

    def removeCloseList(self, value):
        return self.closeList.pop(0)

    def getOpenList(self):
        return self.openList

    def getCloseList(self):
        return self.closeList


def main():

    board_size = 3

    # Board Setup
    myBoard = Board(board_size)

    myBoard.initializeBoardRandom()
    myBoard.initializeBoardOnes()
    myBoard.initializeBoardZeros()

    # DFS setup
    dfs = DFSearch()

    # Initial state
    move = Move(None, None, myBoard.getBoard)
    dfs.pushOpenList(move)

    # Run Game
    while dfs.getOpenList():

        # node = dfs.popOpenList()

        # result = myBoard.verify()

        # if result:
        #     print("GOOD WORK!")
        #     break
        # else:

        #     dfs.addCloseList(node)

        # # myBoard.draw()

        # # user_input_i = int(input("Please enter i coordinate (max " + str(board_size - 1) + "):" ))
        # # user_input_j = int(input("Please enter j coordinate (max " + str(board_size - 1) + "):" ))

        # # print(user_input_i)
        # # myBoard.move(user_input_i, user_input_j)





if __name__ == '__main__':
    main()
