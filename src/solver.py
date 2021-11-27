from sudoku import Sudoku
from queue import PriorityQueue

class Solver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.queue = self.generate_arcs()  # Priority queue of arcs (pairs of cells)

    def generate_arcs(self):
        q = PriorityQueue()
        for i in range(9):
            for j in range(9):
                # if (len(self.sudoku.grid[i][j].neighbors) != 21):
                    # print("cell " + str(i) + str(j) + " has " + str(len(self.sudoku.grid[i][j].neighbors)) + " neighbors.")
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    arc = (self.sudoku.grid[i][j], neighbor)
                    q.put(arc)
        print("length of priority queue is: " + str(q.qsize()))
        return q


    # Arc is a tuple of cells
    def solve(self): 
        if self.sudoku.is_solution():
            return True
        else:
            return False

        # Queue q = list of Arcs, initailly all Arcs
        # while q not empty
        #   (Xm,Xn) <- REMOVE-FIRST(q)
        #   REVISE(sudoku, Xm, Xn)
        #   if new size of Dm = 0 
        #      return false
        #   if Dm has been changed
        #      for each Xk in {neighbors of Xm} - Xn
        #         if (Xk, Xm) not in q
        #            add (Xk, Xm) to q
        # return true


    # TODO fix, think about where to put this
    def is_solution(self):
        return self.sudoku.is_solution()