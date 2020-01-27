from modules.board import Board


def main():
    print("This is the main function")


    board_size = 3

    # Board Setup
    myBoard = Board(board_size)

    myBoard.initializeBoardRandom()
    myBoard.initializeBoardOnes()
    myBoard.initializeBoardZeros()

    # Run Game
    while True:
        result = myBoard.verify()

        if result:
            print("GOOD WORK!")
            break
        else:
            print("NOT YET..")

        myBoard.draw()

        user_input_i = int(input("Please enter i coordinate (max " + str(board_size - 1) + "):" ))
        user_input_j = int(input("Please enter j coordinate (max " + str(board_size - 1) + "):" ))

        print(user_input_i)
        myBoard.move(user_input_i, user_input_j)





if __name__ == '__main__':
    main()
