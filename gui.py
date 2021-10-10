# /usr/bin/python3
# coding:utf-8
# @Author:prq
# @Time:2021/10/10 16:56

from game_gui import Game
import tkinter

'''
建立主界面
'''
window = tkinter.Tk()
window.title('2048')
window.geometry('500x500')
'''
确定size及输入框的位置
'''
tkinter.Label(window, text="size:", font=('Arial', 14)).place(x=10, y=12)
var_size = tkinter.IntVar()
var_size.set(4)
tkinter.Entry(window, textvariable=var_size, font=('Arial', 14)).place(x=50, y=10, width=40)
G = Game(0)
size = 0
score = tkinter.IntVar()


def close():
    window.quit()


def begin():
    global size, G
    size = var_size.get()
    G = Game(size)
    G.random_num()
    for i in range(size):
        for j in range(size):
            tkinter.Label(window, text=G.matrix[i][j]).grid(row=i, column=j, padx=40, pady=40, ipadx=10, ipady=10)
    score.set(G.score())
    tkinter.Label(window, text="score:", font=('Arial', 14)).place(x=250, y=12)
    tkinter.Label(window, textvariable=score, font=('Arial', 14)).place(x=300, y=12)
    tkinter.Button(window, text="关闭", command=close).place(x=350, y=12)


def up():
    # global size, G
    G.up()
    if not G.random_num():
        close()
    for i in range(size):
        for j in range(size):
            tkinter.Label(window, text=G.matrix[i][j]).grid(row=i, column=j, padx=40, pady=40, ipadx=10, ipady=10)
    score.set(G.score())


def down():
    # global size, G
    G.down()
    if not G.random_num():
        close()
    for i in range(size):
        for j in range(size):
            tkinter.Label(window, text=G.matrix[i][j]).grid(row=i, column=j, padx=40, pady=40, ipadx=10, ipady=10)
    score.set(G.score())


def left():
    # global size, G
    G.left()
    if not G.random_num():
        close()
    for i in range(size):
        for j in range(size):
            tkinter.Label(window, text=G.matrix[i][j]).grid(row=i, column=j, padx=40, pady=40, ipadx=10, ipady=10)
    score.set(G.score())


def right():
    # global size, G
    G.right()
    if not G.random_num():
        close()
    for i in range(size):
        for j in range(size):
            tkinter.Label(window, text=G.matrix[i][j]).grid(row=i, column=j, padx=40, pady=40, ipadx=10, ipady=10)
    score.set(G.score())


tkinter.Button(window, text="开始游戏", font=('Arial', 14), command=begin).place(x=120, y=14)

'''
定义上下左右的位置
'''
tkinter.Button(window, text="up", command=up).place(y=480, x=50, width=50)
tkinter.Button(window, text="down", command=down).place(y=480, x=150, width=50)
tkinter.Button(window, text="left", command=left).place(y=480, x=250, width=50)
tkinter.Button(window, text="right", command=right).place(y=480, x=350, width=50)

window.mainloop()
