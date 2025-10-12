import unittest
from card import Card, Deck, Hand

class TestHand(unittest.TestCase):
    def test_hand_add_card(self):
        card_a = Card()
        hand_a = Hand()
        card_a.set_card("Hearts", "A")
        hand_a.add_card(card_a)
        self.assertEqual(len(hand_a.cards), 1)
        
    def test_initial(self):
        deck_a = Deck()
        deck_a.create()
        cards = []
        cards = deck_a.deal_many(5)
        hand_a = Hand()
        hand_a.initial(cards)
        self.assertEqual(len(hand_a.cards), 5)
        
    def test_view(self):
        deck_a = Deck()
        deck_a.create()
        cards = []
        cards = deck_a.deal_many(5)
        hand_a = Hand()
        hand_a.initial(cards)
        self.assertIsNotNone(hand_a.view)
        