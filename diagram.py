from tkinter.filedialog import *
import classification

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
    A = file.readline().split()
    n = int(len(A))
    M = [0] * n
    for i in range(n):
        M[i] = [0] * n
    for line in file:
        vvod = line.split()
        M[int(vvod[0])][int(vvod[1])] = 1

    if classification.isReflexivity(M) and classification.isAntisymmetry(M) and classification.isTransitivity(M):
        pass
    else:
        print("Данное отношение не является отношением порядка")
        sys.exit()

    for i in range(n):
        M[i][i] = 0

    a = set()
    check_a = set()
    lvl = []
    for k in range(n):
        lv = []
        for j in range(n):
            if j in check_a:
                continue
            sum = 0
            for i in range(n):
                if i in check_a:
                    continue
                sum += M[i][j]
            if sum == 0:
                lv.append(j)
                a.add(j)
        lvl.append(lv)
        check_a = a.copy()

    del_edges = []
    for i in range(0, n):
        for j in range(0, n):
            for k in range(0, n):
                if M[i][j] == 1 and M[j][k] == 1 and M[i][k] == 1:
                    a = [i, k]
                    del_edges.append(a)
    for edge in del_edges:
        M[edge[0]][edge[1]] = 0

    inv_lvl = [0] * n
    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            inv_lvl[lvl[i][j]] = j

    size = 600
    root = Tk()
    canvas = Canvas(root, width=size, height=size)
    canvas.pack()
    points = [0] * n
    h = size / (len(lvl) + 1)
    pos_y = size - h
    for i in range(len(lvl)):
        w = size / (len(lvl[i]) + 1)
        pos_x = w
        p = []
        for j in range(len(lvl[i])):
            canvas.create_oval(pos_x - 3, pos_y - 3, pos_x + 3, pos_y + 3, fill="black")
            a = [pos_x, pos_y]
            points[lvl[i][j]] = a
            pos_x += w
        pos_y -= h

    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                x0 = points[i][0]
                y0 = points[i][1]
                x1 = points[j][0]
                y1 = points[j][1]
                canvas.create_line(x0, y0, x1, y1, width = 2)

    for i in range(len(lvl)):
        for j in range(len(lvl[i])):
            canvas.create_text(points[lvl[i][j]][0] + 15, points[lvl[i][j]][1], text = str(A[lvl[i][j]]),
                               fill = "black", font=("Helvectica", "16"))

    if len(lvl[0]) == 1:
        print("Наименьшим и единственным минимальным элементом является элемент " + A[lvl[0][0]])
    elif len(lvl[0]) > 1:
        print("Наименьшего элемента не существует в данном множестве, минимальными являются элементы: " +
              str([int(A[i]) for i in lvl[0]])[1 : -1])
    st = []
    for i in range(n):
        sum = 0
        for j in range(n):
            sum += M[i][j]
        if sum == 0:
           st.append(i)
    l = len(st)
    if l == 1:
        print("Наибольшим и единственным максимальным элементом является элемент " + A[st[0]])
    elif l > 1:
        print("Наибольшего элемента не существует в данном множестве, максимальными являются элементы: " +
              str([int(A[i]) for i in st])[1 : -1])

    mainloop()