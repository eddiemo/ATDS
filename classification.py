def isReflexivity(M):
    flag = True
    n = len(M[0])
    for i in range(n):
        if M[i][i] != 1:
            flag = False
            break
    return flag

def isSymmetry(M):
    flag = True
    n = len(M[0])
    for i in range(0, n):
        for j in range(i, n):
            if M[i][j] != M[j][i]:
                flag = False
                break
    return flag

def isAntisymmetry(M):
    flag = True
    n = len(M[0])
    for i in range(0, n):
        for j in range(i, n):
            if i != j and M[i][j] + M[j][i] == 2:
                flag = False
                break
    return flag

def isTransitivity(M):
    flag = True
    n = len(M[0])
    for i in range(0, n):
        for j in range(0,n):
            for k in range(0, n):
                if M[i][j] == 1 and M[j][k] == 1 and M[i][k] != 1:
                    flag = False
                    break
    return flag

if __name__ == '__main__':
    print(u'Введите количество элементов множества')
    n = int(input())
    M = [0] * n
    for i in range(n):
        M[i] = [0] * n
    print(u'Введите отношение парами:')
    while True:
        vvod = input().split()
        if len(vvod) == 0:
            break
        M[int(vvod[0])][int(vvod[1])] = 1

    str = u'Свойства данного отношения: '
    if isReflexivity(M):
        str += u'рефлексивное, '
    else:
        str += u'нерефлексивное, '
    if isSymmetry(M):
        str += u'симметричное, '
    else:
        str += u'несимметричное, '
    if isAntisymmetry(M):
        str += u'антисимметричное, '
    else:
        str += u'неантисимметричное, '
    if isTransitivity(M):
        str += u'транзитивное.'
    else:
        str += u'нетранзитивное.'
    print(str)