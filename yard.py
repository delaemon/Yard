import re

def left_associate(ope):
    if ope == "**":
        return False
    return True

def shunting_yard(arr):
    priority = {"*": 3, "/": 3, "%": 3, "+": 2, "-": 2, "**": 4}
    result = []
    stack = []
    for data in arr:
        if re.search("\d+|\+\d+|\-\d+", data):
            result.append(data)
        elif re.search("\(", data):
            stack.append(data)
        elif re.search("\)", data):
            exist = False
            while len(stack) != 0:
                a = stack.pop()
                if a == "(":
                    exist = True
                    break
                else:
                    result.append(a)
            if exist == False:
                print "parenthesis error"
                raise
        else:
            if len(stack) != 0 and stack[-1] != "(":
                if (left_associate(data) and priority[data] <= priority[stack[-1]]) \
                    or (left_associate(data) == False and priority[data] < priority[stack[-1]]):
                    result.append(stack.pop())
            stack.append(data)

    if len(stack) == 0:
        return result

    stack.reverse()
    for ope in stack:
        if ope == "(" or ope == ")":
            print "parenthesis error"
            raise
        result.append(ope)

    return result

def lexical_analysis(str):
    s = str.replace(" ", "")
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

def _calc(n1, n2, ope):
    if n1 == None or n2 == None:
        print "argument is not correct"
        raise
    a = float(n1)
    b = float(n2)
    if ope == "+" : return a + b
    if ope == "-" : return a - b
    if ope == "*" : return a * b
    if ope == "/" : return a / b
    if ope == "%" : return a % b
    if ope == "**": return a ** b
    print "operator is not correct"
    raise

def calculate(datas):
    num_stack = []
    for data in datas:
        if re.search("\d", data):
            num_stack.append(data)
        else:
            a = num_stack.pop()
            b = num_stack.pop()
            num_stack.append(_calc(b, a, data))
    if len(num_stack) != 1:
        print "argument is not correct"
        raise

    res = num_stack[0]
    if isinstance(res, float):
        return float(res)
    else:
        return int(res)

tests = [
    ["2+3*4", 14.0],
    ["2*3+4", 10.0],
    ["2*3*4", 24.0],
    ["(-5)", -5],
    ["(3+4)", 7.0],
    ["2*(3+4)", 14.0],
    ["2+(3-4)*5", -3.0],
    ["(3-4)*5", -5.0],
    ["(-3-4)*5", -35.0],
    ["(3-4)*(-5)", 5.0],
    ["(-3-4)*-5", 35.0],
    ["(-3-4)*-5-35", 0.0],
    ["(-3-4)*-5*2", 70.0],
    ["2*(3+4)", 14.0],
    ["2/3", 0.6666666666666666],
    ["(3*8)/(8-2)", 4.0],
    ["  3 + 4 * 2 / ( 1 - 5 ) ** 2 ** 3", 3.0001220703125],
]

for data, answer in tests:
    l = lexical_analysis(data)
    s = shunting_yard(l)
    res = calculate(s)
    print "data: {0}, res: {1}, answer: {2}, success: {3}".format(data, res, answer, res == answer)
