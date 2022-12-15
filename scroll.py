# Scroll 3 rows at a time

# Import
from tkinter import *
import tkinter as tk
from random import randint
 
# Format Window
window = tk.Tk()
window.title('Scroll')
window.geometry('420x400')
window.eval('tk::PlaceWindow . center')

# Format Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)

# Format Rows
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)
window.rowconfigure(5, weight=1)
window.rowconfigure(6, weight=1)
window.rowconfigure(7, weight=1)

spot = [['l11', 'l12', 'l13', 'l14', 'l15'],
        ['l21', 'l22', 'l23', 'l24', 'l25'],
        ['l31', 'l32', 'l33', 'l34', 'l35'],
        ['l41', 'l42', 'l43', 'l44', 'l45'],
        ['l51', 'l52', 'l53', 'l54', 'l55']]

current_color = [['', '', '', '', ''],
                 ['', '', '', '', ''],
                 ['', '', '', '', ''],
                 ['', '', '', '', ''],
                 ['', '', '', '', '']]

current_text = [['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', ''],
                ['', '', '', '', '']]

bg = ['white', 'red', 'green', 'blue', 'black']
fg = ['black', 'white', 'white', 'white', 'white'] 

size = len(bg)

for i in range(5):
    for j in range(5):
        spot[i][j] = tk.Label(window, width=5, height=1, text= str(j + 1))
        spot[i][j].grid(row = i + 1, column = j + 1)
        spot[i][j].config(bg = bg[i], fg = fg[i])

def upleft():
    for i in range(5):
        for j in range(5):
            current_text[i][j] = spot[i % size][j].cget('fg')
            current_color[i][j] = spot[i % size][j].cget('bg')
    for i in range(5):
        for j in range(3):
            spot[i][j].config(bg = current_color[(i + 1) % size][j], fg = current_text[(i + 1) % size][j])
    # print(current_color)

def upcenter():
    for i in range(5):
        for j in range(5):
            current_text[i][j] = spot[i % size][j].cget('fg')
            current_color[i][j] = spot[i % size][j].cget('bg')
    for i in range(5):
        for j in range(1,4):
            spot[i][j].config(bg = current_color[(i + 1) % size][j], fg = current_text[(i + 1) % size][j])

def upright():
    for i in range(5):
        for j in range(5):
            current_color[i][j] = spot[i % size][j].cget('bg')
            current_text[i][j] = spot[i % size][j].cget('fg')
    for i in range(5):
        for j in range(2,5):
            spot[i][j].config(bg = current_color[(i + 1) % size][j], fg = current_text[(i + 1) % size][j])

def downleft():
    print('downleft')

def downcenter():
    print('downcenter')

def downright():
    print('downright')

def leftup():
    print('leftup')

def leftcenter():
    print('leftcenter')

def leftdown():
    print('leftdown')

def rightup():
    print('rightup')

def rightcenter():
    print('rightcenter')

def rightdown():
    print('rightdown')

def scramble():
    print('scramble')

def reset():
    for i in range(5):
        for j in range(5):
            spot[i][j] = tk.Label(window, bg='white', width=5, height=1, text= str(j + 1))
            spot[i][j].grid(row = i + 1, column = j + 1)
            if i == 1:
                spot[i][j].config(bg = 'red', fg = 'white')
            elif i == 2:
                spot[i][j].config(bg = 'green', fg = 'white')
            elif i == 3:
                spot[i][j].config(bg = 'blue', fg = 'white')
            elif i == 4:
                spot[i][j].config(bg = 'black', fg = 'white')

upl = tk.Button(window, text = '^', command = upleft)
upl.grid(row = 0, column = 2)

upc = tk.Button(window, text = '^', command = upcenter)
upc.grid(row = 0, column = 3)

upr = tk.Button(window, text = '^', command = upright)
upr.grid(row = 0, column = 4)

downl = tk.Button(window, text = 'v', command = downleft)
downl.grid(row = 6, column = 2)

downc = tk.Button(window, text = 'v', command = downcenter)
downc.grid(row = 6, column = 3)

downr = tk.Button(window, text = 'v', command = downright)
downr.grid(row = 6, column = 4)

leftu = tk.Button(window, text = '<', command = leftup)
leftu.grid(row = 2, column = 0)

leftc = tk.Button(window, text = '<', command = leftcenter)
leftc.grid(row = 3, column = 0)

leftd = tk.Button(window, text = '<', command = leftdown)
leftd.grid(row = 4, column = 0)

rightu = tk.Button(window, text = '>', command = rightup)
rightu.grid(row = 2, column = 6)

rightc = tk.Button(window, text = '>', command = rightcenter)
rightc.grid(row = 3, column = 6)

rightd = tk.Button(window, text = '>', command = rightdown)
rightd.grid(row = 4, column = 6)

scramble = tk.Button(window, text='mix', width = 2, height=1, command=scramble)
scramble.grid(column=4, row=7, sticky=tk.W)

reset = tk.Button(window, text='reset', height=1, width = 2, command=reset)
reset.grid(column=5, row=7, sticky=tk.W)

window.mainloop()