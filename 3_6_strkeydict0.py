class StrKeyDict0(dict):

    def __missing__(self, key):

        if isinstance(key, str): #如果不加这条语句，如果 str(k) 不是一个存在的键，代码就会陷入无限递归。
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        #此处不用key in self,是因为如果这么用回导致__contains__被递归调用
        return key in self.keys() or str(key) in self.keys()

    def __setitem__(self, key, item):
        self[key] = item

if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4', 'four')])
    print(d['2'])
    print(d[4])
    print(d.get('2'))
    print(d.get(4))
    print(2 in d)
    print('4' in d)