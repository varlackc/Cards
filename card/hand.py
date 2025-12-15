"""
Program: Hand
Author: Maxwell Varlack
Description: This program is used to 
to represent a player card hand.
"""
from card import Card


class Hand:
    def __init__(self) -> None:
        """
        Method to initialize the Hand class
        """
        self.cards = []
        self.hand_size = 5
        
    def add_card(self, card_a) -> None:
        """
        Method to add a card to the hand
        """
        self.cards.append(card_a)
        while len(self.cards) > self.hand_size:
            self.cards[0]
            
    def initial(self, cards) -> None:
        """
        Add an initial list of cards to the hand
        """
        size = len(cards)
        for card in cards:
            self.cards.append(card)
        """
        Remove any excess cards
        """
        while len(self.cards) > self.hand_size:
            self.cards[0]
            
    def view(self) -> None:
        """
        Method to view the card hand
        """
        result = []
        for card in self.cards:
            result.append(card.get_card())
        return tuple(result) 
    
    def get_by_index(self, index) -> None:
        """
        Method to get a card by the index
        """
        result = None
        if(index < len(self.cards)):
            result = self.cards[index]
        else:
            result = None
        return result
    
    def get_index(self, suite, rank) -> None:
        """
        Method to get the index of a particular card
        """
        result = None
        for i in range(len(self.cards)):
            if(self.cards[i].suite == suite and self.cards[i].rank == rank):
                return i
        return result
    
    def remove(self, suite, rank) -> None:
        """
        Method to remove a card from the hand
        """
        result = None
        for i in range(len(self.cards)):
            if(self.cards[i].suite == suite and self.cards[i].rank == rank):
                result = self.cards.pop(i)
                return result
        return result
    
    def remove_by_index(self, index) -> None:
        result = None
        if (index < len(self.cards)):
            result = self.cards.pop(index)
        return result
                