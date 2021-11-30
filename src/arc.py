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
        """ Operator < for arcs (necessary for priority queue) """
        # no deliberate ordering
        if self.heuristics == 0:
            return True

        # order both elements inside by smaller domain
        if self.heuristics == 1:
            if len(self.fst.domain) == len(other.fst.domain):
                return self.snd < other.snd
            else:
                return self.fst < other.fst

        # order both elements inside by bigger domain (best)
        if self.heuristics == 2:
            if len(self.fst.domain) == len(other.fst.domain):
                return self.snd > other.snd
        else:
            return self.fst > other.fst

        # first domain is smaller, second domain is bigger
        if self.heuristics == 3:
            if len(self.fst.domain) == len(other.fst.domain):
                return self.snd > other.snd
            else:
                return self.fst < other.fst

        # first domain is smaller, second domain is bigger
        if self.heuristics == 4:
            if len(self.fst.domain) == len(other.fst.domain):
                return self.snd < other.snd
            else:
                return self.fst > other.fst


