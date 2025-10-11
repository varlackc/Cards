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