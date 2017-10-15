def factorial(n):
    '''return n'''
    return 1 if n < 2 else n * factorial(n-1)
print(list(map(factorial, range(6))))
print([factorial(n) for n in range(6)])

print(list(map(factorial, filter(lambda n: n % 2, range(6)))))
print([factorial(n) for n in range(6) if n % 2])