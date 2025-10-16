from card import Card


class Discard:
    def __init__(self):
        self.pile = []
        
    def add(self, card_a):
        self.pile.append(card_a)