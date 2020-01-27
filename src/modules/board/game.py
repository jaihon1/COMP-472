import numpy as np

def initializeBoard(rows, cols):
    board = np.random.randint(10, size=(rows, cols))

    return board

def initializeBoardZeros(rows, cols):
    board = np.zeros(shape=(rows, cols))

    return board

def initializeBoardOnes(rows, cols):
    board = np.ones(shape=(rows, cols))

    return board

def main():

    rows = 4
    cols = 4

    board = initializeBoardOnes(rows, cols)

    print(board)


if __name__ == '__main__':
    main()

