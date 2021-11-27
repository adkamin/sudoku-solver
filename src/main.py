""" Author:  Andrea Minichova (s1021688) 
    Project: Sudoku solver using AC-3 algorithm """

from sudoku import Sudoku
from solver import Solver

def main():
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    filename = "Sudoku" + nr + ".txt"
    sudoku = Sudoku(filename)
    print("Initial sukodu: ")
    print(sudoku)

    subs = sudoku.get_subsquare(3,3)
    for sub in subs:
        print(sub.value)


    steps = 0
    solver = Solver(sudoku)
    if solver.solve() and solver.is_solution():
        print(f"Solved sudoku in {steps} steps!")
    else:
        print("Could not solve sudoku")

    
     

    
if __name__ == "__main__":
    main()