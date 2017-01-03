def isAssociativity(matr):
    n = len(matr[0])
    flag = True
    for y in range(n):
        for x in range(n):
            for z in range(n):
                if table[d[table[x][y]]][z] != table[x][d[table[y][z]]]:
                    flag = False
                    break
            if not flag:
                break
        if not flag:
            break
    return flag

def isCommutativity(matr):
    n = len(matr[0])
    flag = True
    for x in range(n):
        for y in range(x + 1, n):
            if table[x][y] != table[y][x]:
                flag = False
                break
        if not flag:
            break
    return flag

if __name__ == '__main__':
    dict_str = input("Введите множество элементов: ").split()
    n = len(dict_str)
    d = {}
    for i in range(n):
        d[dict_str[i]] = i
    table = []
    print("Введите таблицу Кэли:")
    for i in range(n):
        table.append(input().split())
    a = isAssociativity(table)
    c = isCommutativity(table)
    if a and c:
        print("Операция ассоциативна и коммутативна")
    elif a and not c:
        print("Операция ассоциативна и не коммутативна")
    elif not a and c:
        print("Операция не ассоциативна и коммутативна")
    else:
        print("Операция не ассоциативна и не коммутативна")