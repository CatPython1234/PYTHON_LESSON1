#Домашнее задание:
# Составить "Анкету авантюриста". Анкета состоит из 8 полей и 4 Chekbutton.
# В проект добавить 2 кнопки. 1 кнопка вставляет значения для примера.
# Вторая кнопка очищает все поля.

from tkinter import *
from tkinter import messagebox

def Clean_up():
    name_entry.delete(0, END)
    surname_entery.delete(0, END)
    middlename_entry.delete(0, END)
    city_entry.delete(0, END)
    post_entery.delete(0, END)
    mail_entery.delete(0, END)
    house_entery.delete(0, END)
    flat_entery.delete(0, END)

def Registration():
    messagebox.showinfo("Анкета для приёма на работу", surname_entery.get() + " " + name_entry.get() + " " +
                        middlename_entry.get() + " " + " " + city_entry.get()
                        + " " + " " + post_entery.get() + " " + " " + mail_entery.get()
                        + " " + " " + house_entery.get() + " " + flat_entery.get() )

root = Tk()
root.title("Оконное приложение на Python")
root.geometry("400x500")

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Женат", variable=python_lang,
                                 onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.grid(row=0, column=2, sticky=W)

javascript_lang = IntVar()
javascript_checkbutton = Checkbutton(text="Не женат", variable=javascript_lang,
                                     onvalue=1, offvalue=0, padx=15, pady=10)
javascript_checkbutton.grid(row=1, column=2, sticky=W)


surname_label = Label(text="Введите имя:")
name_label = Label(text="Введите фамилию:").grid(row=1, column=0, sticky="w")
middlename_label = Label(text="Введите отчество")
city_label = Label(text="Введите город")
post_label = Label(text="Введите должность")
mail_label = Label(text="Введите почту")
house_label = Label(text="Введите дом")
flat_label = Label(text="Введите № квартиры")
surname_label.grid(row=0, column = 0, sticky = "w")

middlename_label.grid(row=2, column=0, sticky="w")
city_label.grid(row=3, column=0, sticky="w")
post_label.grid(row=4, column=0, sticky="w")
mail_label.grid(row=5, column=0, sticky="w")
house_label.grid(row=6, column=0, sticky="w")
flat_label.grid(row=7, column=0, sticky="w")


name_entry = Entry()
surname_entery = Entry()
middlename_entry = Entry()
city_entry = Entry()
post_entery = Entry()
mail_entery = Entry()
house_entery = Entry()
flat_entery = Entry()
name_entry.grid(row=0, column = 1, padx=5, pady=5)
surname_entery.grid(row=1, column=1, padx=5, pady=5)
middlename_entry.grid(row=2, column=1, padx=5, pady=5)
city_entry.grid(row=3, column=1, padx=5, pady=5)
post_entery.grid(row=4, column=1, padx=5, pady=5)
mail_entery.grid(row=5, column=1, padx=5, pady=5)
house_entery.grid(row=6, column=1, padx=5, pady=5)
flat_entery.grid(row=7, column=1, padx=5, pady=5)

displey_button = Button(text="Регистрация", command=Registration)
clear_button = Button(text="Отчистить", command=Clean_up)
displey_button.grid(row=11, column=0, padx=6, pady=6, sticky="e")
clear_button.grid(row=11, column=1, padx=6, pady=6, sticky="e")

root.mainloop()