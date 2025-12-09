from enum import Enum
from random import choice
from typing import NamedTuple


class NumberCard(Enum):
    MIN_CARDS_52 = 2  # младшая 2, если в колоде 52 карты
    MIN_CARDS_36 = 6  # младшая 6, если в колоде 36 карт
    MAX__CARDS = 10  # cтаршая карта 10, без учета
    JQKA = "JQKA"  # валет, дама, король, туз


class Card(NamedTuple):
    rank: int | str
    suit: str


class Deck:
    suits = "spades diamonds clubs hearts".split()

    def __init__(self, is_full: bool = False):
        """
        Args:
            is_full (bool, optional): При True количество карт 52. Дефолтное False -> 36 карт в колоде.
        """
        self._is_full = is_full
        self._deck: list[Card] = []
        self._ranks: list[int | str] = []

    def init_deck(self) -> None:
        """Инициализация колоды"""
        if self._is_full:
            self._ranks = [
                value
                for value in range(
                    NumberCard.MIN_CARDS_52.value, NumberCard.MAX__CARDS.value + 1
                )
            ] + list(NumberCard.JQKA.value)
            self._deck = [
                Card(rank, suit) for suit in self.suits for rank in self._ranks
            ]
        else:
            self._ranks = [
                value
                for value in range(
                    NumberCard.MIN_CARDS_36.value, NumberCard.MAX__CARDS.value + 1
                )
            ] + list(NumberCard.JQKA.value)
            self._deck = [
                Card(rank, suit) for suit in self.suits for rank in self._ranks
            ]

    @property
    def deck(self) -> list[Card]:
        """
        Returns:
            list[Card]: Возврат колоды (список объектов класса Card)
        """
        return self._deck

    def __repr__(self):
        return f"{self.__class__.__name__}(is_fullish={self._is_full!r})"

    def __len__(self) -> int:
        return len(self._deck)

    def __getitem__(self, position: int) -> Card:
        return self._deck[position]


def init_deck(decks: list[Deck]) -> None:
    """Инициализация колод из списка колод"""
    for deck in decks:
        deck.init_deck()


def print_card(decks: list[Deck], number_card: int) -> None:
    """Выдача карты под номером number_card из каждой колоды из спискa"""
    for deck in decks:
        print(deck[number_card])


def print_random_card(decks: list[Deck]) -> None:
    """Выдача случайной карты из каждой колоды из списка"""
    for deck in decks:
        print(choice(deck))


def print_deck_len(decks: list[Deck]) -> None:
    """Вывод длины каждой колоды из списка"""
    for deck in decks:
        print(len(deck))


def main():
    deck_full = Deck(is_full=True)
    deck_36 = Deck()
    decks = [deck_full, deck_36]
    init_deck(decks=decks)
    print_card(decks=decks, number_card=13)
    print_random_card(decks=decks)
    print_deck_len(decks=decks)


if __name__ == "__main__":
    main()
