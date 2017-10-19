t1 = (1, 2, 3)
t2 = tuple(t1)
print(t2 is t1)
t3 = t1[:]
print(t3 is t1)

t4 = (1, 2, 3)
print(t1 is t4)

s1 = 'ABC'
s2 = 'ABC'
print(s1 is s2)