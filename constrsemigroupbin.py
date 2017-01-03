def mul(a, b):
    n = len(a[0])
    c = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] |= a[i][k] * b[k][j]
    return c

def adaptationtab(tab):
    n = len(table[0])
    for i in range(n):
        for j in range(n):
            word = tab[i][j]
            l = 0
            while l < len(word):
                cnt = 0
                k = l
                while word[k] == word[l]:
                    k += 1
                    cnt += 1
                    if k == len(word):
                        break
                if cnt > 1:
                    word = word.replace(word[l:k], word[l] + str(cnt))
                l = k
            tab[i][j] = word
    return tab

def adaptationstr(d):
    n = len(d)
    for j in range(n):
        word = d[j]
        l = 0
        while l < len(word):
            cnt = 0
            k = l
            while word[k] == word[l]:
                k += 1
                cnt += 1
                if k >= len(word):
                    break
            if cnt > 1:
                word = word.replace(word[l:k], word[l] + str(cnt))
            l = k
        d[j] = word
    return d

if __name__ == '__main__':
    n = int(input("Введите размерность алфавита: "))
    print("Введите размер матрицы бинарных отношений, саму матрицу и её обозначение:")
    matrixes = {}
    d = {}
    matrname = {}
    for i in range(n):
        k = int(input())
        matr = []
        for j in range(k):
            s = input().split()
            ss = []
            for l in range(len(s)):
                ss.append(int(s[l]))
            matr.append(ss)
        name = input()
        d[i] = name
        matrixes[i] = matr
        matrname[str(matr)] = name
    oldset = set()
    newset = set()
    for i in range(len(matrixes)):
        oldset.add(str(matrixes[i]))
    table = [[''] * n for i in range(n)]
    while True:
        newsetmas = []
        for i in range(n):
            for j in range(n):
                if table[i][j] != '':
                    continue
                elem = mul(matrixes[i], matrixes[j])
                if str(elem) not in oldset and str(elem) not in newset:
                    newsetmas.append(elem)
                    newset.add(str(elem))
                    table[i][j] = d[i] + d[j]
                    matrname[str(elem)] = table[i][j]
                elif str(elem) in oldset:
                    for x in oldset:
                        if x == str(elem):
                            table[i][j] = matrname[str(x)]
                else:
                    for x in newset:
                        if x == str(elem):
                            table[i][j] = matrname[str(x)]
        if len(newset) == 0:
            break
        else:
            i = n
            for elem in newsetmas:
                d[i] = matrname[str(elem)]
                matrixes[i] = elem
                i += 1
            oldset.update(newset)
            newset.clear()
            newn = len(oldset)
            newtable = [[''] * newn for i in range(newn)]
            for i in range(n):
                for j in range(n):
                    newtable[i][j] = table[i][j]
            table = newtable
            n = newn

    d = adaptationstr(d)
    table = adaptationtab(table)
    s = 'Получившаяся полугруппа: '
    for i in range(n):
        s += d[i] + ' '
    print(s + '\n')
    print('Таблица Кэли:')
    s = '\\'
    for i in range(n):
        s += '\t' + d[i]
    print(s)
    for i in range(n):
        s = d[i]
        for j in range(len(table[i])):
            s += '\t' + table[i][j]
        print(s)
    print('\n' + 'Элементы:')
    for i in range(n):
        print(d[i])
        for j in range(len(matrixes[i][0])):
            print(matrixes[i][j])