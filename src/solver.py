from sudoku import Sudoku
from collections import deque

class Solver:
    def __init__(self, sudoku):
        """ Solver initializer """
        self.sudoku = sudoku           # Sudoku to solve
        self.q = self.generate_arcs()  # Priority queue of arcs (pairs of cells)


    def generate_arcs(self):
        """ Initializes the priority queue to contain all possible arcs """
        q = deque()
        for i in range(9):
            for j in range(9):
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    # Only generate arcs where at least one cell does not have set value
                    # if self.sudoku.grid[i][j].value != 0 and neighbor.value != 0: 
                    arc = (self.sudoku.grid[i][j], neighbor)
                    q.append(arc)
        return q


    def solve(self):
        """ AC-3 algorithm """
        """ Returns true if constraints can be satisfied, returns false otherwise"""
        counter = 0
        while self.q:
            print(counter)
            counter += 1
            arc = self.q.popleft()
            print(f"currently working on arc with values: {arc[0].value} {arc[1].value}")
            if self.revise(arc):
                if not arc[0].domain:
                    return False
                for neighbor in arc[0].get_other_neighbors(arc[1]):
                    if (neighbor, arc[0]) not in self.q:
                        self.q.append((neighbor, arc[0]))
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
        """ Returns true if domain of arc[0] is revised, returns false otherwise """
        revised = False
        orig_domain = list.copy(arc[0].domain)
        for value in orig_domain:
            if value in arc[1].domain:
                arc[0].remove_from_domain(value)
                revised = True
        return revised


    def is_solution(self):
        return self.sudoku.is_solution()