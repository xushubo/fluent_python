from random import randrange

from tombola import Tombola

@Tombola.register
class TomboList(list):

    def pick(self):
        if self:
            positiion = randrange(len(self))
            return self.pop(position)
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(sorted(self))
# Tombola.register(TomboList)

print(issubclass(TomboList, Tombola))
t = TomboList(range(100))
print(isinstance(t, Tombola))
print(TomboList.__mro__)