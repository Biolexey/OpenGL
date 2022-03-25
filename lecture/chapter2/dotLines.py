from tkinter import *

W, H = 600, 600

def display(canvas):
    points = ((W/60, H-1), (W/20, H-1), (W/8, H-1), (W/4, H-1),
              (W/2, H-1), (W-1, H-1), (W-1, H/2), (W-1, H/4),
              (W-1, H/8), (W-1, H/20), (W-1, H/60))
    origin = (0, 0)
    for i in range(len(points)):
        if points[i][0] >= points[i][1]:
            n = int(points[i][0])
            d = points[i][1] / points[i][0]
            for x in range(n+1):
                y = int(x*d+0.5)
                p, q = ((x, y), (x+1, y+1))
                canvas.create_rectangle(p, q, outline="", fill="black")
        
        else:
            n = int(points[i][1])
            d = points[i][0] / points[i][1]
            for y in range(n+1):
                x = int(y*d+0.5)
                p, q = ((x, y), (x+1, y+1))
                canvas.create_rectangle(p, q, outline="", fill="black")


def main():
    root = Tk()
    canvas = Canvas(root, width=W, height=H, highlightthickness=0)

    canvas.pack()
    display(canvas)
    root.mainloop()

if __name__ == "__main__":
    main()