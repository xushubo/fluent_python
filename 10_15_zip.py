a = (x for x in range(5))
b = (y for y in range(5, 10))
c = (z for z in range(10, 15))

for x, y, z in zip(a, b, c):
    print(x, y ,z)

print(list(zip(range(3), 'ABC')))
print(list(zip(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))

from itertools import zip_longest
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3])))
print(list(zip_longest(range(3), 'ABC', [0.0, 1.1, 2.2, 3.3], fillvalue=-1)))