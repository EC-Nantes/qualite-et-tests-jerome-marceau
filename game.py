import tictactoe

if __name__ == '__main__':
    board = tictactoe.Board()
    while board.check_win() is False:
        print(board)
        x = input("x: ")
        y = input("y: ")
        while not (x in ['0', '1', '2'] and y in ['0', '1', '2']):
            print("Veuillez entrer des coordonnées valides")
            x = input("x: ")
            y = input("y: ")
        x = int(x)
        y = int(y)
        board.new_move(y, x)

    print(board)
    print("Le joueur", board.check_win(), "a gagné !")