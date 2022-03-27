from tkinter import *

R = 5

def pressed1(event):
    global canvas
    x, y = event.x, event.y     #event.x,yはイベント発生時のカーソルの座標
    canvas.create_rectangle((x-R, y-R), (x+R+1, y+R+1), outline="", fill="#ff0000")

def pressed2(event):
    global canvas
    x, y = event.x, event.y
    canvas.create_rectangle((x-R, y-R), (x+R+1, y+R+1), outline="", fill="#00ff00")

def pressed3(event):
    global canvas
    x, y = event.x, event.y
    canvas.create_rectangle((x-R, y-R), (x+R+1, y+R+1), outline="", fill="#0000ff")

def main():
    global canvas
    W, H = 400, 400
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#ffffff")
    canvas.pack()
    canvas.bind("<Button-1>", pressed1)
    canvas.bind("<Button-2>", pressed2)
    canvas.bind("<Button-3>", pressed3)
    canvas.bind("<Shift-Button-1>", pressed3)       #shift+クリックを割り当てている
    root.mainloop()

if __name__ == "__main__":
    main()