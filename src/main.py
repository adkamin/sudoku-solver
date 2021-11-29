""" Author:  Andrea Minichova (s1021688) 
    Project: Sudoku solver using AC-3 algorithm """

from sudoku import Sudoku
from solver import Solver


def main():
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    filename = "Sudoku" + nr + ".txt"
    sudoku = Sudoku(filename)
    print("Initial sudoku:")
    print(sudoku)

    solver = Solver(sudoku)
    if solver.solve() and sudoku.is_solution():
        print(f"Solved sudoku in {solver.steps} steps!")
        print(sudoku)
    else:
        print("Could not solve sudoku")

    
if __name__ == "__main__":
    main()