from tkinter.filedialog import *
import zamykaniya

def open_file():
    op = askopenfile()
    op = str(op)
    st = op.find('name=') + 6
    fin = op.find('mode') - 2
    path = op[st:fin]
    return path

if __name__ == '__main__':
    file_path = open_file()
    file = open(file_path, "r")
    n = int(file.readline())
    M = [0] * n
    for i in range(n):
        M[i] = [0] * n
    for line in file:
        vvod = line.split()
        M[int(vvod[0])][int(vvod[1])] = 1

    M1 = [0] * n
    for i in range(n):
        M1[i] = [0] * n
    for i in range(n):
        for j in range(n):
            M1[i][j] = M[i][j]
    print('Эквивалентное замыкание: ' + zamykaniya.output(zamykaniya.equalZam(M1)))

    a = [M1[i] for i in range(n)]
    aa = []
    strr = ''
    for elem in a:
        for i in range(len(elem)):
            strr += str(elem[i])
        aa.append(strr)
        strr = ''
    s = set()
    syst_pred = []
    for i in range(len(aa)):
        if aa[i] in s:
            continue
        else:
            s.add(aa[i])
            syst_pred.append(i)
    print("Система представителей: " + str(syst_pred))