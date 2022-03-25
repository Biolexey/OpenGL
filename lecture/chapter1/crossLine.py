
from tkinter import *
import sys

W, H = 400, 300

def display(canvas, msg):                   #描画関数
    """
    canvas
    2本の線分と文字列を描画する

    """
    canvas.create_line((0, 0), (W-1, H-1))
    canvas.create_line((0, H-1), (W-1, 0))
    canvas.create_text((W/2, H/2), text = msg)

def main():
    if len(sys.argv) > 1:
        msg = sys.argv[1]
    else:
        msg = input("msg = ")
    root = Tk()
    canvas = Canvas(root, width = W, height = H, highlightthickness = 0)

    canvas.pack()
    display(canvas, msg)
    root.mainloop()

if __name__ =="__main__":
    main()