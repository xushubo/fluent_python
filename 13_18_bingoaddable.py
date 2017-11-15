import itertools
import random
from tombola import Tombola

class BingoCage(Tombola):

    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self):
        self.pick()

class AddableBingoCage(BingoCage):

    def __add__(self, other):
        if isinstance(other, Tombola):
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable other.inspect()
        else:
            try:
                other_iterable = iter(other)
            except TypeError:
                self_cls = type(self).__name__
                msg = 'right operand in += must be {!r} or an iterable'
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable)
        return self


vowels = 'AEIOU'
globe = AddableBingoCage(vowels)
print(globe.inspect())
print(globe.pick() in vowels)
print(len(globe.inspect()))
globe2 = AddableBingoCage('XYZ')
globe3 = globe + globe2
print(len(globe3.inspect()))
globe_orig = globe
print(len(globe_orig.inspect()))
globe += globe2
print(len(globe.inspect()))
globe += ['M', 'N']
print(len(globe.inspect()))
print(globe is globe_orig)
globe += 1
