from tkinter import*
clicks = 0
def click_button():
    global clicks
    clicks +=1
    root.title("Clicks {}".format(clicks))

root = Tk()
root.title("GUI на Python")
root.geometry("500x350")

btn = Button(text="Нажми на меня", background="#555",foreground="#ccc",padx="20", pady="8", font="16",
             command=click_button)
btn.pack()

root.mainloop()