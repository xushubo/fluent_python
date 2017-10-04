'''新建一个 Latin-1 字符集合，该集合里的每个字符的 Unicode 名字里都有“SIGN”这个单词'''
from unicodedata import name
sign = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(sign)

s = {1, 2, 3, 4}
z = {3, 4, 5, 6}
print(s.symmetric_difference(z))
print(s ^ z)
print(z ^ s)