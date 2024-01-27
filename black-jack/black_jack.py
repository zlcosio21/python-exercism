"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

CARDS_VALUE = {
    "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7, "8": 8,
    "9": 9, "10": 10, "A": 1, "J": 10,
    "Q": 10, "K": 10
}


def value_of_card(card):
    """Determine the scoring value of a card."""

    value = CARDS_VALUE.get(card)

    return value


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""

    if value_of_card(card_one) > value_of_card(card_two):
        return card_one

    if value_of_card(card_one) < value_of_card(card_two):
        return card_two

    return card_one, card_two


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card."""

    if card_one == "A" or card_two == "A":
        return 1

    if value_of_card(card_one) + value_of_card(card_two) + 11 > 21:
        return 1

    return 11

def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""

    black_jack = "10JQK"

    return (card_one == "A" or card_two == "A") and (card_one in black_jack or card_two in black_jack)


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands"""

    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)

    return card_one == card_two


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet"""

    card_one = value_of_card(card_one)
    card_two = value_of_card(card_two)

    return 9 <= card_one + card_two <= 11