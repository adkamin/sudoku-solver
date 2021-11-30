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

    # Heuristics:
    # heuristics = 0 # no deliberate ordering
    # heuristics = 1 # order both elements inside tuple by smaller domain
    # heuristics = 2 # order only first element
    # heuristics = 3 # first domain is smaller, second domain is bigger
    heuristics = 4 # order both elements inside tuple by bigger domain

    solver = Solver(sudoku, heuristics)
    if solver.solve() and sudoku.is_solution():
        print(f"Solved sudoku in {solver.steps} steps!")
        print(sudoku)
    else:
        print("Could not solve sudoku")
        print(f"Took {solver.steps} steps")

    
if __name__ == "__main__":
    main()