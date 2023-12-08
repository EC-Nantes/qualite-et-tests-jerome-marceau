import tictactoe

if __name__ == '__main__':
    board = tictactoe.Board()
    while board.check_win() is False:
        print(board)
        x = input("x: ")
        y = input("y: ")
        board.new_move(y, x)

    print(board)
    print("Le joueur", board.check_win(), "a gagné !")