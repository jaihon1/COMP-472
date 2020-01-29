from modules.play import Play

def main():
    print("This is the main function")

    board_size = 3

    play = Play(board_size)
    play.setup()
    play.run()

if __name__ == '__main__':
    main()