from tkinter import *
def change_text():
    label.config(text="Новый текст для Label,35354,534535")
root = Tk()
root.title('HELLO')
root.geometry('900x800')
button = Button(root, text="Изменить текст",background='#555', foreground='#eee',pady='22',padx='22',font='16',
command=change_text)
button.pack()
label = Label(root, text="Текст для Label")
label.pack()
root.mainloop()