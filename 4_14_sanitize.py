import unicodedata
import string

def shave_marks(txt):
    """去掉全部变音符号"""
    norm_txt = unicodedata.normalize('NFD', txt) # 把所有字符分解成基字符和组合记号
    shaved = ''.join(c for c in norm_txt
                    if not unicodedata.combining(c)) # 过滤掉所有组合记号
    return unicodedata.normalize('NFC', shaved) # 重组所有字符

order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(shave_marks(order))

Greek = 'Zέφupoς, Zéfiro'
print(shave_marks(Greek))

def shave_marks_latin(txt):
    """把拉丁基字符中所有的变音符号删除"""
    norm_txt = unicodedata.normalize('NFD', txt) # 把所有字符分解成基字符和组合记号
    latin_base = False
    keepers = []
    for c in norm_txt:
        if unicodedata.combining(c) and latin_base: # 基字符为拉丁字母时，跳过组合记号
            continue
        keepers.append(c) # 否则，保存当前字符
        # 如果不是组合字符，那就是新的基字符
        if not unicodedata.combining(c): # 检测新的基字符，判断是不是拉丁字母
            latin_base = c in string.ascii_letters
    shaved = ''.join(keepers)
    return unicodedata.normalize('NFC', shaved) # 重组所有字符

order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(shave_marks_latin(order))

Greek = 'Zέφupoς, Zéfiro'
print(shave_marks_latin(Greek))

single_map = str.maketrans(""",ƒ,,†ˆ‹‘’“”•––˜›""",  # 构建字符替换字符的映射表
                            """'f''*^<''""---~>""")

multi_map = str.maketrans({  # 构建字符替换字符串的映射表
    '€': '<euro>',
    '…': '...',
    #'OE': 'OE',
    '™': '(TM)',
    #'oe': 'oe',
    '‰': '<per mille>',
    '‡': '**',
})

multi_map.update(single_map) # 合并两个映射表

def dewinize(txt): # dewinize 函数不影响 ASCII 或 latin1 文本，只替换 Microsoft 在 cp1252 中为latin1 额外添加的字符
    """把Win1252符号替换成ASCII字符或序列"""
    return txt.translate(multi_map)

def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt)) # 调用 dewinize 函数，然后去掉变音符号
    no_marks = no_marks.replace('ß', 'ss')# 把德语 Eszett 替换成“ss”（这里没有使用大小写折叠，因为我们想保留大小写）
    return unicodedata.normalize('NFKC', no_marks) # 使用 NFKC 规范化形式把字符和与之兼容的码位组合起来

order = '“Herr Voß: • ½ cup of OEtker™ caffè latte • bowl of açaí.”'
print(dewinize(order))
print(asciize(order))