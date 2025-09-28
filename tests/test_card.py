import unittest
from card import Card

class TestCard(unittest.TestCase):
    def set_card(self):
        self.assertIsNotNone(Card().set_card("Hearts","A"))