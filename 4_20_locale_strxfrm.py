fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
print(sorted(fruits))

import locale
locale.setlocale(locale.LC_COLLATE, 'pt_BR.UTF-8') # locale.Error: unsupported locale setting
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=locale.strxfrm)
print(sorted_fruits)