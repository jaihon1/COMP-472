import numpy as np
import time
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

        while not (currentState.getPreviousState() == None):
            currentState = currentState.getPreviousState()
            self.solutionPath.append(currentState)

        return self.solutionPath

    def outputNoSolution(self):
        with open(str(self.puzzleIndex) + '_dfs_solution.txt', 'a') as f:
            print("NO SOLUTION!", file=f)

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
                    state = State(i, j, newBoardState, depth, tempCurrentState)
                    childs.append(state)

        return childs

    def run(self, board):
        # Initial state
        initial_state = State(None, None, board.getBoard(), 0, None)
        self.pushOpenList(initial_state)

        # Initiate Timer
        start_time = time.time()

        # Run Game
        print("Initiating DFS!!")
        while self.getOpenList():
            current_state = self.popOpenList()
            board.setBoard(current_state.getBoardState())

            self.addCloseList(current_state)

            result = board.verify()

            if result:
                print("GOOD WORK!", "Waiting to finish output files...")
                print("--- Duration of DFS: %s seconds ---" % (time.time() - start_time))
                self.getSolution(current_state)
                self.outputSolution()
                self.outuptSearch()
                print("--- Duration of Output to file: %s seconds ---" % (time.time() - start_time))
                print("Nodes visited: ", len(self.closeList))
                print("End.")
                break
            else:
                childs = self.getChilds(board, current_state)
                for child in childs:
                    exist = False

                    # # Check in close list
                    # for move in self.getCloseList():
                    #     resultState = np.array_equal(child.getBoardState(), move.getBoardState())
                    #     # result_i = child.getCoordinateI() == move.getCoordinateI()
                    #     # result_j = child.getCoordinateJ() == move.getCoordinateJ()

                    #     # if resultState and result_i and result_j:
                    #     if resultState:
                    #         exist = True
                    #         break

                    # if not exist:
                    #     # Check in open list
                    #     for move in self.getOpenList():
                    #         resultState = np.array_equal(child.getBoardState(), move.getBoardState())
                    #         # result_i = child.getCoordinateI() == move.getCoordinateI()
                    #         # result_j = child.getCoordinateJ() == move.getCoordinateJ()

                    #         # if resultState and result_i and result_j:
                    #         if resultState:
                    #                 exist = True
                    #                 break

                    if not exist:
                        if child.getDepth() <= self.maxDepth:
                            self.pushOpenList(child)

        if not self.getOpenList():
            print("NO SOLUTIOON!", "Waiting to finish output files...")
            self.outputNoSolution()
            print("Nodes visited: ", len(self.closeList))
            print("End.")








def main():
    print("This is DFS.")





if __name__ == '__main__':
    main()
