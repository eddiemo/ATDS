def Transponir(Ma):
    n = len(Ma[0])
    MT = [0] * n
    for i in range(n):
        MT[i] = [0] * n
    for i in range(n):
        for j in range(n):
            MT[j][i] = Ma[i][j]
    return MT

def reflZam(Ma):
    n = len(Ma[0])
    for i in range(n):
        Ma[i][i] = 1
    return Ma

def symZam(Ma):
    n = len(Ma[0])
    MT = Transponir(Ma)
    for i in range(n):
        for j in range(n):
            Ma[i][j] |= MT[i][j]
    return Ma

def tranZam(Ma):
    n = len(Ma[0])
    for k in range(n):
        for i in range(n):
            for j in range(n):
                Ma[i][j] = Ma[i][j] | (Ma[i][k] & Ma[k][j])
    return Ma

def equalZam(Ma):
    return tranZam(symZam(reflZam(Ma)))

def output(Ma):
    s = ''
    n = len(Ma[0])
    for i in range(n):
        for j in range(n):
            if Ma[i][j] == 1:
                s += '(' + str(i) + ', ' + str(j) + ')' + ', '
    return s[:-2]

if __name__ == '__main__':
    print(u'Введите количество элементов множества')
    n = int(input())
    M = [0] * n
    for i in range(n):
        M[i] = [0] * n
    print(u'Введите бинарное отношение парами:')
    while True:
        vvod = input().split()
        if len(vvod) == 0:
            break
        M[int(vvod[0])][int(vvod[1])] = 1
    M1 = [0] * n
    for i in range(n):
        M1[i] = [0] * n
    for i in range(n):
        for j in range(n):
            M1[i][j] = M[i][j]
    print('Рефлексивное замыкание: ' + output(reflZam(M)))
    for i in range(n):
        for j in range(n):
            M[i][j] = M1[i][j]
    print('Симметричное замыкание: ' + output(symZam(M)))
    for i in range(n):
        for j in range(n):
            M[i][j] = M1[i][j]
    print('Транзитивное замыкание: ' + output(tranZam(M)))
    for i in range(n):
        for j in range(n):
            M[i][j] = M1[i][j]
    print('Эквивалентное замыкание: ' + output(equalZam(M)))