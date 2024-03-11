from tkinter import *
from tkinter import messagebox

def my_massage():
    messagebox.showinfo("Hello Python", message.get())


root = Tk()
root.title("Python")
root.geometry("300x400")

message = StringVar()

message_entry = Entry(textvariable=message)
message_entry.place(relx=.5, rely=.1, ancho="c")

message_button = Button(text="Нажми на меня", command=my_massage)
message_button.place(relx=.5, rely=.1, anchor="c")

root.mainloop()
