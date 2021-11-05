# Author: Andrea Minichova (s1021688)

import itertools
import math

from cell import Cell

class Sudoku:
    def __init__(self, filename):
        self.grid = self.read_sudoku(filename)
        self.init_neighbors()
    

    # Read a sudoku text file into a global sudoku 2D list
    def read_sudoku(self, filename):
        grid = [[0 for i in range(9)] for j in range(9)]
        with open(filename) as f:
            for i in range(9):
                for j in range(9):
                    cell = Cell((int(f.read(1))), list(range(1,10)), [])
                    grid[i][j] = cell
                f.read(1)
        return grid


    def init_neighbors(self):
        for i in range(9):
            for j in range(9):
                self.grid[i][j].update_neighbors(self.generate_neighbors(i,j))

    
    # Generate neighbors
    def generate_neighbors(self, row, col):
        vertical, horizontal, subsquare, neighbors = [], [], [], []
        for i in range(9):
            for j in range(9):
                if row != i or col != j:
                    vertical.append(self.grid[row][i])
                    horizontal.append(self.grid[j][col])
                subsquare = self.get_subsquare(row, col)
        neighbors = list(set(vertical + horizontal + subsquare)) # make into set and back to list to remove duplicates
        return neighbors


    def get_subsquare(self, row, col):
        subsquare = []
        square_row = math.floor(row/3) * 3
        square_col = math.floor(col/3) * 3
        for i in range(square_row, square_row+3):
            for j in range(square_col, square_col+3):
                if square_row != row or square_col != col:
                    subsquare.append(self.grid[i][j])
        return subsquare


    # Prints a visual representation of sudoku
    def __str__(self):
        output = "╔═══════╦═══════╦═══════╗\n"
        for i in range(9):
            if i == 3 or i == 6:
                output += "╠═══════╬═══════╬═══════╣\n"
            output += "║ "
            for j in range(9):
                if j == 3 or j == 6:
                    output += "║ "
                output += ". " if self.grid[i][j].get_value() == 0 else chr(self.grid[i][j].get_value() + ord('0')) + " "
            output += "║\n"
        output += "╚═══════╩═══════╩═══════╝\n"
        return output


    # Returns true, if sudoku is solved, returns false otherwise
    def is_solution(self):
        for row in self.grid:
            if len(set(row)) != len(row):
                return False
        columns = zip(*self.grid)
        for col in columns:
            if len(set(col)) != len(col):
                return False
        for square in subsquares:
            if len(set(square)) != len(square):
                return False
        print("Solved!")
        return True


    # Returns true if number is one of possible numbers in given cell
    def num_possible(self, n, row, col):
        for i in range(9):
            if self.grid[row][i] == n or self.grid[i][col] == n:
                return False
        square = subsquares[math.floor(row/3) + (3 * math.floor(col/3))]
        for i in range(9):
            if square[i] == n:
                return False
        return True