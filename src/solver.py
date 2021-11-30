from queue import PriorityQueue
from arc import Arc

class Solver:
    def __init__(self, sudoku, heuristics):
        """ Solver initializer """
        self.sudoku = sudoku           # Sudoku to solve
        self.h = heuristics            # Heuristics for ordering of arcs
        self.q = self.generate_arcs()  # Priority queue of arcs (pairs of cells)
        self.steps = 0                 # Steps the solver takes to solve sudoku


    def generate_arcs(self):
        """ Initializes the priority queue to contain all arcs """
        q = PriorityQueue()
        for i in range(9):
            for j in range(9):
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    arc = Arc(self.h, self.sudoku.grid[i][j], neighbor)
                    q.put(arc)
        return q


    def solve(self):
        """ AC-3 algorithm """
        """ Returns true if constraints can be satisfied, returns false otherwise"""
        while not self.q.empty():
            self.steps += 1
            arc = self.q.get()
            if self.revise(arc):
                if not arc.fst.domain:
                    return False
                for neighbor in arc.fst.get_other_neighbors(arc.snd):
                    newarc = Arc(self.h, neighbor, arc.fst)
                    if newarc not in self.q.queue:
                        self.q.put(newarc)
            # print(self.sudoku)
        return True
 

    def revise(self, arc):
        """ Returns true if domain of arc[0] is revised, returns false otherwise """
        revised = False
        orig_domain = list.copy(arc.fst.domain)
        for value in orig_domain:
            if not self.consistent(value, arc.snd):
                arc.fst.remove_from_domain(value)
                revised = True
        return revised


    def consistent(self, value, cell):
        """ Returns true if arc is consistent """
        for value2 in cell.domain:
            if value != value2:
                return True
        return False