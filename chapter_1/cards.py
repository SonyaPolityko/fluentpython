from typing import NamedTuple
from enum import Enum
from random import choice

class NumberCard(Enum):
    MIN_CARDS_52 = 2 # младшая 2, если в колоде 52 карты
    MIN_CARDS_36 = 6 # младшая 6, если в колоде 36 карт
    MAX__CARDS = 10 # cтаршая карта 10, без учета 
    JQKA = 'JQKA' # валет, дама, король, туз
    


class Card(NamedTuple):
    rank: int | str
    suit: str


class Deck:
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self, is_full: bool = False):
        """
        Args:
            is_full (bool, optional): При True количество карт 52. Дефолтное False -> 36 карт в колоде.
        """
        self._is_full = is_full
        self._deck: list[Card] = []
        self._ranks: list[int | str]  = []

    
    def init_deck(self) -> None:
        """ Инициализация колоды"""
        if self._is_full:
            self._ranks = [value for value in range(NumberCard.MIN_CARDS_52.value, NumberCard.MAX__CARDS.value + 1)] + list(NumberCard.JQKA.value)
            self._deck = [Card(rank, suit) for suit in self.suits for rank in self._ranks]
        else:
            self._ranks = [value for value in range(NumberCard.MIN_CARDS_36.value, NumberCard.MAX__CARDS.value + 1)] + list(NumberCard.JQKA.value)
            self._deck = [Card(rank, suit) for suit in self.suits for rank in self._ranks]

    @property
    def deck(self) -> list[Card]:
        """
        Returns:
            list[Card]: Возврат колоды (список объектов класса Card)
        """
        return self._deck
    
    def __repr__(self):
        return f'{self.__class__.__name__}(is_fullish={self._is_full!r})'
    

    def __len__(self) -> int:
        return len(self._deck)
    

    def __getitem__(self, position: int) -> Card:
        return self._deck[position]


def main():
    deck_full = Deck(is_full=True) 
    deck_full.init_deck()
    print(len(deck_full))
    print(deck_full[13])
    print(choice(deck_full))
    deck_36 = Deck()
    deck_36.init_deck()
    print(len(deck_36))
    print(deck_36[13])
    print(choice(deck_36))



if __name__ == '__main__':
    main()






    