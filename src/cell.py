class Cell:
    def __init__(self, value, domain, neighbors):
        """ Cell initializer """
        self.value = value              # The current value (0 if no value)
        self.domain = domain            # A list of possible values for cells
        self.neighbors = neighbors      # A list of all fields that this field is constrained by


    def remove_from_domain(self, n):
        """ Removes the given value from the domain, and possibly assigns the last value to the field """
        self.domain = self.domain.remove(n)
        if len(domain) == 1:
            self.value = self.domain[0]
    

    def update_neighbors(self, neighbors):
        """ Updates the neighbors of cell """
        self.neighbors = neighbors