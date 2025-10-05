import unittest
from card import Deck

class TestDeck(unittest.TestCase):
    def test_create(self):
        deck_a = Deck()
        deck_a.create()
        self.assertEqual(len(deck_a.pile), 52)
        