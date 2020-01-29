from .board import Board

class Play():
    def __init__(self, size):
        self.size = size
        self.board = None

    def setup(self):
        # Board Setup
        self.board = Board(self.size)

        self.board.initializeBoardRandom()
        self.board.initializeBoardOnes()
        self.board.initializeBoardZeros()

    def run(self):
        while True:
            result = self.board.verify()

            if result:
                print("GOOD WORK!")
                break
            else:
                print("NOT YET..")

                self.board.draw()

                try:
                    user_input_i = int(input("Please enter i coordinate (max " + str(self.size - 1) + "):" ))
                    user_input_j = int(input("Please enter j coordinate (max " + str(self.size - 1) + "):" ))
                    self.board.move(user_input_i, user_input_j)
                except ValueError:
                    print("Invalid input!")
                    continue


def main():
    print("Play class")

if __name__ == '__main__':
    main()