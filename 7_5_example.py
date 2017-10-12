def f1(a):
    print(a)
    print(b)
try:
    f1(3)
except NameError:
    print("NameError: name 'b' is not defined")

b = 6
def f2(a):
    print(a)
    print(b)
    b = 9

try:
    f2(6)
except UnboundLocalError:
    print("UnboundLocalError: local variable 'b' referenced before assignment")

def f3(a):
    print(a)
    print(b)
    global b
    b = 9
    print(b)
f3(3)

def f4(a):
    global b
    print(a)
    print(b)

f4(3)

from dis import dis

dis(f1)
print('-----------------------------------------')
dis(f2)