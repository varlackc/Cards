"""
Program: Discard
Author: Maxwell Varlack
Description: This program is used to 
to represent a discard pile.
"""
from card import Card


class Discard:
    def __init__(self) -> any:
        """
        Method to initialize the Discard class
        """
        self.pile = []
        
    def add(self, card_a) -> None:
        """
        Method to add a card to the discard pile
        """
        self.pile.append(card_a)
        
    def __len__(self) -> None:
        """
        Method to determine the size of the discard pile
        """
        result = len(self.pile)
        return result