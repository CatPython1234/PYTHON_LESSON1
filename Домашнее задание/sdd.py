# Домашнее задание:
# 1)Создать холст
# 2)Создать круг
# 3)Добавить управление для перемещения круга на клавиши WASD
# 4)Добавить возможность изменения цвета круга при нажатии на кнопки (Z - первый цвет, X - второй цвет, C - третий цвет)
import tkinter as tk
def change_color(color):
    canvas.itemconfig(circle, fill=color)

def change_to_black(event):
    change_color("black")

def change_to_pink(event):
    change_color("pink")

def change_to_blue(event):
    change_color("blue")

def move(event):
    if event.keysym == 'w':
        canvas.move(circle, 0, -10)
    elif event.keysym == 's':
        canvas.move(circle, 0, 10)
    elif event.keysym == 'a':
        canvas.move(circle, -10, 0)
    elif event.keysym == 'd':
        canvas.move(circle, 10, 0)

root = tk.Tk()
root.title("GUE on PYTHON")
canvas=tk.Canvas(root,width=300,height=300)
canvas.pack()

circle=canvas.create_oval(20,20,50,50,outline="white",fill="blue")

root.bind("<KeyPress>", move)
root.bind("z", change_to_black)
root.bind("x", change_to_pink)
root.bind("c", change_to_blue)

root.mainloop()