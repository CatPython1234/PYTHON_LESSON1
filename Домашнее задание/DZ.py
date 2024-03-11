from tkinter import *
from tkinter import messagebox
def Register():
    messagebox.showinfo("Python", name_entry.get() + " " + surname_entry.get() +
                        " " + middle_name_entry.get() + " " + city_entry.get() + " " +
                        post_entery.get() + " " + mail_entery.get() + " " + house_entery.get() + " " +
                        flat_entery.get())
def Clear():
    name_entry.delete(0,END)
    surname_entry.delete(0,END)
    middle_name_entry.delete(0,END)
    city_entry.delete(0,END)
    post_entery.delete(0,END)
    mail_entery.delete(0,END)
    house_entery.delete(0,END)
    flat_entery.delete(0,END)

def open_window():
    listbox=Toplevel(root1)
    listbox.title("Hello Python")

    def clear_listbox():
        language_listbox.delete(0, END)

    def add_to_listbox():
        new_language = language_entry.get()
        language_listbox.insert(END, new_language)
        language_entry.delete(0, END)

    language_entry = Entry(listbox, width=40)
    language_entry.grid(column=0, row=0, padx=6, pady=6)

    add_button = Button(listbox, text="Add", command=add_to_listbox)
    add_button.grid(column=1, row=0, padx=6, pady=6)

    language_listbox = Listbox(listbox)
    language_listbox.grid(row=1, column=0, columnspan=2, sticky=W + E, padx=5, pady=5)

    clear_button = Button(listbox, text="Clear", command=clear_listbox)
    clear_button.grid(row=2, column=0, padx=5, pady=5, sticky="e")





root1 = Tk()
root1.title("Hello")
root1.geometry("400x500")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Женат", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=2, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="Не женат", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=2, sticky=W)

nl=Label(text="Имя").grid(row=0,column=0,sticky="w")
sl=Label(text="Фамилия").grid(row=1,column=0,sticky="w")
pl=Label(text="Отчество").grid(row=2,column=0,sticky="w")
cl = Label(text="Введите город").grid(row=3,column=0,sticky="w")
pl = Label(text="Введите должность").grid(row=4,column=0,sticky="w")
ml = Label(text="Введите почту").grid(row=5,column=0,sticky="w")
hl = Label(text="Введите дом").grid(row=6,column=0,sticky="w")
fl = Label(text="Введите № квартиры").grid(row=7,column=0,sticky="w")

name_entry=Entry()
name_entry.grid(row=0,column=1,padx=5,pady=5)
surname_entry=Entry()
surname_entry.grid(row=1,column=1,padx=5,pady=5)
middle_name_entry=Entry()
middle_name_entry.grid(row=2,column=1,padx=5,pady=5)
city_entry = Entry()
city_entry.grid(row=3,column=1,padx=5,pady=5)
post_entery = Entry()
post_entery.grid(row=4,column=1,padx=5,pady=5)
mail_entery = Entry()
mail_entery.grid(row=5,column=1,padx=5,pady=5)
house_entery = Entry()
house_entery.grid(row=6,column=1,padx=5,pady=5)
flat_entery = Entry()
flat_entery.grid(row=7,column=1,padx=5,pady=5)

but1=Button(text="Регистрация",command=Register).grid(row=8,column=0,padx=5,pady=5,sticky=S)
but2=Button(text="Отчистить",command=Clear).grid(row=9,column=0,padx=5,pady=5,sticky=S)


open_listbox_button = Button(root1, text="Open Listbox Window", command=open_window).grid(row=10,column=0,padx=5,pady=5)
open_listbox_button1= Button(root1, text="Open Radiobutton", ).grid(row=11,column=0,padx=5,pady=5)



root1.mainloop()