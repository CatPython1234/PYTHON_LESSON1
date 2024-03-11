from tkinter import *

def add():
    new_language = language_entery.get()
    language_listbox.insert(0, new_language)
def clear():
    language_listbox.delete(0, END)

root = Tk()
root.title("GUI on Python")

language_entery = Entry(width=40)
language_entery.grid(column=0, row=0, padx=6, pady=6)
add_button = Button(text="Add", command=add).grid(column=1,row=0,padx=6, pady=6)

language_listbox = Listbox()
language_listbox.grid(row=1, column=0, columnspan=2, sticky = W+E, padx=5, pady=5)

language_listbox.insert(END, "Python")
language_listbox.insert(END, "C#")

click = Button(text="Отчистить", command= clear)
click.grid(row=2, column=1, padx=5, pady=5, sticky="e")

root.mainloop()