from tkinter import*
root = Tk()
root.title("Graphic program on Python")
root.geometry("400x300+500+250")
btn = Button(text="Hello",
             background="#555",
             foreground="#ccc",
             padx="50",
             pady="30",
             font="Arial 16")
btn.pack()
root.mainloop()