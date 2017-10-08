s1 = 'café'
s2 = 'cafe\u0301'
print(s1, s2)
print(len(s1), len(s2))
print(s1 == s2)

from unicodedata import normalize, name

s1 = 'café' # 把"e"和重音符组合在一起
s2 = 'cafe\u0301' # 分解成"e"和重音符
print(len(s1), len(s2))
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))
print(normalize('NFC', s1) == normalize('NFC', s2))
print(normalize('NFD', s1) == normalize('NFD', s2))

ohm = '\u2126'
print(name(ohm))
ohm_c = normalize('NFC', ohm)
print(name(ohm_c))
print(ohm == ohm_c)
print(normalize('NFC', ohm) == normalize('NFC', ohm_c))

half = '½'
print(normalize('NFKC', half))
four_squared = '4²'
print(normalize('NFKC', four_squared))
micro = 'µ'
micro_kc = normalize('NFKC', micro)
print(micro, micro_kc)
print(ord(micro), ord(micro_kc))
print(name(micro), name(micro_kc))

micro = 'µ'
print(name(micro))
micro_cf = micro.casefold()
print(name(micro_cf))
print(micro, micro_cf)

eszett = 'ß'
print(name(eszett))
eszett_cf = eszett.casefold()
print(eszett, eszett_cf)