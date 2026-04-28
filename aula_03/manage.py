# MÓDULOS NATIVO PYTHON
# import random as rd
# from random import randint as rdint, random as rd

# from calculadora import *

# print(rdint(1, 15))
# print(rd())


# from tkinter import *
# from tkinter import ttk

# root = Tk()
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# root.mainloop()

# MODULOS COMPARTILHADOS

from tqdm import tqdm
import time


for x in tqdm( range(10) ):
    time.sleep(0.5)

