from card import Card
class Deck:
    def __init__(self):
        self.card = Card()
        self.pile = []
    def create(self):
        suites = ["Spades", "Diamonds", "Clubs", "Hearts"]
        ranks = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K",]
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
        try:
            result = self.pile.pop(0)
        except:
            result = None
        self.card = result
        return result
    # __len__
    def __len__(self):
        result = len(self.pile)
        return result
    # __repr__ Deck of # cards