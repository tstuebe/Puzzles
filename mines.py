# Game loosely based on minesweeper

# Import
from tkinter import *
import tkinter as tk
from random import randint
 
# Format Window
window = tk.Tk()
window.title('Mines')
window.geometry('400x400')

# Format Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)
window.columnconfigure(7, weight=1)
window.columnconfigure(8, weight=1)

# Format Rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)
window.rowconfigure(8, weight=1)

x = 6
y = 3

cases = [0, 1, 2, 3, 4, 5, 6, 7, 8]

spot = [['l11', 'l12', 'l13', 'l14', 'l15', 'l16', 'l17'],
        ['l21', 'l22', 'l23', 'l24', 'l25', 'l26', 'l27'],
        ['l31', 'l32', 'l33', 'l34', 'l35', 'l36', 'l37'],
        ['l41', 'l42', 'l43', 'l44', 'l45', 'l46', 'l47'],
        ['l51', 'l52', 'l53', 'l54', 'l55', 'l56', 'l57'],
        ['l61', 'l62', 'l63', 'l64', 'l65', 'l66', 'l67'],
        ['l71', 'l72', 'l73', 'l74', 'l75', 'l76', 'l77']]

for i in range(0,7):
    for j in range(0,7):
        spot[i][j] = tk.Label(window, bg='white', width=5, height=1, text='')
        spot[i][j].grid(row = i + 1, column = j + 1)

spot[x][y] = tk.Label(window, bg='white', width=5, height=1, text='o')
spot[x][y].grid(row = x + 1, column = y + 1)

def reset():
    for i in range(0,7):
        for j in range(0,7):
            spot[i][j] = tk.Label(window, bg='white', width=5, height=1, text='')
            spot[i][j].grid(row = i, column = j)

def up():
    global x
    global y
    if x > 0:
        spot[x][y].config(text='')
        x = x - 1
        spot[x][y].config(text='o')
    elif x == 0:
        spot[x][y].config(text=':)')

def down():
    global x
    global y
    if x < 6:
        spot[x][y].config(text='')
        x = x + 1
        spot[x][y].config(text='o')
    elif x == 7:
        spot[x][y].config(text='o')

def left():
    global x
    global y
    if y > 0:
        spot[x][y].config(text='')
        y = y - 1
        spot[x][y].config(text='o')
    elif y == 0:
        spot[x][y].config(text='o')

def right():
    global x
    global y
    if y < 6:
        spot[x][y].config(text='')
        y = y + 1
        spot[x][y].config(text='o')
    elif y == 0:
        spot[x][y].config(text='o')

# player = tk.Label(window, bg='white', width=5, height=1, text='o')

b1 = tk.Button(window, text='<', height=1, command=left)
b2 = tk.Button(window, text='v', height=1, command=down)
b3 = tk.Button(window, text='^', height=1, command=up)
b4 = tk.Button(window, text='>', height=1, command=right)

# player.grid(row = x, column = y)

b1.grid(column = 4, row = 8)
b2.grid(column = 5, row = 8)
b3.grid(column = 6, row = 8)
b4.grid(column = 7, row = 8)



window.mainloop()