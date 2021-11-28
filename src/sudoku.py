import itertools
import math

from cell import Cell


class Sudoku:
    def __init__(self, filename):
        """ Sudoku initializer """
        self.grid = self.read_sudoku(filename)
        self.subsquares = []
        self.init_neighbors()
        self.init_domains()
        # for neigh in self.grid[4][4].neighbors:
        #     print(f"neighbor: {neigh.value}")
    

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

    
    def init_domains(self):
        """ Initializes domains of all cells """
        for i in range(9):
            for j in range(9):
                # Case value is set, domain is that value
                if self.grid[i][j].value != 0:
                    self.grid[i][j].domain = [self.grid[i][j].value]
                # Case value is not set, generate domain based on neighbor values
                else:
                    for val in self.grid[i][j].domain:
                        for neighbor in self.grid[i][j].neighbors:
                            if i == 4 and j == 4:
                                print(neighbor.value)
                                print(f"value = {self.grid[i][j].value}")
                            if val == neighbor.value:
                                self.grid[i][j].remove_from_domain(val)


    def generate_neighbors(self, row, col):
        """ Returns all neighbors of a cell (which constrain it) """
        neighbors = {}
        for i in range(9):
            if i != row:
                neighbors[(col,i)] = self.grid[col][i]
        for j in range(9):
            if j != col:
                neighbors[(j,row)] = self.grid[j][row]
        self.get_subsquare(row, col, neighbors)
        # print(f"nr of neighbors after subsquares: {len(list(set(neighbors)))}")
        return list(neighbors.values())


    def get_subsquare(self, row, col, neighbors):
        """ Returns all neighbors inside the same subsquare """
        square_row = math.floor(row/3) * 3
        square_col = math.floor(col/3) * 3
        for i in range(square_row, square_row+3):
            for j in range(square_col, square_col+3):
                if (i != row or j != col):
                    neighbors[(j,i)] = self.grid[j][i]


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
    #     square = self.subsquares[math.floor(row/3) + (3 * math.floor(col/3))]
    #     for i in range(9):
    #         if square[i] == n:
    #             return False
    #     return True