from inspect import signature

def clip(text, max_len=80):
    '''在max_len前面或后面的第一个空格处截断文本'''
    end = None
    if len(text) > max_len:
        space_before = text.rfind(' ', 0, max_len)
        if space_before >= 0:
            end = space_before
        else:
            spac_after = text.rfind(' ', max_len)
        if spac_after >= 0:
            end = spac_after
    if end is None:
        end = len(text)
    return text[:end].rstrip()

sig = signature(clip)
print(sig)

for name, param in sig.parameters.items():
    print(param.kind, ':', name, '=', param.default)