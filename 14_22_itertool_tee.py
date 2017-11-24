import itertools
print(list(itertools.tee('ABC')))
print(list(itertools.tee('ABC', 3)))
g1, g2 = itertools.tee('ABC')
print(next(g1), next(g2))
print(next(g2))
print(list(g1))
print(list(g2))
print(list(zip(*itertools.tee('ABC'))))