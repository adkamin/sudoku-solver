from sudoku import Sudoku

def main():
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    filename = "Sudoku" + nr + ".txt"
    sudoku = Sudoku(filename)
    print("neighbors: ")
    for i in range(len(sudoku.grid[5][5].neighbors)):
        if sudoku.grid[5][5].neighbors[i].value != 0:
            print(sudoku.grid[5][5].neighbors[i].value)
    print(sudoku)
    print(sudoku.is_solution())

    
if __name__ == "__main__":
    main()