import re

def lexical_analysis(str):
    s = str.replace(" ", "")
    print s
    arr = []
    may_sign = True
    sign = ""
    while True:
        if len(s) <= 0: break
        m = re.match("\*\*", s)
        if m:
            arr.append(m.group())
            may_sign = True
            s = s[2:]
        m = re.match("\*|\/|\%|\(|\)", s)
        if m:
            arr.append(m.group())
            may_sign = True
            s = s[1:]
        m = re.match("\+|\-", s)
        if m:
            if may_sign:
                sign = m.group()
                s = s[1:]
            else:
                arr.append(m.group())
                s = s[1:]
        m = re.match("\d+", s)
        if m:
            arr.append(sign + m.group())
            s = s[len(m.group()):]
            sign = ""
            may_sign = False

    return arr

print lexical_analysis("33 + 4 * 2 / (-1 - 55) ** -22 ** 3")