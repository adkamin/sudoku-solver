class Arc:
    def __init__(self, heuristics, cell1, cell2):
        """ Arc initializer """
        self.heuristics = heuristics
        self.fst = cell1
        self.snd = cell2


    def __eq__(self, other):
        """ Operator == to state that arcs are equal if they are the same object """
        return self.fst is other.fst and self.snd is other.snd


    def __lt__(self, other):
        # no deliberate ordering
        if self.heuristics == 0:
            return True

        # order both elements inside tuple by smaller domain
        if self.heuristics == 1:
            if (self.fst == other.fst):
                return self.snd < other.snd
            else:
                return self.fst < other.fst

        # order only first element
        elif self.heuristics == 2:
            return self.fst < self.snd

        # first domain is smaller, second domain is bigger
        elif self.heuristics == 3:
            if (self.fst == other.fst):
                return self.snd > other.snd
            else:
                return self.fst < other.fst

        # order both elements inside tuple by bigger domain
        elif self.heuristics == 4:
            if (self.fst == other.fst):
                return self.snd > other.snd
        else:
            return self.fst > other.fst