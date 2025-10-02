from card import Card
class Deck:
    def __init__(self):
        self.pile = []
    def create(self):
        suites = ["Spades", "Diamonds", "Clubs", "Hearts"]
        ranks = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K",]
        for suite in suites:
            for rank in ranks:
                self.pile.append(Card().set_card(suite, rank))
    # shuffle

    # deal
    
    # __len__
    
    # __repr__ Deck of # cards