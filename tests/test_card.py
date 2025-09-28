import unittest
from card import Card

class TestCard(unittest.TestCase):
    def test_set_card(self):
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.suite, "Hearts")
    def test_set_card_no_output(self):
        self.assertIsNone(Card().set_card("Hearts","A"))
    def test_get_card_output(self):
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertIsNotNone(card_a.get_card())
    def test_get_card(self):
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.get_card(), ('Hearts', 'A'))
        