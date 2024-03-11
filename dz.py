from tkinter import *
cliks = 0
def clik_button():
    global cliks
    cliks += 1
    buttonText.set("Cliks {}".format(cliks))

root = Tk()
root.title('HELLO')
root.geometry('40x300')



buttonText = StringVar
buttonText.set("Cliks {}".format(cliks))
btn = Button(textvariable=buttonText, background="#555",foreground="#ccc",padx="20", pady="8", font="16",
             )
root.mainloop()
btn.pack()
