"""
Program: Test Deck
Author: Maxwell Varlack
Description: This program is used to 
Test the Deck class.
"""
import unittest
from card import Deck


class TestDeck(unittest.TestCase):
    def test_create(self) -> None:
        """
        Test to verify the test_create method
        :param self: Description
        """
        deck_a = Deck()
        deck_a.create()
        self.assertEqual(len(deck_a.pile), 52)
        
    def test_deal(self) -> None:
        """
        Test to verify the test_deal method
        :param self: Description
        """
        deck_a = Deck()
        deck_a.create()
        self.assertIsNotNone(deck_a.deal())
        
    def test_deal_many(self) -> None:
        """
        Docstring for test_deal_many
        
        :param self: Description
        """
        result = []
        deck_a = Deck()
        deck_a.create()
        result = deck_a.deal_many(5)
        self.assertEqual(len(result), 5)
        