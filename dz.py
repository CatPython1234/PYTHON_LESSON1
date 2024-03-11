from tkinter import *
from tkinter import messagebox

def displey_full_name():
    messagebox.showinfo("GUI Python", name.get() + " " + surname.get())

root = Tk()
root.title("GUI Python")
root.geometry("300x400")

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


python_lang = IntVar()
python_checkbutton = Checkbutton(text="Женат", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=2, column=0, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="Не женат", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=4, column=0, sticky=S)



root.mainloop()