import numpy as np
import time
from copy import deepcopy
from .state import State

TOGGLE_REMOVE_PREVIOUS_MOVE = False
TOGGLE_ORDER_CHILDREN = True

class AStarSearch():
    def __init__(self, maxSearchLength, puzzleIndex):
        self.openList = [] # A priority queue, sorted in ascending order, ie: next is the lowest f(n)
        self.closeList = [] # A stack
        self.maxSearchLength = maxSearchLength
        self.solutionPath = []
        self.puzzleIndex = puzzleIndex

    # push to the end of the open list
    def pushOpenList(self, value):
        self.openList.append(value)
        self.openList = sorted(self.openList, key=lambda x: x.totalCost, reverse=True)

    # return next node to be accessed
    def popOpenList(self):
        return self.openList.pop()

    # add to the end of the closed list
    def addCloseList(self, value):
        self.closeList.append(value)

    # get latest accessed node
    def removeCloseList(self, value):
        return self.closeList.pop()

    # return the current open list
    def getOpenList(self):
        return self.openList

    # return the current closed list
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
        with open(str(self.puzzleIndex) + '_astar_solution.txt', 'a') as f:
            print("NO SOLUTION!", file=f)

    def outputSolution(self):
        with open(str(self.puzzleIndex) + '_astar_solution.txt', 'a') as f:
            for state in reversed(self.solutionPath):
                print(str(state.getAlphabeticalCoordinateI()) + str(state.getCoordinateJ()), ''.join(map(str, state.getBoardState().flatten().astype(int))), file=f)

    def outuptSearch(self):
        with open(str(self.puzzleIndex) + '_astar_search.txt', 'a') as f:
            for state in self.closeList:
                # f(n), g(n), h(n)
                print(str(state.getTotalCost()) + ' ' + str(state.getDepth()) + ' ' + str(state.getCost()), ''.join(map(str, state.getBoardState().flatten().astype(int))), file=f)

    def reorderChildren(self, children):
        flattenedChildren = []
        sortedKeys = []
        reorderedChildren = []

        dictionary = {}
        for child in children:
            flattenedChildren.append(child.getBoardState().flatten())

        # iterating through flattened children:
        length = len(flattenedChildren)
        for i in range(length):
            # convert numpy array to list so that we can use "index()":
            arrayToList = flattenedChildren[i].tolist()

            if(0 in arrayToList):
                # index of first 0:
                index = arrayToList.index(0)
                # store index of first 0 in dictionary:
                dictionary[i] = index
            else:
            # if 0 is not in list, store arbitrary number bigger than any index
            # when sorting, boards w/o 1 won't be discarded and 100 will be sorted after the 1s
                dictionary[i] = 100

        # sort by dictionary by value and reverse it because of the logic in the push open list
        tupleList = sorted(dictionary.items(), key=lambda x: (x[1],x[0]), reverse=True)

        # converting list of tuples to dictionary:
        sortedDictionary = dict(tupleList)

        # taking keys of sortedDictionary:
        for key in sortedDictionary:
            sortedKeys.append(key)

        # reorder children:
        for key in sortedKeys:
            reorderedChildren.append(children[key])

        return reorderedChildren

    def getChildren(self, board, currentState):
        children = []
        # tempCurrentState = deepcopy(currentState)
        tempCurrentState = currentState
        for i in range(board.getRows()):
            for j in range(board.getCols()):
                # Don't include previous move Mode
                if TOGGLE_REMOVE_PREVIOUS_MOVE:
                    if not (i == currentState.getCoordinateI() and j == currentState.getCoordinateJ()):
                        temp = board.getBoard()
                        oldBoardState = temp.copy()

                        board.move(i, j)

                        newBoardState = board.getBoard()
                        board.setBoard(oldBoardState)

                        depth = currentState.getDepth() + 1
                        state = State(i, j, newBoardState, depth, tempCurrentState)

                        children.append(state)
                # Normal Mode
                else:
                    temp = board.getBoard()
                    oldBoardState = temp.copy()

                    board.move(i, j)

                    newBoardState = board.getBoard()
                    board.setBoard(oldBoardState)

                    depth = currentState.getDepth() + 1
                    state = State(i, j, deepcopy(newBoardState), depth, tempCurrentState)

                    children.append(state)

        if TOGGLE_ORDER_CHILDREN:
            reorderedChildren = self.reorderChildren(children)
            return reorderedChildren
        else:
            return children


    def run(self, board):
        print('Running astar')
        # Initial state
        initial_state = State(11, 0, deepcopy(board.getBoard()), 0, None)
        self.pushOpenList(initial_state)

        # Initiate Timer
        start_time = time.time()

        # Run Game
        print("Initiating ASTAR!!")
        while self.getOpenList():
            if self.maxSearchLength == len(self.getCloseList()):
                break
            current_state = self.popOpenList()
            board.setBoard(deepcopy(current_state.getBoardState()))
            # self.addCloseList(deepcopy(current_state))
            self.addCloseList(current_state)
            result = board.verify()

            if result:
                print("GOOD WORK!", "Waiting to finish output files...")
                print("--- Duration of ASTAR: %s seconds ---" % (time.time() - start_time))
                self.getSolution(current_state)
                self.outputSolution()
                self.outuptSearch()
                print("--- Duration of Output to file: %s seconds ---" % (time.time() - start_time))
                print("Nodes visited: ", len(self.closeList))
                print("End.")
                break
            else:
                children = self.getChildren(board, current_state)
                for child in children:
                    self.pushOpenList(child)


        if not self.getOpenList() or self.maxSearchLength == len(self.getCloseList()):
            print("NO SOLUTION!", "Waiting to finish output files...")
            print("--- Duration of ASTAR: %s seconds ---" % (time.time() - start_time))
            self.outputNoSolution()
            self.outuptSearch()
            print("--- Duration of Output to file: %s seconds ---" % (time.time() - start_time))
            print("Nodes visited: ", len(self.closeList))
            print("End.")

def main():
    print("This is ASTAR.")



if __name__ == '__main__':
    main()
