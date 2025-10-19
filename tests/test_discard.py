"""
Program: Test Discard
Author: Maxwell Varlack
Description: This program is used to 
Test the Discard class.
"""
import unittest
from card import discard
from card import card

class TestDiscard(unittest.TestCase):
    def test_add(self):
        card_a = card()
        card_a.set_card("Hearts", "A")
        discard_a = discard()
        discard_a.add(card_a)
        self.assertIsNotNone(discard_a.pile)