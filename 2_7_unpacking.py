lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates #元组拆包
print(latitude, longitude)

a, b = 1, 3
a, b = b, a
print(a, b)

print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))

import os
_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')
print(filename)

a, b, *rest = range(5)
print(rest)
a, *rest, b = range(5)
print(rest)
*rest, a, b = range(5)
print(rest)
a, b, *rest = range(3)
print(rest)
a, b, *rest = range(2)
print(rest)