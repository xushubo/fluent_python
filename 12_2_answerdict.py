class AnswerDict(dict):
    def __getitem__(self, key):
        return 42

ad = AnswerDict(a='foo')
print(ad['a'])

d = {}
d.update(ad)
print(d['a'])
print(d)