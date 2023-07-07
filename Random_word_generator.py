#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 08:03:44 2023

@author: vishuddhimakeshwaran
"""

from tkinter import *
import random

root = Tk()
root.title("Random Word Generator")
root.geometry("400x500")

label1 = Label(root)

list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def gen(): 
    random1 = random.randint(0, len(list1) - 1)
    random2 = random.randint(0, len(list1) - 1)
    random3 = random.randint(0, len(list1) - 1)
    random4 = random.randint(0, len(list1) - 1)
    random5 = random.randint(0, len(list1) - 1)
    
    word = list1[random1] + list1[random2] + list1[random3] + list1[random4] + list1[random5]
    label1["text"] = word

button1 = Button(root, text = "Generate Random Word", command = gen)
button1.place(relx = 0.5, rely = 0.4, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.5, anchor = CENTER)
root.mainloop()
