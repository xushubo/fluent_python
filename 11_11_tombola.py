from tombola import Tombola

class Fake(Tombola):
    def pick(self):
        return 13

print(Fake)
Fake()