from tkinter import *

root = Tk()
root.title("GUt на Python")
root.geometry("500x300")


btn1 = Button(text="Нажми на меня", background="#555",foreground="#ccc",padx="20", pady="8", font="16",)
btn1.pack(fill = Y, side = LEFT)

root.mainloop()