from tkinter import *

root = Tk()
root.title("GUt на Python")
root.geometry("500x300")

for r in range(5):
    for c in range(5):
        btn = Button(text="{}-{}".format(r,c))
        btn.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)

root.mainloop()