import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])
class FrenchDeck(object):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card)
print(beer_card.rank)
print(beer_card.suit)
print('------------------------')

deck = FrenchDeck()
print(len(deck))
print('------------------------')

print(deck[0], deck[-1])
print('------------------------')

print(choice(deck))
print(choice(deck))
print(choice(deck))
print('------------------------')

print(deck[:3])
print(deck[12::13])
print('------------------------')

for card in deck:
    if card.suit == 'diamonds':
        break
    print(card)
print('------------------------')

for card in reversed(deck):
    if card.suit == 'clubs':
        break
    print(card)
print('------------------------')

print(Card('7', 'hearts') in deck)
print(Card('K', 'hearts') in deck)
print('------------------------')

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
    if spades_high(card) == 13:
        break

