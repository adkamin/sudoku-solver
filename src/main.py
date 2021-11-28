""" Author:  Andrea Minichova (s1021688) 
    Project: Sudoku solver using AC-3 algorithm """

from sudoku import Sudoku
from solver import Solver


def main():
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    filename = "Sudoku" + nr + ".txt"
    sudoku = Sudoku(filename)

    # # Testing domain
    # print(f"Domain of (0,0): ")
    # for val in sudoku.grid[0][0].domain:
    #     print(val)

    # # Testing neighbors
    # print(f"Neighbors of (0,0): ")
    # for neigh in sudoku.grid[0][0].neighbors:
    #     print(neigh.value)

    steps = 0
    solver = Solver(sudoku)
    if solver.solve() and solver.is_solution():
        print(f"Solved sudoku in {steps} steps!")
    else:
        print("Could not solve sudoku")
        print(sudoku)


    
if __name__ == "__main__":
    main()