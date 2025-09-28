class Card:
    def __init__(self):
        self.suite = ""
        self.rank = ""
    def get_card(self):
        return (self.suite, self.rank)
    def set_card(self,suite,rank):
        self.suite = suite
        self.rank = rank
    def get_suite(self):
        return self.suite
    def get_rank(self):
        return self.rank
    def __repr__(self):
        return f"{self.rank} of {self.suite}"