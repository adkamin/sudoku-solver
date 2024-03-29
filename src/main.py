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
    # heuristics = 1 # order both elements inside by smaller domain     (much worse)
    # heuristics = 2 # order both elements inside by bigger domain      (slightly worse)
    # heuristics = 3 # first domain is smaller, second domain is bigger (best)
    heuristics = 4 # first domain is bigger, second domain is smaller   (identical to 3)

    solver = Solver(sudoku, heuristics)
    if solver.solve() and sudoku.is_solution():
        print(f"Solved sudoku in {solver.steps} steps!")
        print(sudoku)
    else:
        print("Could not solve sudoku")
        print(f"Took {solver.steps} steps")

    
if __name__ == "__main__":
    main()