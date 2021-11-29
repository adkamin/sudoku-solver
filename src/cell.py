class Cell:
    def __init__(self, value, domain, neighbors):
        """ Cell initializer """
        self.value = value              # The current value (0 if no value)
        self.domain = domain            # A list of possible values for cells
        self.neighbors = neighbors      # A list of all cells that this cell is constrained by

    
    def __lt__(self, other):
        """ Operator < for domain size (necessary for priority queue of cell arcs) """
        return len(self.domain) < len(other.domain)

    
    def __eq__(self, other):
        """ Operator == to state that cells are equal if they are the same object """
        return self is other


    def remove_from_domain(self, n):
        """ Removes the given value from the domain, and possibly assigns the last value to the cell """
        if n in self.domain:
            self.domain.remove(n)
        if len(self.domain) == 1:
            self.value = self.domain[0]
    

    def update_neighbors(self, neighbors):
        """ Updates neighbors """
        self.neighbors = neighbors


    def get_other_neighbors(self, other):
        """ Returns neighbors excluding the neighbor 'other' """
        orig_neighbors = list.copy(self.neighbors)
        if other in orig_neighbors:
            orig_neighbors.remove(other)
        return orig_neighbors