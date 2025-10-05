import unittest
from card import Card, Hand

class TestHand(unittest.TestCase):
    def test_hand_add_card(self):
        card_a = Card()
        hand_a = Hand()
        card_a.set_card("Hearts", "A")
        hand_a.add_card(card_a)
        self.assertEqual(len(hand_a.cards), 1)
        