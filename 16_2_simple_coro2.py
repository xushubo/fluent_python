def simple_coro2(a):
    print('-> Startd: a =', a)
    b = yield a
    print('-> Received: b =', b)
    c = yield a + b
    print('-> Received: c =', c)

my_coro2 = simple_coro2(14)
from inspect import getgeneratorstate
print(getgeneratorstate(my_coro2))
next(my_coro2)
print(getgeneratorstate(my_coro2))
my_coro2.send(28)
my_coro2.send(99)