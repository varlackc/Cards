"""
Program: Deck
Author: Maxwell Varlack
Description: This program is used to 
to represent a Deck of cards.
"""
from card import Card
import random


class Deck:
    def __init__(self) -> None:
        self.card = Card()
        self.pile = []
        
    def create(self) -> None:
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
    def shuffle(self) -> None:
        random.shuffle(self.pile)
        
    # deal
    def deal(self) -> any | None:
        try:
            result = self.pile.pop(0)
        except:
            result = None
        self.card = result
        return result
    
    def deal_many(self, count) -> list:
        result = []
        for i in range(count):
            try:
                result.append(self.pile.pop(0))
            except:
                continue
            self.card = result
        return result
        
    # __len__
    def __len__(self) -> int:
        result = len(self.pile)
        return result
    
    # __repr__ Deck of # cards
    def __repr__(self) -> str:
        return f"The deck contains {len(self.pile)} cards."