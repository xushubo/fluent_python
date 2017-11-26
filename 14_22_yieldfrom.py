def chain(*iterables):
    for iterable in iterables:
        for it in iterable:
            yield it


def chain1(*iterables):
    for iterable in iterables:
        yield from iterable

s = 'ABC'
t = tuple(range(3))

print(list(chain(s, t)))
print(list(chain1(s, t)))