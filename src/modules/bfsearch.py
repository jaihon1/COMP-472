import numpy as np
from copy import deepcopy
from .state import State


class BFSearch():
    def __init__(self, maxSearchLength, puzzleIndex):
        self.openList = [] # A stack
        self.closeList = [] # A queue
        self.maxSearchLength = maxSearchLength
        self.solutionPath = []
        self.puzzleIndex = puzzleIndex

    def run(self, board):
        print('running bfsearch')

def main():
    print("This is BFS.")





if __name__ == '__main__':
    main()
