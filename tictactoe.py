class Board:

    def __init__(self):
        self.grid = [[' ' for _ in range(3)] for _ in range(3)]
        self.turn = 1
        self.symbols = ['x', 'o']

    def new_move(self, x, y):
        if self.grid[x][y] == ' ':
            self.grid[x][y] = self.symbols[self.turn]
            self.turn = 1 - self.turn
        else:
            print("case déjà occupé")

    def check_win(self):

        # Check line
        for i in range(3):
            counter_x = 0
            counter_o = 0
            for k in range(3):
                if self.grid[i][k] == 'x':
                    counter_x += 1
                elif self.grid[i][k] == 'o':
                    counter_o += 1
            if counter_x == 3:
                return 'x'
            elif counter_o == 3:
                return 'o'
            
        # Check column
        for i in range(3):
            counter_x = 0
            counter_o = 0
            for k in range(3):
                if self.grid[k][i] == 'x':
                    counter_x += 1
                elif self.grid[k][i] == 'o':
                    counter_o += 1
            if counter_x == 3:
                return 'x'
            elif counter_o == 3:
                return 'o'
            
        # Check first diagonal
        for i, j in zip(range(3), range(3)):
            if self.grid[i][j] == 'x':
                counter_x += 1
            elif self.grid[i][j] == 'o':
                counter_o += 1
        if counter_x == 3:
            return 'x'
        elif counter_o == 3:
            return 'o'
            
        # Check second diagonal
        for i, j in zip(range(3), range(2, -1, -1)):
            if self.grid[i][j] == 'x':
                counter_x += 1
            elif self.grid[i][j] == 'o':
                counter_o += 1
        if counter_x == 3:
            return 'x'
        elif counter_o == 3:
            return 'o'
        
    def __str__(self):
        res = ""
        for line in self.grid:
            res += f'{line[0]} {line[1]} {line[2]}' + '\n'
        return res