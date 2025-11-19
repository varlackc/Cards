"""
Program: Card
Author: Maxwell Varlack
Description: This program is used to 
to represent a Card.
"""
class Card:
    def __init__(self) -> None:
        self.suite = ""
        self.rank = ""
        
    def get_card(self) -> tuple[str | any, str | any]:
        return (self.suite, self.rank)
    
    def set_card(self,suite,rank):
        self.suite = suite
        self.rank = rank
        
    def get_suite(self):
        return self.suite
    
    def get_rank(self):
        return self.rank
    
    def __repr__(self):
        return f"{self.rank} of {self.suite}"