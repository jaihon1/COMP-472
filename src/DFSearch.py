import numpy as np
from modules.board import Board
from modules.state import State

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

    def getChilds(self, board, currentState):
        childs = []

        for i in range(board.getRows()):
            for j in range(board.getCols()):
                # Don't get the child that did the same move as you
                if not (i == currentState.getCoordinateI() and j == currentState.getCoordinateJ()):
                    temp = board.getBoard()
                    oldBoardState = temp.copy()

                    board.move(i, j)
                    newBoardState = board.getBoard()
                    board.setBoard(oldBoardState)

                    depth = currentState.getDepth() + 1

                    # print(oldBoardState)
                    # print(i, j)
                    # print(newBoardState)
                    # print("------------")

                    state = State(i, j, newBoardState, depth)
                    childs.append(state)

        return childs



def main():

    board_size = 3
    max_depth = 3

    # Board Setup
    myBoard = Board(board_size)

    myBoard.initializeBoardRandom()
    myBoard.initializeBoardOnes()
    myBoard.initializeBoardZeros()

    # DFS setup
    dfs = DFSearch()

    print("Initial Board")
    print(myBoard.getBoard())

    # Initial state
    initial_state = State(None, None, myBoard.getBoard(), 0)
    dfs.pushOpenList(initial_state)

    # Run Game
    while dfs.getOpenList():

        print("Open Size:", len(dfs.getOpenList()))
        print("Close Size:", len(dfs.getCloseList()))

        current_state = dfs.popOpenList()
        myBoard.setBoard(current_state.getState())

        result = myBoard.verify()

        if result:
            print("GOOD WORK!")
            break
        else:
            childs = dfs.getChilds(myBoard, current_state)
            for child in childs:
                exist = False

                # # Check in close list
                # for move in dfs.getCloseList():
                #     resultState = np.array_equal(child.getState(), move.getState())
                #     # result_i = child.getCoordinateI() == move.getCoordinateI()
                #     # result_j = child.getCoordinateJ() == move.getCoordinateJ()

                #     # if resultState and result_i and result_j:
                #     if resultState:
                #         exist = True
                #         break

                # if not exist:
                #     # Check in open list
                #     for move in dfs.getOpenList():
                #         resultState = np.array_equal(child.getState(), move.getState())
                #         # result_i = child.getCoordinateI() == move.getCoordinateI()
                #         # result_j = child.getCoordinateJ() == move.getCoordinateJ()

                #         # if resultState and result_i and result_j:
                #         if resultState:
                #                 exist = True
                #                 break

                if not exist:
                    if child.getDepth() <= max_depth:
                        dfs.pushOpenList(child)


            dfs.addCloseList(current_state)



if __name__ == '__main__':
    main()
