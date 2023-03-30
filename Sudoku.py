import random


class SudokuBoard: 
    def __init__(self, size: int):
        self.root = int(size ** 0.5)
        if self.root != size ** 0.5:
            raise ValueError("Size must be a square")
        self.size = size
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.filledTiles = 0
        self.solved = False
    
    def __str__(self):
        for i in range(self.size):
            print(self.board[i])
    
    def generateSolvableBoard(self):
        for i in range(self.size):
            for j in range(self.size):
                self.filledTiles += 1
                self.board[i][j] = (i + j) % self.size + 1
        while self.filledTiles > self.size:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.board[row][col] != 0:
                self.board[row][col] = 0
                self.filledTiles -= 1

    
    def setVal(self, row: int, col: int, val: int):
        self.board[row][col] = val
        if val == 0:
            self.filledTiles -= 1
        else: 
            self.filledTiles += 1
    
    def validatePosition(self, row: int, col:int, val:int):
        for i in range(self.size):
            if self.board[row][i] == val:
                return False
        for i in range(self.size):
            if self.board[i][col] == val:
                return False
        boxRow = row - row % self.root
        boxCol = col - col % self.root
        for i in range(self.root):
            for j in range(self.root):
                if self.board[boxRow + i][boxCol + j] == val:
                    return False
        return True

    def solve(self, row: int, col: int):
        if (row == self.size - 1 and col == self.size):
            return True
        if col == self.size:
            row += 1
            col = 0
        if self.board[row][col] > 0:
            return self.solve(row, col + 1)
        for num in range(1, self.size + 1, 1): 
            if self.validatePosition(row, col, num):
                self.setVal(row, col, num)
                if self.solve(row, col + 1):
                    return True
            self.setVal(row, col, 0)
        return False

board = SudokuBoard(9)
board.generateSolvableBoard()
board.__str__()
print(board.solve(0,0))
print()
print()
board.__str__()

