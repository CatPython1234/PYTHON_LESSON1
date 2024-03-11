from tkinter import *
clik = 0
def my_text():
    global clik
    clik += 1
    label.config(text=clik)


root = Tk()
root.title("HELLO")
root.geometry("400x500")


button = Button(text="Нажми на меня",
             background='#555',
             foreground='#eee',
             pady='22',
             padx='22',
             font='16',
                command=my_text
             )

label = Label(text="TEXT", fg="#eee", bg="#444")
label.pack()


button.pack()
root.mainloop()