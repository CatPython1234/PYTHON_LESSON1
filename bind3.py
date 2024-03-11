from tkinter import *

def exitWin(event):
    root.destroy()

def inLabel(event):
    t = ent.get()
    lbl.configure(text=t)

def selectAll(event):
    root.after(10, select_All, event.widget)

def select_All(widget):
    widget.selection_range(0, END)
    widget.icursor(END)

def font1(event):
    lbl.configure(font="Verdana 12")

def font2(event):
    lbl['font2']="Times"


root = Tk()
ent = Entry(width=40)
ent.focus_set()
ent.pack()
lbl = Label(height=3, fg='red', bg='green', font="Verdana 24")
lbl.pack(fill=X)

lbl.bind('<Button-1>', font1)
ent.bind('<Return>', inLabel)
ent.bind('<Control-a>', selectAll)
ent.bind('<Control-q>', exitWin)

root.mainloop()