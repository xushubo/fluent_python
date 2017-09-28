t = (1, 2, [30, 40])
try:
    t[2] += [50, 60]
    # t[2].extend([50, 60])
except:
    pass
print(t)