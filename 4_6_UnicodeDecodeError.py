octets = b'Montr\xe9al'
print(octets.decode('cp1252'))
print(octets.decode('iso8859_7'))
print(octets.decode('koi8_r'))
try:
    octets.decode('utf-8')
except UnicodeDecodeError:
    print('UnicodeDecodeError')
print()