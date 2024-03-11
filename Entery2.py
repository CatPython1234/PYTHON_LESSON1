from tkinter import *
from tkinter import messagebox

def displey_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

root = Tk()
root.title("GUI Python")

name = StringVar()
surname = StringVar()

name_label = Label(text="First name:")
surname_label = Label(text="Second name:")
name_label.grid(row=0, column = 0, sticky = "w")
surname_label.grid(row=1, column=0, sticky="w")

name_entry = Entry(textvariable=name)
surname_entery = Entry(textvariable=surname)
name_entry.grid(row=0, column = 1, padx=5, pady=5)
surname_entery.grid(row=1, column=1, padx=5, pady=5)

message_button = Button(text="Click me", command=displey_full_name)
message_button.grid(row=2, column=1, padx=5, pady=5,sticky="e")

root.mainloop()