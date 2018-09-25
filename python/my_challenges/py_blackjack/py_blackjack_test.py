import unittest

import py_blackjack
from py_blackjack import Card, Deck, Hand

class PyBlackjackTest(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(1, 1)

    def test_Card_class(self):
        card1 = Card("4", "Clubs")
        self.assertEqual(str(card1), '4 of Clubs')
    def test_deck_contains_52_items(self):
        cardlist = Deck().cards
        self.assertEqual(len(cardlist), 52)
    def test_deck_contains_cards(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.pop()
        deck.shuffle()
        self.assertIn('of', str(card1))

    def test_deck_is_shuffled(self):
        deck = Deck()
        deck.shuffle()
        card1 = deck.pop()
        deck2 = Deck()
        deck2.shuffle()
        card2 = deck2.pop()
        self.assertNotEqual(str(card1), str(card2))

    def test_deck_pop_draws_card(self):
        deck = Deck()
        card1 = deck.pop()
        self.assertEqual(len(deck.cards), 51)

    def test_hand_name(self):
        deck = Deck()
        card1 = deck.pop()
        hand = Hand("Al")
        self.assertEqual(hand.name, "Al")

    def test_hand_has_cards_list(self):
        deck = Deck()
        card1 = deck.pop()
        hand = Hand("Al")
        self.assertEqual(hand.cards, [])

    def test_can_add_cards_to_hand(self):
        deck = Deck()
        card1 = deck.pop()
        hand = Hand("Al")
        hand.add_card(card1)
        print(hand)
        self.assertEqual(len(hand.cards), 1)
        self.assertEqual(str(hand), "King of Spades, ")
        
    def test_deal_makes_hand(self):
        deck = Deck()
        hand = Hand("Al")
        deck.deal([hand] ,2)
        print(hand)
        self.assertEqual(len(hand.cards), 2)
        self.assertEqual(str(hand), "King of Spades, Queen of Spades, ")

    def test_deal_to_two_players(self):
        deck = Deck()
        hand = Hand("Al")
        hand2 = Hand("Fred")
        deck.deal([hand, hand2] ,2)
        print(hand)
        print(hand2)
        self.assertEqual(len(hand.cards), 2)
        self.assertEqual(len(hand2.cards), 2)
        self.assertNotEqual(str(hand2), "King of spades, Queen of Spades, ")
        self.assertNotEqual(str(hand2), str(hand))

    def test_score_of_card(self):
        card = Card("2", "Diamonds")
        self.assertEqual(card.score(), 2)

    def test_score_of_hand(self):
        card = Card("4", "Diamonds")
        hand = Hand("Al")
        hand.add_card(card)
        self.assertEqual(hand.score(), 4)

    def test_blackjack_score_aces_low_over_21(self):
        card = Card("Ace", "Diamonds")
        card2 = Card("6", "Diamonds")
        card3 = Card("7", "Diamonds")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        hand.add_card(card3)
        self.assertEqual(hand.score(), 14)

    def test_score_over_21_bust(self):
        card = Card("8", "Diamonds")
        card2 = Card("6", "Diamonds")
        card3 = Card("9", "Diamonds")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        hand.add_card(card3)
        self.assertEqual(hand.score(), 0)
        
    def test_score_21_blackjack(self):
        card = Card("Ace", "Diamonds")
        card2 = Card("10", "Diamonds")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        self.assertEqual(hand.score(), 21)
    
    def test_score_with_2_aces(self):
        card = Card("Ace", "Diamonds")
        card2 = Card("Ace", "Hearts")
        card3 = Card("10", "Hearts")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        hand.add_card(card3)
        self.assertEqual(hand.score(), 12)

    def test_score_with_3_aces(self):
        card = Card("Ace", "Diamonds")
        card2 = Card("Ace", "Hearts")
        card4 = Card("Ace", "Spades")
        card3 = Card("10", "Hearts")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        hand.add_card(card3)
        hand.add_card(card4)
        self.assertEqual(hand.score(), 13)

    def test_2_aces_one_high_one_low(self):
        card = Card("Ace", "Diamonds")
        card2 = Card("Ace", "Hearts")
        card3 = Card("9", "Hearts")
        hand = Hand("Al")
        hand.add_card(card)
        hand.add_card(card2)
        hand.add_card(card3)
        self.assertEqual(hand.score(), 21)

    def test_can_add_to_existing_hand(self):
        deck = Deck()
        hand = Hand("Al")
        deck.deal([hand] ,2)
        print(hand)
        deck.deal([hand] ,1)
        self.assertEqual(len(hand.cards), 3)
        self.assertEqual(str(hand), "King of Spades, Queen of Spades, Jack of Spades, ")

    def test_str_of_deck(self):
        deck = Deck()
        print(deck)
        self.assertEqual("""Ace of Clubs, 2 of Clubs, 3 of Clubs, 4 of Clubs, 5 of Clubs, 6 of Clubs, 7 of Clubs, 8 of Clubs, 9 of Clubs, 10 of Clubs, Jack of Clubs, Queen of Clubs, King of Clubs, Ace of Diamonds, 2 of Diamonds, 3 of Diamonds, 4 of Diamonds, 5 of Diamonds, 6 of Diamonds, 7 of Diamonds, 8 of Diamonds, 9 of Diamonds, 10 of Diamonds, Jack of Diamonds, Queen of Diamonds, King of Diamonds, Ace of Hearts, 2 of Hearts, 3 of Hearts, 4 of Hearts, 5 of Hearts, 6 of Hearts, 7 of Hearts, 8 of Hearts, 9 of Hearts, 10 of Hearts, Jack of Hearts, Queen of Hearts, King of Hearts, Ace of Spades, 2 of Spades, 3 of Spades, 4 of Spades, 5 of Spades, 6 of Spades, 7 of Spades, 8 of Spades, 9 of Spades, 10 of Spades, Jack of Spades, Queen of Spades, King of Spades, """, str(deck))


if __name__ == '__main__':
    unittest.main()
