""" Author:  Andrea Minichova (s1021688) 
    Project: Sudoku solver using AC-3 algorithm """


import itertools
import math

from cell import Cell


class Sudoku:
    def __init__(self, filename):
        """ Sudoku initializer """
        self.grid = self.read_sudoku(filename)
        self.subsquares = []
        self.init_neighbors()
    

    def read_sudoku(self, filename):
        """ Reads into grid from a specified file """
        grid = [[0 for i in range(9)] for j in range(9)]
        with open(filename) as f:
            for i in range(9):
                for j in range(9):
                    cell = Cell((int(f.read(1))), list(range(1,10)), [])
                    grid[i][j] = cell
                f.read(1)
        return grid


    def init_neighbors(self):
        """ Initializes neighbors for each cell in grid """
        for i in range(9):
            for j in range(9):
                self.grid[i][j].update_neighbors(self.generate_neighbors(i,j))

    
    def generate_neighbors(self, row, col):
        """ Returns all neighbors of a cell (which constrain it) """
        vertical, horizontal, subsquare, neighbors = [], [], [], []
        for i in range(9):
            for j in range(9):
                if row != i or col != j:
                    vertical.append(self.grid[row][i])
                    horizontal.append(self.grid[j][col])
                subsquare = self.get_subsquare(row, col)
        neighbors = list(set(vertical + horizontal + subsquare))
        return neighbors


    def get_subsquare(self, row, col):
        """ Returns all neighbors inside the same subsquare """
        subsquare = []
        square_row = math.floor(row/3) * 3
        square_col = math.floor(col/3) * 3
        for i in range(square_row, square_row+3):
            for j in range(square_col, square_col+3):
                if square_row != row or square_col != col:
                    subsquare.append(self.grid[i][j])
        return subsquare


    def __str__(self):
        """ Returns string representation of sudoku """
        output = "╔═══════╦═══════╦═══════╗\n"
        for i in range(9):
            if i == 3 or i == 6:
                output += "╠═══════╬═══════╬═══════╣\n"
            output += "║ "
            for j in range(9):
                if j == 3 or j == 6:
                    output += "║ "
                output += ". " if self.grid[i][j].value == 0 else chr(self.grid[i][j].value + ord('0')) + " "
            output += "║\n"
        output += "╚═══════╩═══════╩═══════╝\n"
        return output


    def is_solution(self):
        """ Returns true if sudoku is solved, returns false otherwise """
        for row in self.grid:
            if sum(cell.value for cell in row) != 45:
                return False
        columns = zip(*self.grid)
        for col in columns:
            if sum(cell.value for cell in col) != 45:
                return False
        self.subsquares = self.generate_subsquares()
        for square in self.subsquares:
            if sum(cell.value for cell in square) != 45:
                return False
        print("Solved!")
        return True


    def generate_subsquares(self):
        """ Returns all subsquares in a sudoku """
        subsquares = []
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subsquare = list(itertools.chain.from_iterable(row[j:j+3] for row in self.grid[i:i+3]))
                subsquares.append(subsquare)
        return subsquares


    # # Returns true if number is one of possible numbers in given cell
    # def num_possible(self, n, row, col):
    #     for i in range(9):
    #         if self.grid[row][i] == n or self.grid[i][col] == n:
    #             return False
    #     square = subsquares[math.floor(row/3) + (3 * math.floor(col/3))]
    #     for i in range(9):
    #         if square[i] == n:
    #             return False
    #     return True