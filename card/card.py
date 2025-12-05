"""
Program: Card
Author: Maxwell Varlack
Description: This program is used to 
to represent a Card.
"""
class Card:
    def __init__(self) -> None:
        """
        initialize the Card class
        """
        self.suite = ""
        self.rank = ""
        
    def get_card(self) -> tuple[str | any, str | any]:
        """
        Method to get the values of a card
        """
        return (self.suite, self.rank)
    
    def set_card(self,suite,rank) -> None:
        """
        Method to get values to a card
        """
        self.suite = suite
        self.rank = rank
        
    def get_suite(self) -> str | any:
        """
        Method to optain the suite of a particular card
        """
        return self.suite
    
    def get_rank(self) -> str | any:
        return self.rank
    
    def __repr__(self) -> str:
        return f"{self.rank} of {self.suite}"