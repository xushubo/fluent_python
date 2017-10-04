from dis import dis
dis('{1}')
dis('set([1])')

needles = {1, 2, 3, 4, 5}
haystack = {3, 4, 5, 6, 7}
found = len(set(needles) & set(haystack))
print(found)
found = len(set(needles).intersection(haystack))
print(found)