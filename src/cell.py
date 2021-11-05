class Cell:
    def __init__(self, value, domain, neighbors):
        self.value = value         # The current value (0 if no value)
        self.domain = domain       # A list of possible valuse for cells
        self.neighbors = neighbors      # A list of all fields that this field is constrained by

    def get_value(self):
        return self.value

    def set_value(self, n):
        self.value = n

    def get_domain(self):
        return self.domain

    def remove_from_domain(self, n):
        self.domain = self.domain.remove(n)
        if len(domain) == 1:
            self.value = self.domain[0]

    def update_neighbors(self, neighbors):
        self.neighbors = neighbors