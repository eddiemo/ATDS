from tkinter import *

n = 10
size = 600
root = Tk()
canvas = Canvas(root, width=size, height=size)
canvas.pack()
a = [[0,1,2], [3,4], [6], [5,7,8], [9]]
points = []
h = size / (len(a) + 1)
pos_y = size - h
for i in range(len(a)):
    w = size / (len(a[i]) + 1)
    pos_x = w
    p = []
    for j in range(len(a[i])):
        canvas.create_oval(pos_x - 3, pos_y - 3, pos_x + 3, pos_y + 3, fill = "black")
        pi = [pos_x, pos_y]
        p.append(pi)
        pos_x += w
    pos_y -= h
    points.append(p)

canvas.create_line(points[0][0][0], points[0][0][1], points[1][0][0], points[1][0][1], width = 2)

mainloop()