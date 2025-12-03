"""
Program: Test Hand
Author: Maxwell Varlack
Description: This program is used to 
Test the Hand class.
"""
import unittest
from card import Card, Deck, Hand

class TestHand(unittest.TestCase):
    def test_hand_add_card(self) -> None:
        card_a = Card()
        hand_a = Hand()
        card_a.set_card("Hearts", "A")
        hand_a.add_card(card_a)
        self.assertEqual(len(hand_a.cards), 1)
        
    def test_initial(self) -> None:
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
        
    def test_get_by_index(self):
        deck_a = Deck()
        deck_a.create()
        cards = []
        cards = deck_a.deal_many(5)
        hand_a = Hand()
        hand_a.initial(cards)
        self.assertIsNotNone(hand_a.get_by_index(0))
        
    def test_get_index(self):
        hand_a = Hand()
        card_a = Card()
        card_b = Card()
        card_c = Card()
        card_a.set_card("Hearts", "A")
        card_b.set_card("Hearts", "2")
        card_c.set_card("Hearts", "3")
        hand_a.initial([card_a,card_b,card_c])
        self.assertEqual(hand_a.get_by_index("Hearts", "A"), 0)
        
    def test_remove(self):
        hand_a = Hand()
        card_a = Card()
        card_b = Card()
        card_c = Card()
        card_a.set_card("Hearts", "A")
        card_b.set_card("Hearts", "2")
        card_c.set_card("Hearts", "3")
        hand_a.initial([card_a,card_b,card_c])
        self.assertIsNotNone(hand_a.remove("Hearts","A"))
        
    def test_remove_by_index(self):
        hand_a = Hand()
        card_a = Card()
        card_b = Card()
        card_c = Card()
        card_a.set_card("Hearts", "A")
        card_b.set_card("Hearts", "2")
        card_c.set_card("Hearts", "3")
        hand_a.initial([card_a,card_b,card_c])
        self.assertIsNotNone(hand_a.remove_by_index(2))