fruits = ['grape', 'raspberry', 'apple', 'banana']
print(sorted(fruits))
print(fruits)
print(sorted(fruits, reverse=True))
print('-------------------')

print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))
print(fruits)
print('-------------------')

fruits.sort()
print(fruits)