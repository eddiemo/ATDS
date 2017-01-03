import math

def iscommutativitysum(new, m):
    for val1 in new:
        for val2 in new:
            if (val1 + val2) % m != (val2 + val1) % m:
                return False
    return True

def iscommutativitymul(new, m):
    for val1 in new:
        for val2 in new:
            if (val1 * val2) % m != (val2 * val1) % m:
                return False
    return True

def isassociativitymul(new, m):
    for val1 in new:
        for val2 in new:
            for val3 in new:
                if (val1 * ((val2 * val3) % m)) % m != (((val1 * val2) % m) * val3) % m:
                    return False
    return True

def isassociativitysum(new, m):
    for val1 in new:
        for val2 in new:
            for val3 in new:
                if (val1 + ((val2 + val3) % m)) % m != (((val1 + val2) % m) + val3) % m:
                    return False
    return True

def isdistributivity(new, m):
    for val1 in new:
        for val2 in new:
            for val3 in new:
                if (val1 * (val2 + val3)) % m != ((val1 * val2) + (val1 * val3)) % m \
                        or ((val2 + val3) * val1) % m != ((val2 * val1) + (val3 * val1)) % m:
                    return False
    return True

def existinv(new, m):
    null = findnull(new, m)
    if null == -1:
        return False
    for val in new:
        if not (null - val + m) % m in new:
            return False
    return True

def findnull(new, m):
    for val in new:
        check = True
        for elem in new:
            if (elem + val) % m != elem:
                check = False
                break
        if check:
            return val
    return -1

def findone(new, m):
    for val in new:
        check = True
        for elem in new:
            if (elem * val) % m != elem:
                check = False
                break
        if check:
            return val
    return -1

def closedoperations(new, m):
    newset = set(new)
    for val1 in new:
        for val2 in new:
            if (not (val1 + val2) % m in newset) or (not (val1 * val2) % m in newset):
                return False
    return True

def buildring(m):
    ring = []
    for i in range(m):
        ring.append(i)
    return ring

def buildsubring(init, m):
    oldset = set()
    newset = set()
    for i in range(len(init)):
        oldset.add(init[i])
    while True:
        while len(oldset) != len(newset):
            newset.update(oldset)
            for val1 in newset:
                for val2 in newset:
                    oldset.add((val1 + val2) % m)
                    oldset.add((val1 * val2) % m)
        check = True
        null = findnull(newset, m)
        one = findone(newset, m)
        if null == -1:
            null = 0
        if one == -1:
            one = 1
        if not null in newset:
            newset.add(null)
            check = False
        if not one in newset:
            newset.add(one)
            check = False

        if not check:
            continue

        helpset = set()
        helpset.update(newset)
        for elem in newset:
            if not ((m + null - elem) % m) in newset:
                helpset.add((m + null - elem) % m)
                check = False
        newset.update(helpset)
        if check:
            break
    new = list(newset)
    new.sort()
    return new

def buildideal(init, m):
    newset = set()
    oldset = set()
    for i in range(len(init)):
        oldset.add(init[i])
    while (len(oldset) != len(newset)):
        newset.update(oldset)
        for val1 in newset:
            for val2 in newset:
                oldset.add((val1 - val2) % m)
            for elem in range(m):
                oldset.add((val1 * elem) % m)
    new = list(newset)
    new.sort()
    return new

def closedidealopers(initset, m):
    for elem1 in initset:
        for elem2 in initset:
            if not (elem1 - elem2) % m in initset:
                return False
    for elem1 in initset:
        for elem2 in range(m):
            if not (elem1 * elem2) % m in initset:
                return False
    return True

def buildfactorring(idealset, m):
    used = [False] * m
    factorring = {}
    for val1 in range(m):
        if not used[val1]:
            for val2 in range(m):
                if (val1 - val2) % m in idealset:
                    if factorring.get(val1) == None:
                        factorring[val1] = []
                    factorring[val1].append(val2)
                    used[val2] = True
            used[val1] = True
    return factorring

def f(x, m):
    return x % m

