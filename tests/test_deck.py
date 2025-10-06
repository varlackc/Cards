import unittest
from card import Deck

class TestDeck(unittest.TestCase):
    def test_create(self):
        deck_a = Deck()
        deck_a.create()
        self.assertEqual(len(deck_a.pile), 52)
    def test_deal(self):
        deck_a = Deck()
        deck_a.create()
        self.assertIsNotNone(deck_a.deal())
        