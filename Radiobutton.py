from tkinter import *

languages = [("Python", 1), ("JavaScript", 2), ("Java", 3)]

def select():
    i = language.get()
    if i == 1: sel.config(text="Вы выбрали Python")
    elif i == 2: sel.config(text="Вы выбрали JavaScript")
    elif i == 3: sel.config(text="Вы выбрали Java")

root = Tk()
root.title("GUE on Python")
root.geometry("300x400")

header = Label(text="Choose a course", padx=15, pady=10)
header.grid(row=0,column=0,sticky=W)

language = IntVar()

row = 1
for txt, val in languages:
    Radiobutton(text=txt, value=val,variable=language, padx=15, pady=10, command=select)\
        .grid(row=row, sticky=W)
    row += 1

sel = Label(padx=15, pady=10)
sel.grid(row=row, sticky=W)

root.mainloop()