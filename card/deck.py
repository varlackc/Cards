from card import Card
class Deck:
    def __init__(self):
        self.pile = []
    def create(self):
        suites = ["Spades", "Diamonds", "Clubs", "Hearts"]
        ranks = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K",]
        card_group = []
        i = 0
        for suite in suites:
            for rank in ranks:
                #card_a.set_card(suite, rank)
                self.pile.append(None)
                self.pile[i] = Card()
                self.pile[i].set_card(suite, rank)
                i += 1
    # shuffle

    # deal
    def deal(self):
        return self.pile.pop(0)
    # __len__
    
    # __repr__ Deck of # cards