class Board:

    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 1
        self.symbols = ['x', 'o']

    def new_move(self, x, y):
        if x in ['0', '1', '2'] and y in ['0', '1', '2']:
            x = int(x)
            y = int(y)
        else:
            print("Veuillez entrer des coordonnées valides")
            return
        if self.grid[x][y] == ' ':
            self.grid[x][y] = self.symbols[self.turn]
            self.turn = 1 - self.turn
        else:
            print("case déjà occupé")

    def check_win(self):

        # Check line
        for i in range(3):
            if self.checkLine(i):
                return self.checkLine(i)

        # Check column
        for i in range(3):
            if self.checkColumn(i):
                return self.checkColumn(i)
        
        # Check diagonal
        for i in range(2):
            if self.checkDiagonal(i):
                return self.checkDiagonal(i)
        
        return False
    
    def checkLine(self, line):
        if self.grid[line][0] == self.grid[line][1] == self.grid[line][2]:
            return self.grid[line][0]
        return False

    def checkColumn(self, column):
        if self.grid[0][column] == self.grid[1][column] == self.grid[2][column]:
            return self.grid[0][column]
        return False
    
    def checkDiagonal(self, diagonal):
        if diagonal == 0:
            if self.grid[0][0] == self.grid[1][1] == self.grid[2][2]:
                return self.grid[0][0]
        else:
            if self.grid[0][2] == self.grid[1][1] == self.grid[2][0]:
                return self.grid[0][2]
        return False

    def __str__(self):
        res = ""
        for line in self.grid:
            res += f'{line[0]} | {line[1]} | {line[2]}' + '\n'
            res += '----------' + '\n'
        return res[:-11]