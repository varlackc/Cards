class Card:
    def __init__(self):
        self.suite = ""
        self.value = ""
    def get_card(self):
        return [self.suite, self.value]
    def set_card(self,suite,value):
        self.suite = suite
        self.value = value
    def get_suite(self):
        return self.suite
    