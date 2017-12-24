def chain(*iterables):
    for it in iterables:
        yield from it

s = "abc"
t = tuple(range(3))
print(list(chain(s, t)))

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]

for x in flatten(items):
    print(x)