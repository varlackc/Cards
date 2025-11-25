"""
Program: Hand
Author: Maxwell Varlack
Description: This program is used to 
to represent a player card hand.
"""
from card import Card


class Hand:
    def __init__(self) -> None:
        self.cards = []
        self.hand_size = 5
        
    def add_card(self, card_a) -> None:
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
    
    def get_index(self, suite, rank):
        result = None
        for i in range(len(self.cards)):
            if(self.cards[i].suite == suite and self.cards[i].rank == rank):
                return i
        return result
    
    def remove(self, suite, rank):
        result = None
        for i in range(len(self.cards)):
            if(self.cards[i].suite == suite and self.cards[i].rank == rank):
                result = self.cards.pop(i)
                return result
        return result
    
    def remove_by_index(self, index):
        result = None
        if (index < len(self.cards)):
            result = self.cards.pop(index)
        return result
                