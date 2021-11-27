from sudoku import Sudoku
from queue import PriorityQueue

class Solver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.queue = self.generate_arcs()  # Priority queue of arcs (pairs of cells)


    def generate_arcs(self):
        """ Initializes the priority queue to contain all possible arcs """
        q = PriorityQueue()
        for i in range(9):
            for j in range(9):
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    arc = (self.sudoku.grid[i][j], neighbor)
                    # print(f"arc {i} {j} : {arc[0].value}, {arc[1].value}.")
                    q.put(arc)
        return q


    def solve(self):
        """ AC-3 algorithm """
        """ Returns true if constraints can be satisfied, returns false otherwise"""
        counter = 0
        while not self.queue.empty():
            print(f"iteration nr {counter}")
            counter+=1
            (c1,c2) = self.queue.get()
            orig_domain = c1.domain
            self.revise((c1,c2))
            if c1.domain == 0:
                return False
            if c1.domain != orig_domain:
                print(type(c1))
                for neighbor in c1.get_other_neighbors(c2):
                    if not any((neighbor, c1) in arc for arc in self.queue.queue):
                    # if (neighbor, c1) not in self.queue:
                        self.queue.put((neighbor, c1))
        return True

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

    def revise(self, arc):
        (c1,c2) = arc
        if (c1.domain):
            for value in c1.domain:
                if c2.domain:
                    if value in c2.domain:
                        c1.remove_from_domain(value)
                        return


        



    # TODO fix, think about where to put this
    def is_solution(self):
        return self.sudoku.is_solution()