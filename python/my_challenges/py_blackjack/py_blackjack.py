import random
from random import shuffle

Card_Scores = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9' : 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10,
         }

class Card:
    RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']

    # def __init__(self, suit=0, rank=0):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)
        # return "%s of %s" % (
        #         Card.RANKS[self.rank], 
        #         Card.SUITS[self.suit])
        # return '{0} of {1}'.format(Card.RANKS[self.rank], Card.SUITS[self.suit])
    # @property
    def score(self):
        return Card_Scores[self.rank]
    
class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
        # for suit in range(4):
            for rank in Card.RANKS:
            # for rank in range(0,13):
                self.cards.append(Card(rank, suit))

    def pop(self):
        return self.cards.pop()

    def __str__(self):
        deck = ""
        for card in range(len(self.cards)):
            deck += str(self.cards[card]) + ", "
        return deck

    def shuffle(self):
        return random.shuffle(self.cards)

    # Deal takes a list of Hand objects ie containg a string of names of each player who requires a hand, and the number of cards to deal to each
    def deal(self, hands, num_cards):
        for name in hands:
            for card in range(num_cards):
                card = self.pop()
                name.add_card(card)

class Hand(Deck):
    def __init__(self, name=""):
        self.cards = []
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def score(self):
        card_sum = sum(map(lambda card: card.score(), self.cards))
        num_aces = len(list(filter(lambda card: card.rank == "Ace", self.cards)))
        if card_sum > 21 and num_aces > 0:
            for ace in range(num_aces):
                while card_sum > 21:
                    card_sum = card_sum -10
                    # print(card_sum)
                return card_sum
        elif card_sum > 21 and num_aces < 1:
            return 0
        else:
            return card_sum

