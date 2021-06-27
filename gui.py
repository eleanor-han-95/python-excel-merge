#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
import function


root = Tk()
root.title("small program")
root.geometry('300x300')

l1 = Label(root, text="please enter main excel:")
l1.pack()
xls_text = StringVar()
xls = Entry(root, textvariable = xls_text)
xls.pack()


l2 = Label(root, text="please enter secondary excel:")
l2.pack()
sheet_text = StringVar()
sheet = Entry(root, textvariable = sheet_text)

sheet.pack()


l3 = Label(root, text="please enter new excel name:")
l3.pack()
loop_text = StringVar()
loop = Entry(root, textvariable = loop_text)

loop.pack()






def on_click():
    x = xls_text.get()
    s = sheet_text.get()
    l = loop_text.get()
    function.main1(x,s,l)
    string = str("Done")
    #print("xls名：%s sheet名：%s 循环次数：%s 休眠时间：%s " %(x, s, l, sl))
    messagebox.showinfo(title='Message', message = string)

Button(root, text="Start", command = on_click).pack()

root.mainloop()
function.main1

