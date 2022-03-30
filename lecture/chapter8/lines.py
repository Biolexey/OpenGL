import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#windowsではglutInit()でエラーが起こる可能性がある。その場合は64bit版を別途サイトからダウンロードしてpip installしなおせば動く
#https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyopengl

W, H = 600, 600
points = ((W/60, H-1), (W/20, H-1), (W/8, H-1), (W/4, H-1),
          (W/2, H-1), (W-1, H-1), (W-1, H/2), (W-1, H/4),
          (W-1, H/8), (W-1, H/20), (W-1, H/60))

def window(width, height):
    glutInit(sys.argv)      #glutの初期化
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"OpenGL") #windowの作成

def init(): #openglの初期化
    glClearColor(1, 1, 1, 1)    #背景色の設定(白)

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width-1, 0, height-1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def display():
    origin = (0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_LINES)
    glColor3d(0, 0, 0)
    for i in range(len(points)):
        glVertex2dv(origin)
        glVertex2dv(points[i])
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