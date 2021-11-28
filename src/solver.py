from sudoku import Sudoku
import heapq

class Solver:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.q = self.generate_arcs()  # Priority queue of arcs (pairs of cells)


    def generate_arcs(self):
        """ Initializes the priority queue to contain all possible arcs """
        q = []
        for i in range(9):
            for j in range(9):
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    # Only generate arcs where at least one cell does not have set value
                    if self.sudoku.grid[i][j] != 0 or neighbor.value != 0: 
                        arc = (self.sudoku.grid[i][j], neighbor)
                    q.append(arc)
        heapq.heapify(q)
        return q


    def solve(self):
        """ AC-3 algorithm """
        """ Returns true if constraints can be satisfied, returns false otherwise"""
        # counter = 0
        while self.q:
            # print(f"iteration nr {counter}")
            # counter+=1
            arc = heapq.heappop(self.q)
            # print(f"Length of domain of c1: {len(arc[0].domain)} and of c2: {len(arc[1].domain)}" )
            # print(f"c1 is: {arc[0].value} and c2 is {arc[1].value}" )
            if self.revise(arc):
                if arc[0].domain == 0:
                    return False
                for neighbor in arc[0].get_other_neighbors(arc[1]):
                    if (neighbor, arc[0]) not in self.q:
                        heapq.heappush(self.q, (neighbor, arc[0]))
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
        for value in arc[0].domain:
            if value in arc[1].domain:
                arc[0].remove_from_domain(value)
                revised = True
        return revised


        



    # TODO fix, think about where to put this
    def is_solution(self):
        return self.sudoku.is_solution()