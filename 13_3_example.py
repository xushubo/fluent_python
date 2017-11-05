from collections import Counter

ct = Counter('abracadabra')
print(ct)
ct['r'] = -3
ct['d'] = 0
print(ct)
print(+ct)
print(ct == +ct)