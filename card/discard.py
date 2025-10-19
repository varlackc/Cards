"""
Program: Discard
Author: Maxwell Varlack
Description: This program is used to 
to represent a discard pile.
"""
from card import Card


class Discard:
    def __init__(self):
        self.pile = []
        
    def add(self, card_a):
        self.pile.append(card_a)