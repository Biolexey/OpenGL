import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

LEFT, RIGHT, TOP, BOTTOM = -300, 300, 600, 0

def window():
    glutInit(sys.argv)      #glutの初期化
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(RIGHT-LEFT+1, TOP-BOTTOM)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"OpenGL") #windowの作成

def init():
    glClearColor(0, 0, 0, 1)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(LEFT, RIGHT, BOTTOM, TOP)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()  

def display():
    width = 4                       #上端での縞の幅
    ratio = width / (TOP-BOTTOM)    #y方向一画素での縞の幅の変化量
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    for y in range(TOP, BOTTOM, -1):
        for x in range(LEFT, RIGHT+1):
            rgb = abs(math.floor(x / (ratio*y)) % 2)    #xを縞の幅で割った際の整数部分の偶奇で白黒決定
            glColor3d(rgb, rgb, rgb)
            glVertex2i(x, y)
    glEnd()
    glFlush()

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()    

def main():
    window()
    init()
    loop()

if __name__ == "__main__":
    main()