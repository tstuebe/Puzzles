from tkinter import *
import tkinter as tk
 

window = tk.Tk()
window.title('My Window')
window.geometry('600x150')

ring0 = [0, 1, 2, 3, 4, 5, 6]
ring1 = [0, 1, 2, 3, 4, 5, 6]
ring2 = [0, 1, 2, 3, 4, 5, 6]
ring3 = [0, 1, 2, 3, 4, 5, 6]
ring4 = [0, 1, 2, 3, 4, 5, 6]

i = 0
j = 0
k = 0
l = 0
m = 0

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)
window.columnconfigure(4, weight=1)
window.columnconfigure(5, weight=1)
window.columnconfigure(6, weight=1)

l0 = tk.Label(window, bg='white', width=10, text=ring0[i])
l0.grid(column=1, row=0)

l1 = tk.Label(window, bg='white', width=10, text=ring1[j])
l1.grid(column=2, row=0)

l2 = tk.Label(window, bg='white', width=10, text=ring2[k])
l2.grid(column=3, row=0)

l3 = tk.Label(window, bg='white', width=10, text=ring3[l])
l3.grid(column=4, row=0)

l4 = tk.Label(window, bg='white', width=10, text=ring4[m])
l4.grid(column=5, row=0)

def twist_up():
    global i
    global j
    global k
    global l
    global m
    if (var1.get() == 0):
        i = (i + 1) % 7
        k = (k + 1) % 7
        m = (m + 1) % 7
        l0.config(text=ring0[i])
        l2.config(text=ring2[k])
        l4.config(text=ring4[m])
    elif (var1.get() == 1):
        i = (i + 1) % 7
        j = (j + 1) % 7
        k = (k + 1) % 7
        l0.config(text=ring0[i])
        l1.config(text=ring1[j])
        l2.config(text=ring2[k])
    elif (var1.get() == 2):
        k = (k + 1) % 7
        l = (l + 1) % 7
        m = (m + 1) % 7
        l2.config(text=ring2[k])
        l3.config(text=ring3[l])
        l4.config(text=ring4[m])

def twist_down():
    global i
    global j
    global k
    global l
    global m
    if (var1.get() == 0):
        i = (i - 1) % 7
        k = (k - 1) % 7
        m = (m - 1) % 7
        l0.config(text=ring0[i])
        l2.config(text=ring2[k])
        l4.config(text=ring4[m])
    elif (var1.get() == 1):
        i = (i - 1) % 7
        j = (j - 1) % 7
        k = (k - 1) % 7
        l0.config(text=ring0[i])
        l1.config(text=ring1[j])
        l2.config(text=ring2[k])
    elif (var1.get() == 2):
        k = (k - 1) % 7
        l = (l - 1) % 7
        m = (m - 1) % 7
        l2.config(text=ring2[k])
        l3.config(text=ring3[l])
        l4.config(text=ring4[m])
 
var1 = tk.IntVar()

c1 = tk.Radiobutton(window, text='Free', variable=var1, value=0)
c1.grid(column=2, row=1, sticky=tk.W)

c2 = tk.Radiobutton(window, text='Button 1', variable=var1, value=1)
c2.grid(column=2, row=2, sticky=tk.W)

c3 = tk.Radiobutton(window, text='Button 2', variable=var1, value=2)
c3.grid(column=2, row=3, sticky=tk.W)

b1 = tk.Button(window, text='up', height=1, command=twist_up)
b1.grid(column=4, row=2)

b2 = tk.Button(window, text='down', height=1, command=twist_down)
b2.grid(column=4, row=3)
 
window.mainloop()