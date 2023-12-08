import tictactoe

if __name__ == '__main__':
    board = tictactoe.Board()
    while board.check_win() is None:
        print(board)
        x = int(input("x: "))
        y = int(input("y: "))
        board.new_move