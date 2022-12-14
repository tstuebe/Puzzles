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

cases = [0, 1, 2, 3, 4, 5, 6, 7, 8]

x = 4
y = 7


def up():
    global x
    global y
    if y < 0:
        y = y - 1
        player.grid(column = x, row = y)
    elif y == 0:
        print('You Win!')

def down():
    print('down')

def left():
    print('left')

def right():
    print('right')


l11 = tk.Label(window, bg='white', width=5, height=1, text='')
l12 = tk.Label(window, bg='white', width=5, height=1, text='')
l13 = tk.Label(window, bg='white', width=5, height=1, text='')
l14 = tk.Label(window, bg='white', width=5, height=1, text='')
l15 = tk.Label(window, bg='white', width=5, height=1, text='')
l16 = tk.Label(window, bg='white', width=5, height=1, text='')
l17 = tk.Label(window, bg='white', width=5, height=1, text='')

l21 = tk.Label(window, bg='white', width=5, height=1, text='')
l22 = tk.Label(window, bg='white', width=5, height=1, text='')
l23 = tk.Label(window, bg='white', width=5, height=1, text='')
l24 = tk.Label(window, bg='white', width=5, height=1, text='')
l25 = tk.Label(window, bg='white', width=5, height=1, text='')
l26 = tk.Label(window, bg='white', width=5, height=1, text='')
l27 = tk.Label(window, bg='white', width=5, height=1, text='')

l31 = tk.Label(window, bg='white', width=5, height=1, text='')
l32 = tk.Label(window, bg='white', width=5, height=1, text='')
l33 = tk.Label(window, bg='white', width=5, height=1, text='')
l34 = tk.Label(window, bg='white', width=5, height=1, text='')
l35 = tk.Label(window, bg='white', width=5, height=1, text='')
l36 = tk.Label(window, bg='white', width=5, height=1, text='')
l37 = tk.Label(window, bg='white', width=5, height=1, text='')

l41 = tk.Label(window, bg='white', width=5, height=1, text='')
l42 = tk.Label(window, bg='white', width=5, height=1, text='')
l43 = tk.Label(window, bg='white', width=5, height=1, text='')
l44 = tk.Label(window, bg='white', width=5, height=1, text='')
l45 = tk.Label(window, bg='white', width=5, height=1, text='')
l46 = tk.Label(window, bg='white', width=5, height=1, text='')
l47 = tk.Label(window, bg='white', width=5, height=1, text='')

l51 = tk.Label(window, bg='white', width=5, height=1, text='')
l52 = tk.Label(window, bg='white', width=5, height=1, text='')
l53 = tk.Label(window, bg='white', width=5, height=1, text='')
l54 = tk.Label(window, bg='white', width=5, height=1, text='')
l55 = tk.Label(window, bg='white', width=5, height=1, text='')
l56 = tk.Label(window, bg='white', width=5, height=1, text='')
l57 = tk.Label(window, bg='white', width=5, height=1, text='')

l61 = tk.Label(window, bg='white', width=5, height=1, text='')
l62 = tk.Label(window, bg='white', width=5, height=1, text='')
l63 = tk.Label(window, bg='white', width=5, height=1, text='')
l64 = tk.Label(window, bg='white', width=5, height=1, text='')
l65 = tk.Label(window, bg='white', width=5, height=1, text='')
l66 = tk.Label(window, bg='white', width=5, height=1, text='')
l67 = tk.Label(window, bg='white', width=5, height=1, text='')

l71 = tk.Label(window, bg='white', width=5, height=1, text='')
l72 = tk.Label(window, bg='white', width=5, height=1, text='')
l73 = tk.Label(window, bg='white', width=5, height=1, text='')
l74 = tk.Label(window, bg='white', width=5, height=1, text='')
l75 = tk.Label(window, bg='white', width=5, height=1, text='')
l76 = tk.Label(window, bg='white', width=5, height=1, text='')
l77 = tk.Label(window, bg='white', width=5, height=1, text='')

player = tk.Label(window, bg='white', width=5, height=1, text='o')

b1 = tk.Button(window, text='<', height=1, command=left)
b2 = tk.Button(window, text='v', height=1, command=down)
b3 = tk.Button(window, text='^', height=1, command=up)
b4 = tk.Button(window, text='>', height=1, command=right)


l11.grid(column = 1, row = 1)
l12.grid(column = 1, row = 2)
l13.grid(column = 1, row = 3)
l14.grid(column = 1, row = 4)
l15.grid(column = 1, row = 5)
l16.grid(column = 1, row = 6)
l17.grid(column = 1, row = 7)

l21.grid(column = 2, row = 1)
l22.grid(column = 2, row = 2)
l23.grid(column = 2, row = 3)
l24.grid(column = 2, row = 4)
l25.grid(column = 2, row = 5)
l26.grid(column = 2, row = 6)
l27.grid(column = 2, row = 7)

l31.grid(column = 3, row = 1)
l32.grid(column = 3, row = 2)
l33.grid(column = 3, row = 3)
l34.grid(column = 3, row = 4)
l35.grid(column = 3, row = 5)
l36.grid(column = 3, row = 6)
l37.grid(column = 3, row = 7)

l41.grid(column = 4, row = 1)
l42.grid(column = 4, row = 2)
l43.grid(column = 4, row = 3)
l44.grid(column = 4, row = 4)
l45.grid(column = 4, row = 5)
l46.grid(column = 4, row = 6)
l47.grid(column = 4, row = 7)

l51.grid(column = 5, row = 1)
l52.grid(column = 5, row = 2)
l53.grid(column = 5, row = 3)
l54.grid(column = 5, row = 4)
l55.grid(column = 5, row = 5)
l56.grid(column = 5, row = 6)
l57.grid(column = 5, row = 7)

l61.grid(column = 6, row = 1)
l62.grid(column = 6, row = 2)
l63.grid(column = 6, row = 3)
l64.grid(column = 6, row = 4)
l65.grid(column = 6, row = 5)
l66.grid(column = 6, row = 6)
l67.grid(column = 6, row = 7)

l71.grid(column = 7, row = 1)
l72.grid(column = 7, row = 2)
l73.grid(column = 7, row = 3)
l74.grid(column = 7, row = 4)
l75.grid(column = 7, row = 5)
l76.grid(column = 7, row = 6)
l77.grid(column = 7, row = 7)

player.grid(column = x, row = y)

b1.grid(column = 4, row = 8)
b2.grid(column = 5, row = 8)
b3.grid(column = 6, row = 8)
b4.grid(column = 7, row = 8)



window.mainloop()