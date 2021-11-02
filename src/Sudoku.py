# Author: Andrea Minichova (s1021688)

# Read a sudoku text file into a global sudoku 2D list
def read_sudoku():
    global sudoku 
    sudoku = [[0 for i in range(9)] for j in range(9)] 
    nr = input("Specify sudoku file (1,2,3,4 or 5): ")
    file = "Sudoku" + nr + ".txt"
    with open(file) as f:
        sudoku = f.readlines()

# Prints a visual representation of sudoku
def print_sudoku():
    output = "╔═══════╦═══════╦═══════╗\n"
    for i in range(9):
        if i == 3 or i == 6:
            output += "╠═══════╬═══════╬═══════╣\n"
        output += "║ "
        for j in range(9):
            if j == 3 or j == 6:
                output += "║ "
            output += sudoku[i][j] + " "
        output += "║\n"
    output += "╚═══════╩═══════╩═══════╝\n"
    print(output)

# Returns true, if sudoku is solved, returns false otherwise
def is_solution():
    for row in sudoku:
        if len(set(row)) != len(row):
            return False
    columns = zip(*sudoku)
    for col in columns:
        if len(set(col)) != len(col):
            return False
    print("is solution!")
    # TODO: Check cell
    return True

def main():
    read_sudoku()
    print_sudoku()
    is_solution()
    #check()

if __name__ == "__main__":
    main()