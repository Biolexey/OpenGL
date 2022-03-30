from OpenGL.GL import *
from OpenGL.GLUT import *
from lines import window, init, reshape, W, H, points

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    glColor3d(0, 0, 0)
    for i in range(len(points)):
        if points[i][0] >= points[i][1]:
            n = int(points[i][0]) + 1
            d = points[i][1] / points[i][0]
            for x in range(n):
                glVertex2i(x, int(d*x+0.5))
        else:
            n = int(points[i][1]) + 1
            d = points[i][0] / points[i][1]        
            for y in range(n):
                glVertex2i(int(d*y+0.5), y)   
    glEnd()
    glFlush()

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

def main():
    window(W, H)
    init()
    loop()

if __name__ == "__main__":
    main() 