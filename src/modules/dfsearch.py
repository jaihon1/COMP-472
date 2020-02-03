import numpy as np
from copy import deepcopy
from .state import State

class DFSearch():
    def __init__(self, maxDepth, puzzleIndex):
        self.openList = [] # A stack
        self.closeList = [] # A queue
        self.maxDepth = maxDepth
        self.solutionPath = []
        self.puzzleIndex = puzzleIndex

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

    def getSolution(self, state):
        currentState = state
        self.solutionPath.append(currentState)
        # print(currentState.getCoordinateI(), currentState.getCoordinateJ())
        # print(currentState.getBoardState())
        # print("------------")

        while not (currentState.getPreviousState() == None):

                currentState = currentState.getPreviousState()
                self.solutionPath.append(currentState)

                # print(currentState.getCoordinateI(), currentState.getCoordinateJ())
                # print(currentState.getBoardState())
                # print("------------")


        return self.solutionPath

    def outputSolution(self):
        with open(str(self.puzzleIndex) + '_dfs_solution.txt', 'a') as f:
            for state in reversed(self.solutionPath):
                print(state.getCoordinateI(), state.getCoordinateJ(), state.getBoardState().flatten(), file=f)

    def outuptSearch(self):
        with open(str(self.puzzleIndex) + '_dfs_search.txt', 'a') as f:
            for state in self.closeList:
                print(state.getCoordinateI(), state.getCoordinateJ(), state.getBoardState().flatten(), file=f)


    def getChilds(self, board, currentState):
        childs = []
        tempCurrentState = deepcopy(currentState)
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

                    # print(tempCurrentState.getBoardState())
                    # print(i, j)
                    # print(newBoardState)
                    # print("------------")

                    state = State(i, j, newBoardState, depth, tempCurrentState)
                    childs.append(state)

        return childs

    def run(self, board):
        # Initial state
        initial_state = State(None, None, board.getBoard(), 0, None)
        self.pushOpenList(initial_state)

        # Run Game
        while self.getOpenList():

            # print("Open Size:", len(self.getOpenList()))
            # print("Close Size:", len(self.getCloseList()))

            current_state = self.popOpenList()
            board.setBoard(current_state.getBoardState())

            self.addCloseList(current_state)

            result = board.verify()

            if result:
                print("GOOD WORK!")
                # self.addCloseList(current_state)
                self.getSolution(current_state)
                self.outputSolution()
                self.outuptSearch()
                break
            else:
                childs = self.getChilds(board, current_state)
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
                        if child.getDepth() <= self.maxDepth:
                            self.pushOpenList(child)








def main():
    print("This is DFS.")





if __name__ == '__main__':
    main()
