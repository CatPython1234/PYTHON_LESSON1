from tkinter import *

root = Tk()
root.title("GUt на Python")
root.geometry("500x300")

label1 = Label(text = "HELLO Python", fg = "#eee", bg= "#333")
label1.pack()

poetry = "hfrkrfrfr,\nhrwhwrhh;\nrhrghrghwr,\ngdvdvdivhi."
label2 = Label(text=poetry,justify=LEFT)
label2.place(relx=.2, rely=.3)

root.mainloop()