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

current_bg = [['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', '']]

current_fg = [['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', ''],
              ['', '', '', '', '']]

current_tx = [['', '', '', '', ''],
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

def get_vars():
    for i in range(5):
        for j in range(5):
            current_bg[i][j] = spot[i % size][j].cget('bg')
            current_fg[i][j] = spot[i % size][j].cget('fg')
            current_tx[i][j] = spot[i % size][j].cget('text')

def move_up(a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            spot[i][j].config(bg = current_bg[(i + 1) % size][j], 
                              fg = current_fg[(i + 1) % size][j],
                              text = current_tx[(i + 1) % size][j])

def move_dn(a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            spot[i][j].config(bg = current_bg[(i - 1) % size][j], 
                              fg = current_fg[(i - 1) % size][j],
                              text = current_tx[(i - 1) % size][j])

def move_lf(a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            spot[i][j].config(bg = current_bg[i][(j + 1) % size], 
                              fg = current_fg[i][(j + 1) % size],
                              text = current_tx[i][(j + 1) % size])

def move_rt(a, b, c, d):
    for i in range(a, b):
        for j in range(c, d):
            spot[i][j].config(bg = current_bg[i][(j - 1) % size], 
                              fg = current_fg[i][(j - 1) % size],
                              text = current_tx[i][(j - 1) % size])

def upleft():
    get_vars()
    move_up(0, 5, 0, 3)

def upcenter():
    get_vars()
    move_up(0, 5, 1, 4)

def upright():
    get_vars()
    move_up(0, 5, 2, 5)

def downleft():
    get_vars()
    move_dn(0, 5, 0, 3)

def downcenter():
    get_vars()
    move_dn(0, 5, 1, 4)

def downright():
    get_vars()
    move_dn(0, 5, 2, 5)

def leftup():
    get_vars()
    move_lf(0, 3, 0, 5)

def leftcenter():
    get_vars()
    move_lf(1, 4, 0, 5)

def leftdown():
    get_vars()
    move_lf(2, 5, 0, 5)

def rightup():
    get_vars()
    move_rt(0, 3, 0, 5)

def rightcenter():
    get_vars()
    move_rt(1, 4, 0, 5)

def rightdown():
    get_vars()
    move_rt(2, 5, 0, 5)
    
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