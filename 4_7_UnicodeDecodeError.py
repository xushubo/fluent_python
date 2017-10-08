octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
try:
    octets.decode('utf-8')
except UnicodeDecodeError:
    print('UnicodeDecodeError')
print(octets.decode('utf-8', errors='replace'))

str1 = 'Montréal'
print(str1.encode('utf-8').decode('utf-8'))