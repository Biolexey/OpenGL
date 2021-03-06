from tkinter import *
import circle

def display(canvas, points):
    for i in range(1, len(points)):
        j = (2*i) % len(points)
        canvas.create_line(points[i], points[j])

def main():
    root = Tk()
    canvas = Canvas(root, width=circle.W, height=circle.H)
    canvas.pack()
    points = circle.circle()
    circle.display(canvas, points)
    display(canvas, points)
    root.mainloop()

if __name__ == "__main__":
    main()