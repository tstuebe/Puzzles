# A very easy tube shaped puzzle. Solvable in three moves.

# Import
from tkinter import *
import tkinter as tk
from random import randint
 
# Format Window
window = tk.Tk()
window.title('Tube Puzzle')
window.geometry('600x250')

# Define Rings
ring = [0, 1, 2, 3, 4, 5, 6]
ring_len = len(ring)

# Define Ring Indices
i = 0
j = 0
k = 0
l = 0
m = 0

# Format Columns
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)

# Prepare Output Interface
l0 = tk.Label(window, bg='white', width=10, text=ring[i])
l0.grid(column=1, row=1, pady=15)

l1 = tk.Label(window, bg='white', width=10, text=ring[j])
l1.grid(column=2, row=1, pady=15)

l2 = tk.Label(window, bg='white', width=10, text=ring[k])
l2.grid(column=3, row=1, pady=15)

l3 = tk.Label(window, bg='white', width=10, text=ring[l])
l3.grid(column=4, row=1, pady=15)

l4 = tk.Label(window, bg='white', width=10, text=ring[m])
l4.grid(column=5, row=1, pady=15)

# Define Functions
def twist_up():
    # get indices
    global i
    global j
    global k
    global l
    global m

    # twist first, middle, and last column clockwise
    if (var1.get() == 0):
        i = (i + 1) % ring_len
        k = (k + 1) % ring_len
        m = (m + 1) % ring_len
        l0.config(text=ring[i])
        l2.config(text=ring[k])
        l4.config(text=ring[m])

    #twist first three columns clockwise
    elif (var1.get() == 1):
        i = (i + 1) % ring_len
        j = (j + 1) % ring_len
        k = (k + 1) % ring_len
        l0.config(text=ring[i])
        l1.config(text=ring[j])
        l2.config(text=ring[k])

    # twist last three columns clockwise
    elif (var1.get() == 2):
        k = (k + 1) % ring_len
        l = (l + 1) % ring_len
        m = (m + 1) % ring_len
        l2.config(text=ring[k])
        l3.config(text=ring[l])
        l4.config(text=ring[m])

def twist_down():
    # get indices
    global i
    global j
    global k
    global l
    global m

    # twist first, middle, and last column counter-clockwise
    if (var1.get() == 0):
        i = (i - 1) % ring_len
        k = (k - 1) % ring_len
        m = (m - 1) % ring_len
        l0.config(text=ring[i])
        l2.config(text=ring[k])
        l4.config(text=ring[m])

    #twist first three columns counter-clockwise
    elif (var1.get() == 1):
        i = (i - 1) % ring_len
        j = (j - 1) % ring_len
        k = (k - 1) % ring_len
        l0.config(text=ring[i])
        l1.config(text=ring[j])
        l2.config(text=ring[k])
        
    # twist last three columns counter-clockwise
    elif (var1.get() == 2):
        k = (k - 1) % ring_len
        l = (l - 1) % ring_len
        m = (m - 1) % ring_len
        l2.config(text=ring[k])
        l3.config(text=ring[l])
        l4.config(text=ring[m])

def reset():
    # set indices
    global i
    global j
    global k
    global l
    global m
    i = 0
    j = 0
    k = 0
    l = 0
    m = 0

    # print
    l0.config(text=ring[i])
    l1.config(text=ring[j])
    l2.config(text=ring[k])
    l3.config(text=ring[l])
    l4.config(text=ring[m])
    

def scramble():
    # get indices
    global i
    global j
    global k
    global l
    global m
    i = randint(0, ring_len - 1)
    j = randint(0, ring_len - 1)
    k = randint(0, ring_len - 1)
    # l must be defined later
    m = randint(0, ring_len - 1)

    # set indice l
    l = (ring_len + i + (m - k) - 1 ) % ring_len

    # print
    l0.config(text=ring[i])
    l1.config(text=ring[j])
    l2.config(text=ring[k])
    l3.config(text=ring[l])
    l4.config(text=ring[m])
 
# Define Radio Button Variable
var1 = tk.IntVar()

# Prepare User Input Interface
c1 = tk.Radiobutton(window, text='Free', variable=var1, value=0)
c1.grid(column=2, row=2, sticky=tk.W)

c2 = tk.Radiobutton(window, text='Button 1', variable=var1, value=1)
c2.grid(column=2, row=3, sticky=tk.W)

c3 = tk.Radiobutton(window, text='Button 2', variable=var1, value=2)
c3.grid(column=2, row=4, sticky=tk.W)

b1 = tk.Button(window, text='up', height=1, command=twist_up)
b1.grid(column=4, row=2)

b2 = tk.Button(window, text='down', height=1, command=twist_down)
b2.grid(column=4, row=3)

b3 = tk.Button(window, text='scramble', height=1, command=scramble)
b3.grid(column=2, row=6, sticky=tk.W, pady=15)

b4 = tk.Button(window, text='reset', height=1, command=reset)
b4.grid(column=2, row=7, sticky=tk.W)

# Begin Loop
window.mainloop()