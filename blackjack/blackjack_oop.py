"""Game of blackjack in OOP"""


class Card:
    """Returns a card and gets the point associated with the card"""

    def __init__(self, rank: str, suit: str) -> None:
        self.rank = rank
        self.suit = suit.upper()

    def to_string(self) -> str:
        """Returns the correct string to represent the card"""
        return self.rank + self.suit

    def get_points(self) -> int:
        """Gets the correct number of points for a card"""
        if self.rank == "A":
            return 11
        if self.rank in {"J", "Q", "K"}:
            return 10
        return int(self.rank)


# pylint: disable=W0621
card = Card("A", "S")
print(card.get_points())

# pylint: disable=R0903
# pylint: disable=W0612


class Hand:
    """Calculates the amount of points in (the players or dealers) hand"""

    def __init__(self, cards: list) -> None:
        all_cards = all(isinstance(card, Card) for card in cards)

        if not all_cards:
            raise ValueError('A Hand can only contain Cards')

        self.cards = cards
        self.points = 0
        self.ace_count = 0

    def get_points(self) -> int:
        """Calculates the total points for a hand of cards"""

        for card in self.cards:
            if card.rank == "A":
                self.ace_count += 1
            self.points += card.get_points()

        if len(self.cards) == 2 and self.ace_count == 2:
            return 21

        return self.points


class Deck:
    """Generates the deck of cards, shuffles it and draws cards one by one"""

    def __init__(self) -> None:
        self.cards = []
        self.generate_deck()

    def generate_deck(self):
        """Generates a deck of cards and returns them"""
        suits = ["S", "D", "C", "H"]
        numbers = ["A", "2", "3", "4", "5", "6",
                   "7", "8", "9", "10", "J", "Q", "K"]
        for suit in suits:
            for number in numbers:
                self.cards.append(Card(number, suit))
        return self.cards

    def draw(self) -> Card:
        """Removes and returns the top card from the deck"""
        return self.cards.pop(0)

    def shuffle(self) -> None:
        """Shuffles the cards in this deck"""
        print(self.cards)