def buildtesthomomorf(z, m):
    zn = []
    for x in z:
        zn.append(f(x, m))
    for x in zn:
        for y in zn:
            if f(x + y, m) != (f(x, m) + f(y, m)) % m:
                return zn, False
            if f(x * y, m) != (f(x, m) * f(y, m)) % m:
                return zn, False
    return zn, True

if __name__ == '__main__':
    m = int(input('Модуль = '))
    initsplt = input('Порождающее множество: ').split()
    init = []
    for i in range(len(initsplt)):
        init.append(int(initsplt[i]))

    subring = buildsubring(init, m)
    print('Подкольцо: ' + str(subring)[1:-1])
    if closedoperations(subring, m):
        print('Множество замкнуто относительно умножения и сложения')
    else:
        print('Множество не замкнуто относительно умножения и сложения')
    if iscommutativitysum(subring, m):
        print('Тест на коммутативность по сложению пройден')
    else:
        print('Тест на коммутативность по сложению не пройден')
    if isassociativitysum(subring, m):
        print('Тест на ассоциативность по сложению пройден')
    else:
        print('Тест на ассоциативность по сложению не пройден')
    x = findnull(subring, m)
    if x != -1:
        print('Нейтральный элемент по сложению найден, это ' + str(x))
    else:
        print('Нейтральный элемент по сложению не найден')
    if existinv(subring, m):
        print('Все элементы имеют противоположные')
    else:
        print('Один из элементов не имеет противоположного')

    if iscommutativitymul(subring, m):
        print('Тест на коммутативность по умножению пройден')
    else:
        print('Тест на коммутативность по умножению не пройден')
    if isassociativitymul(subring, m):
        print('Тест на ассоциативность по умножению пройден')
    else:
        print('Тест на ассоциативность по умножению не пройден')
    x = findone(subring, m)
    if x != -1:
        print('Нейтральный элемент по умножению найден, это ' + str(x))
    else:
        print('Нейтральный элемент по сложению не найден')
    if isdistributivity(subring, m):
        print('Тест на дистрибутивность пройден')
    else:
        print('Тест на дистрибутивность не пройден')
    print()

    print('Таблица Кэли для сложения:')
    s = '+'
    for elem in subring:
        s += '\t' + str(elem)
    print(s)
    for elem1 in subring:
        s = str(elem1)
        for elem2 in subring:
            s += '\t' + str((elem1 + elem2) % m)
        print(s)
    print('Таблица Кэли для умножения:')
    s = '*'
    for elem in subring:
        s += '\t' + str(elem)
    print(s)
    for elem1 in subring:
        s = str(elem1)
        for elem2 in subring:
            s += '\t' + str((elem1 * elem2) % m)
        print(s)
    print()

    ideal = buildideal(init, m)
    idealset = set(ideal)
    print('Идеал: ' + str(ideal)[1:-1])
    if closedoperations(idealset, m):
        print('Операции в идеале замкнуты')
    else:
        print('Операции в идеале не замкнуты')
    print()

    print('Таблица Кэли для сложения:')
    s = '+'
    for elem in ideal:
        s += '\t' + str(elem)
    print(s)
    for elem1 in ideal:
        s = str(elem1)
        for elem2 in ideal:
            s += '\t' + str((elem1 + elem2) % m)
        print(s)
    print('Таблица Кэли для умножения:')
    s = '*'
    for elem in ideal:
        s += '\t' + str(elem)
    print(s)
    for elem1 in ideal:
        s = str(elem1)
        for elem2 in ideal:
            s += '\t' + str((elem1 * elem2) % m)
        print(s)
    print()

    factorring = buildfactorring(idealset, m)
    print('Фактор-кольцо: ' + str(factorring)[1:-1])

    print('Гомоморфизм: ')
    initsplt = input('Множество целых чисел: ').split()
    z = []
    for i in range(len(initsplt)):
        z.append(int(initsplt[i]))
    s = 'Z:\t'
    for elem in z:
        s += '\t' + str(elem)
    print(s)
    zn, flag = buildtesthomomorf(z, m)
    if flag:
        s = 'f(Z):'
        for elem in zn:
            s += '\t' + str(elem)
        print(s)
        print('Свойства гомоморфизма выполняются')
    else:
        print("Не удалось построить гомоморфизм")