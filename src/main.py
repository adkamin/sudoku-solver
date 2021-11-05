from sudoku import Sudoku

def main():
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    filename = "Sudoku" + nr + ".txt"
    sudoku = Sudoku(filename)
    print(sudoku)
    print(sudoku.is_solution())

    
if __name__ == "__main__":
    main()