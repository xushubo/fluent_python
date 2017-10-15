class C: pass
obj = C()
def func(): pass
print(sorted(set(dir(func)) - set(dir(obj))))