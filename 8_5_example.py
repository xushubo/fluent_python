t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])
print(t1 == t2)
print(id(t1))
t1[-1].append(99)
print(t1)
print(id(t1))
print(t1 == t2)

l1 = [3, [55, 44], (7, 8, 9)]
l2 = list(l1)
print(l2)
print(l2 == l1)
print(l2 is l1)