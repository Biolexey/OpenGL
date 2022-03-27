from tkinter import *

W, H = 200, 200

def pressed(event):     #ボタン押下関数
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline="", fill="#ff0000")

def released(event):    #ボタン離化関数
    global canvas
    canvas.create_rectangle((2, 2), (W+3, H+3), outline="", fill="#00ff00")

def main():
    global canvas
    root = Tk()
    canvas = Canvas(root, width=W, height=H, bg="#00ff00")
    canvas.pack()
    canvas.bind("<Button-1>", pressed)          #コールバック関数
    canvas.bind("<ButtonRelease-1>", released)  #コールバック関数
    root.mainloop()

if __name__ == "__main__":
    main()