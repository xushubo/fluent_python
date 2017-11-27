with open('chinadaily.txt') as fp:
    src = fp.read(60)

print(len(src))
print(fp)
print(fp.closed, fp.encoding)