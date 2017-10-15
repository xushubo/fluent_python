from operator import mul
from functools import partial
from unicodedata import normalize, name

triple = partial(mul, 3)
print(triple(7))

print(list(map(triple, range(1, 10))))

nfc = partial(normalize, 'NFC')
s1 = 'café'
s2 = 'cafe\u0301'
s3 = '\u0301'
print(name(s3))
print(s1 == s2)
print(nfc(s1) == nfc(s2))