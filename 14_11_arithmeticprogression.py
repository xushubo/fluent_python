class ArithmeticProgression:

    def __init__(self, begin, step, end=None):
        self.begin = begin
        self.step = step
        self.end = end #None -> 无穷数列

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0
        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

ap = ArithmeticProgression(0, 1, 3)
print(list(ap))
ap = ArithmeticProgression(1, .5, 3)
print(list(ap))
ap = ArithmeticProgression(0, 1/3, 1)
print(list(ap))

from fractions import Fraction
ap = ArithmeticProgression(0, Fraction(1, 3), 1)
print(list(ap))

from decimal import Decimal
ap = ArithmeticProgression(0, Decimal('.1'), .3)
print(list(ap))