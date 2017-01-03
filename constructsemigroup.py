def reduction(word, rules, rulesset):
    change = False
    while True:
        for tmpl in rulesset:
            if word.find(tmpl) != -1:
                word = word.replace(tmpl, rules[tmpl])
                change = True
                break
        if change:
            change = False
        else:
            break
    return word

if __name__ == '__main__':
    dict_str = input("Введите множество элементов: ").split()
    n = len(dict_str)
    d = {}
    for i in range(n):
        d[i] = dict_str[i]
    k = int(input("Введите количесво правил: "))
    print("Введите правила:")
    rules = {}
    rulesset = set()
    for i in range(k):
        xy = input().split()
        xy.remove('=')
        xy.sort(key=lambda c: (len(c), c[0]))
        rules[xy[1]] = xy[0]
        rulesset.add(xy[1])
    oldset = set()
    newset = set()
    table = [[''] * n for i in range(n)]
    for i in range(n):
        oldset.add(dict_str[i])
    while True:
        newsetmas = []
        for i in range(n):
            for j in range(n):
                if table[i][j] != '':
                    continue
                word = d[i] + d[j]
                if word not in oldset and word not in newset:
                    word = reduction(word, rules, rulesset)
                    if word not in oldset and word not in newset:
                        newset.add(word)
                        newsetmas.append(word)
                table[i][j] = word
        if len(newset) == 0:
            break
        else:
            i = n
            for elem in newsetmas:
                d[i] = elem
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
    s = 'Получившаяся полугруппа: '
    for i in range(len(d)):
        s += d[i] + ' '
    print(s + '\n')
    print('Таблица Кэли:')
    s = '\\'
    for i in range(len(d)):
        s += '\t\t' + d[i]
    print(s)
    for i in range(len(d)):
        s = d[i]
        for j in range(len(table[i])):
            s += '\t\t' + table[i][j]
        print(s)
