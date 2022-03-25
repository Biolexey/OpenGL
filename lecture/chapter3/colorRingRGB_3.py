from tkinter import *
import sys, os
sys.path.append("..")
from chapter2 import circle


def f2hex(x):   #１６進数文字列への変換関数
    return "{:02X}".format(int(x*0xff))

def string(r, g, b):    #色指定文字列の作成関数
    return "#" + f2hex(r) + f2hex(g) + f2hex(b)

def color(n, i):
    """
    n = 頂点数
    i = 順番
    円周上でi/nの色指定文字列を作成して返す
    
    """
    onesixth, twosixth, threesixth, foursixth, fivesixth, six = \
        1/6, 2/6, 3/6, 4/6, 5/6, 6
    ratio = i / n
    if ratio <= onesixth:
        return string(1.0, ratio*six, 0.0)
    elif ratio <= twosixth:
        return string((twosixth-ratio)*six, 1.0, 0.0)
    elif ratio <= threesixth:
        return string(0.0, 1.0, (ratio-twosixth)*six)
    elif ratio <= foursixth:
        return string(0.0, (foursixth-ratio)*six, 1.0)
    elif ratio <= fivesixth:
        return string((ratio-foursixth)*six, 0.0, 1.0)
    else:
        return string(1.0, 0.0, (1.0-ratio)*six)

def display(canvas, points):
    for i in range(len(points)):
        j = (i+1) % len(points)
        canvas.create_line(points[i], points[j], fill=color(len(points), i))

def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H, bg="black")
    canvas.pack()
    points = circle.circle()
    display(canvas, points)
    root.mainloop()

if __name__ == "__main__":
    main()
