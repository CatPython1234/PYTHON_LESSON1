from tkinter import *
from tkinter import messagebox

def clear():
    name_entry.delete(0, END)
    surname_entery.delete(0,END)

def displey():
    messagebox.showinfo("GUI Python", name_entry.get() + " " + surname_entery.get())

root = Tk()
root.title("GUI Python")
root.geometry("300x400")


name_label = Label(text="First name:")
name_label = Label(text="First name:")
surname_label = Label(text="Second name:")
name_label.grid(row=0, column = 0, sticky = "w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry()
surname_entery = Entry()
name_entry.grid(row=0, column = 1, padx=5, pady=5)
surname_entery.grid(row=1, column=1, padx=5, pady=5)

name_entry.insert(0, "Tom")
surname_entery.insert(0,"Soyer")


displey_button = Button(text="Display", command=displey)
clear_button = Button(text="Clear", command=clear)
displey_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()