from tkinter import *
def change_text():
    label.config(text="Новый текст для Label,45455,45454")

root = Tk()
button = Button(root, text="Изменить текст", command=change_text)
button.pack()
label = Label(root, text="Текст для Label")
label.pack()
root.mainloop()