class Board:

    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 1
        self.symbols = ['x', 'o']

    def new_move(self, x, y):
        if self.grid[x][y] == ' ':
            self.grid[x][y] = self.symbols[self.turn]
            self.turn = 1 - self.turn
            return True
        else:
            print("case déjà occupé")
            return False

    def check_win(self):

        # Check line
        for i in range(3):
            if self.check_line(i):
                return self.check_line(i)

        # Check column
        for i in range(3):
            if self.check_column(i):
                return self.check_column(i)
        
        # Check diagonal
        for i in range(2):
            if self.check_diagonal(i):
                return self.check_diagonal(i)
        
        return False
    
    def check_line(self, line):
        if self.grid[line][0] == self.grid[line][1] == self.grid[line][2] and self.grid[line][0] != ' ':
            return self.grid[line][0]
        return False

    def check_column(self, column):
        if self.grid[0][column] == self.grid[1][column] == self.grid[2][column] and self.grid[0][column] != ' ':
            return self.grid[0][column]
        return False
    
    def check_diagonal(self, diagonal):
        if diagonal == 0:
            if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] != ' ':
                return self.grid[0][0]
        else:
            if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] != ' ':
                return self.grid[0][2]
        return False

    def __str__(self):
        res = ""
        for line in self.grid:
            res += f'{line[0]} | {line[1]} | {line[2]}' + '\n'
            res += '----------' + '\n'
        return res[:-11]