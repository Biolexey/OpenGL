from tkinter import *


W, H = 400, 400

def pressed(event):
    global oldX, oldY
    oldX, oldY = event.x, event.y

def dragged(event): #カーソルを動かすたびに古い座標を更新して線を引く
    global canvas, oldX, oldY
    x, y = event.x, event.y
    canvas.create_line((oldX, oldY), (x, y))
    oldX, oldY = x, y

def delete(event):  #全消去関数(任意)
    global canvas
    canvas.create_rectangle((2, 2), (W-1, H-1), outline="", fill="#ffffff")

def eraser(event):  #消しゴム関数(任意)
    global canvas, oldX, oldY
    x, y = event.x, event.y
    canvas.create_line((oldX, oldY), (x, y), width=20, fill="#ffffff")
    oldX, oldY = x, y

def main():
    global canvas

    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed)
    canvas.bind("<B1-Motion>", dragged)
    canvas.bind("<Button-2>", delete)
    canvas.bind("<Button-3>", pressed)
    canvas.bind("<B3-Motion>", eraser)
    root.mainloop()

if __name__ == "__main__":
    main()