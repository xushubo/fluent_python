from array import array
import reprlib
import math
import numbers
import functools
import operator
import itertools

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other) and 
                all(a == b for a, b in zip(self, other)))

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self)
        if isinstance(index, slice):
            return cls(self._components[index])
        elif isinstance(index, numbers.Integral):
            return self._components[index]
        else:
            msg = '{.__name__} indices must be integers'
            raise TypeError(msg.format(cls))

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self)
        if len(name) == 1:
            pos = cls.shortcut_names.find(name)
            if 0 <= pos < len(self._components):
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, name))

    def angle(self, n):
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles())
            outer_fmt = '<{}>'
        else:
            coords = self
            outer_fmt = '({})'
        components = (format(c, fmt_spec) for c in coords)
        return outer_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

print(repr(Vector([3.1, 4.2])))
print(repr(Vector((3, 4, 5))))
print(repr(Vector(range(10))))

v1 = Vector([3, 4])
x, y = v1
print(x, y)
print(repr(v1))
v1_clone = eval(repr(v1))
print(v1 == v1_clone)
print(v1)
octets = bytes(v1)
print(octets)
print(abs(v1))
print(bool(v1), bool(Vector([0, 0])))

v1 = Vector([3, 4, 5])
x, y, z = v1
print(x, y, z)
print(repr(v1))
v1_clone = eval(repr(v1))
print(v1_clone == v1)
print(v1)
print(abs(v1))
print(bool(v1), bool(Vector([0, 0, 0])))

v7 = Vector(range(7))
print(repr(v7))
print(abs(v7))

v2 = Vector([3, 4, 5])
v2_clone = Vector.frombytes(bytes(v2))
print(repr(v2_clone))
print(v2 == v2_clone)

v1 = Vector([3, 4, 5])
print(len(v1))
print(v1[0], v1[len(v1)-1], v1[-1])

v7 = Vector(range(7))
print(v7[-1])
print(repr(v7[1:4]))
print(repr(v7[-1:]))
# v7[1,2]

v7 = Vector(range(10))
print(v7.x, v7.y, v7.z, v7.t)
# v7.k
v3 = Vector(range(3))
# v3.t
# v3.spam

v1 = Vector([3, 4])
v2 = Vector([3.1, 4.2])
v3 = Vector([3, 4, 5])
v6 = Vector(range(6))
print(hash(v1), hash(v3), hash(v6))

import sys
print(hash(v2) == (384307168202284039 if sys.maxsize > 2**32 else 357915986))

v1 = Vector([3, 4])
print(format(v1))
print(format(v1, '.2f'))
print(format(v1, '.3e'))

v3 = Vector([3, 4, 5])
print(format(v3))
print(format(Vector(range(7))))

print(format(Vector([1, 1]), 'h'))
print(format(Vector([1, 1]), '.3eh'))
print(format(Vector([1, 1]), '0.5fh'))
print(format(Vector([1, 1, 1]), 'h'))
print(format(Vector([2, 2, 2]), '.3eh'))
print(format(Vector([0, 0, 0]), '0.5fh'))
print(format(Vector([-1, -1, -1, -1]), 'h'))
print(format(Vector([0, 1, 0, 0]), '0.5fh'))