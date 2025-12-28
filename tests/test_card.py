"""
Program: Test Card
Author: Maxwell Varlack
Description: This program is used to 
Test the Card class.
"""
import unittest
from card import Card


class TestCard(unittest.TestCase):
    def test_set_card(self) -> any:
        """
        Test to verify the set_card method
        """
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.suite, "Hearts")
        
    def test_set_card_no_output(self) -> None:
        """
        Test to verify the test_set_card_no_output method
        :param self: Description
        """
        self.assertIsNone(Card().set_card("Hearts","A"))
        
    def test_get_card_output(self) -> None:
        """
        Test to verify the test_get_card_output method
        :param self: Description
        """
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertIsNotNone(card_a.get_card())
        
    def test_get_card(self) -> None:
        """
        Tet to verify the test_get_card method
        :param self: Description
        """
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.get_card(), ('Hearts', 'A'))
        
    def test_get_suite_output(self) -> None:
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertIsNotNone(card_a.get_suite())
        
    def test_get_suite(self) -> None:
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.get_suite(), "Hearts")
        
    def test_get_rank_output(self) -> None:
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertIsNotNone(card_a.get_rank(), "A")
        
    def test_print_output(self) -> None:
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertIsNotNone(card_a.__repr__())
        
    def test_print(self) -> None:
        card_a = Card()
        card_a.set_card("Hearts", "A")
        self.assertEqual(card_a.__repr__(), "A of Hearts")
        