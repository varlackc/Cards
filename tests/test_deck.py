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
    def test_deal_many(self):
        result = []
        deck_a = Deck()
        deck_a.create()
        result = deck_a.deal_many(5)
        self.assertEqual(len(result), 5)
        