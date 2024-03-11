import tkinter as tk
import time
def DrawKvadrat(x, y, l, color):
    canvas.create_line(x, y, x+l, y, fill=color)
    canvas.create_line(x+l, y, x+l, y+l, fill=color)
    canvas.create_line(x + l, y + l, x, y+l, fill=color)
    canvas.create_line(x, y+l, x, y, fill=color)

def moveRight(event):
    global x,y
    canvas.delete('all')
    x = x + 10
    DrawKvadrat(x,y,100,"blue")
    canvas.update()

def moveUp(event):
    global x,y
    canvas.delete('all')
    y = y - 10
    DrawKvadrat(x,y,100,"blue")
    canvas.update()

def moveDown(event):
    global x,y
    canvas.delete('all')
    y = y + 10
    DrawKvadrat(x,y,100,"blue")
    canvas.update()

def moveLeft(event):
    global x,y
    canvas.delete('all')
    x=x-10
    DrawKvadrat(x,y,100,"blue")
    canvas.update()

root = tk.Tk()
canvas=tk.Canvas(root,width=300,height=300)
canvas.pack()
x = 50
y = 100

root.bind("d", moveRight)
root.bind("a", moveLeft)
root.bind("w", moveUp)
root.bind("s", moveDown)
DrawKvadrat(x,y,100,"blue")

root.mainloop()