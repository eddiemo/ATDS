def polynomtostr(polynom, var):
    strpol = ''
    nulls = True
    for i in range(len(polynom)):
        if polynom[i] != 0:
            if i > 0 and not nulls:
                strpol += '+'
            if i == 0:
                strpol += str(polynom[i])
            elif i == 1:
                if polynom[i] > 1:
                    strpol += str(polynom[i]) + '*' + var
                else:
                    strpol += var
            else:
                if polynom[i] > 1:
                    strpol += str(polynom[i]) + '*' + var + '^' + str(i)
                else:
                    strpol += var + '^' + str(i)
            nulls = False
    if nulls:
        strpol += '0'
    return strpol

def nodnum(a, b):
    a0, a1, b0, b1 = 1, 0, 0, 1
    while b != 0:
        q, r = divmod(a, b)
        a, b = b, r
        a0, a1, b0, b1 = b0, b1, a0 - q * b0, a1 - q * b1
    return a0

def inverse(z, p):
    return ((nodnum(z,p) % p + p) % p)

def sum(a, b, m):
    new = []
    if len(a) >= len(b):
        new.extend(a)
        mlen = len(b)
    else:
        new.extend(b)
        mlen = len(a)
    for i in range(mlen):
        new[i] = (a[i] + b[i]) % m
    while len(new) > 0 and new[-1] == 0:
        new.pop()
    return new

def div(a, b, m):
    new = []
    new.extend(a)
    if len(a) < len(b) or nodnum(b[-1], m) != 1:
        return new

    newdeg = len(a) - 1
    divdeg = len(b) - 1
    inv = inverse(b[-1], m)
    while (len(new) >= len(b)):
        newdegg = newdeg - divdeg
        newi = (inv * new[newdeg]) % m
        for i in range(divdeg + 1):
            new[i + newdegg] = (new[i + newdegg] - b[i] * newi) % m
            if new[i + newdegg] < 0:
                new[i + newdegg] += m
        while len(new) > 1 and new[-1] == 0:
            new.pop()
        newdeg = len(new) - 1
        if new[-1] == 0:
            break
    while len(new) > 1 and new[-1] == 0:
        new.pop()
    return new

def mul(a, b, m):
    new = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            new[i + j] = (new[i + j] + (a[i] * b[j])) % m
    while len(new) > 1 and new[-1] == 0:
        new.pop()
    return new

def next(polynom, m):
    new = []
    new.extend(polynom)
    for i in range(len(new)):
        if new[i] == m - 1:
            new[i] = 0
        else:
            new[i] += 1
            break
    return new

def buildalgextention(mx, m):
    field = []
    n = len(mx) - 1
    cnt = pow(m, n)
    initpol = [0] * (n + 1)
    for i in range(cnt):
        initdeg = len(initpol) - 1
        field.append(initpol)
        initpol = next(initpol, m)
    return field


if __name__ == '__main__':
    m = int(input('Модуль: '))
    initsplt = input('Коэффициенты неприводимого многочлена: ').split()
    mx = []
    for i in range(len(initsplt)):
        mx.append(int(initsplt[i]) % m)
    print('Нормальный его вид:\nm(x) = ' + polynomtostr(mx, 'x'))
    field = buildalgextention(mx, m)
    print('Элементы алгебраического расширения поля:')
    maxlen = 0
    for pol in field:
        strpol = polynomtostr(pol, 'x')
        if len(strpol) > maxlen:
            maxlen = len(strpol)
        print(strpol)
    print()

    print('Таблица Кэли для сложения:')
    s = '+' + (maxlen - 1 + 3) * ' '
    for elem in field:
        ss = polynomtostr(elem, 'x')
        s += ss + (maxlen - len(ss) + 3) * ' '
    print(s)
    for elem1 in field:
        s = ''
        ss = polynomtostr(elem1, 'x')
        s += ss + (maxlen - len(ss) + 3) * ' '
        for elem2 in field:
            ss = polynomtostr(div(sum(elem1, elem2, m), mx, m), 'x')
            s += ss + (maxlen - len(ss) + 3) * ' '
        print(s)
    print('Таблица Кэли для умножения:')
    s = '*' + (maxlen - 1 + 3) * ' '
    for elem in field:
        ss = polynomtostr(elem, 'x')
        s += ss + (maxlen - len(ss) + 3) * ' '
    print(s)
    for elem1 in field:
        s = ''
        ss = polynomtostr(elem1, 'x')
        s += ss + (maxlen - len(ss) + 3) * ' '
        for elem2 in field:
            ss = polynomtostr(div(mul(elem1, elem2, m), mx, m), 'x')
            s += ss + (maxlen - len(ss) + 3) * ' '
        print(s)
