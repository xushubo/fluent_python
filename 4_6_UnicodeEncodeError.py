city = 'São Paulo'
print(city.encode('utf-8'))
print(city.encode('utf-16'))
print(city.encode('iso8859_1'))
try:
    city.encode('cp437')
except UnicodeEncodeError:
    print('UnicodeEncodeError')

print(city.encode('cp437', errors='ignore'))
print(city.encode('cp437', errors='replace'))
print(city.encode('cp437', errors='xmlcharrefreplace'))