from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_size = 5
    def add_card(self, card_a):
        self.cards.append(card_a)
        while len(self.cards) > self.hand_size:
            self.cards[0]
    def initial(self, cards):
        # add an initial list of cards to the hand
        size = len(cards)
        for card in cards:
            self.cards.append(card)
        # remove any excess cards
        while len(self.cards) > self.hand_size:
            self.cards[0]
    def view(self):
        result = []
        for card in self.cards:
            result.append(card.get_card())
        return tuple(result) 
    def get_by_index(self, index):
        result = None
        if(index < len(self.cards)):
            result = self.cards[index]
        else:
            result = None
        return result