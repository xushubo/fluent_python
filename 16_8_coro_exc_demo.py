class DemoException(Exception):
    """为这次演示定义的异常类型。 """

def demo_exc_handling():
    print('-> coroutine started')
    while True:
        try:
            x = yield
        except DemoException:
            print('*** DemoException handled. Continuing...')
        else:
            print('-> coroutine received: {!r}'.format(x))
    raise RuntimeError('This line should never run.')

exc_coro = demo_exc_handling()
next(exc_coro)
exc_coro.send(11)
exc_coro.send(22)
exc_coro.throw(DemoException)
from inspect import getgeneratorstate
print(getgeneratorstate(exc_coro))
exc_coro.close()
print(getgeneratorstate(exc_coro))