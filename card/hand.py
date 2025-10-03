from card import Card

class Hand:
    def __init__(self):
        self.cards = []
        self.hand_size = 5
    def add_card(self, card_a):
        self.cards.append(card_a)
        while len(self.cards) > self.hand_size:
            self.cards[0]
