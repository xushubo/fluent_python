import re
import reprlib

RE_WORD = re.compile(r'\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

s = Sentence('"The time has come," the Walrus said,')
print(s)
for word in s:
    print(word, end=' ')
print('\n')
print(list(s))

s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(list(it))
print(list(s3))