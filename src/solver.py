from queue import PriorityQueue

class Solver:
    def __init__(self, sudoku):
        """ Solver initializer """
        self.sudoku = sudoku           # Sudoku to solve
        self.q = self.generate_arcs()  # Priority queue of arcs (pairs of cells)


    def generate_arcs(self):
        """ Initializes the priority queue to contain all possible arcs """
        q = PriorityQueue()
        for i in range(9):
            for j in range(9):
                for neighbor in self.sudoku.grid[i][j].neighbors:
                    arc = (self.sudoku.grid[i][j], neighbor)
                    q.put(arc)
        return q


    def solve(self):
        """ AC-3 algorithm """
        """ Returns true if constraints can be satisfied, returns false otherwise"""
        # counter = 0
        while not self.q.empty():
            arc = self.q.get()
            if self.revise(arc):
                if not arc[0].domain:
                    return False
                for neighbor in arc[0].get_other_neighbors(arc[1]):
                    if (neighbor, arc[0]) not in list(self.q.queue):
                        self.q.put((neighbor, arc[0]))
            print(self.sudoku)
        return True
 

    def revise(self, arc):
        """ Returns true if domain of arc[0] is revised, returns false otherwise """
        revised = False
        orig_domain = list.copy(arc[0].domain)
        for value in orig_domain:
            if not self.consistent(value, arc):
                arc[0].remove_from_domain(value)
                revised = True
        return revised


    def consistent(self, value, arc):
        """ Returns true if arc is consistent """
        for value2 in arc[1].domain:
            if value != value2:
                return True
        return False


    def is_solution(self):
        """ Returns true if sudoku is solved """
        return self.sudoku.is_solution()