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
    glEnable(GL_BLEND)              #αブレンディング（加重平均）
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   #描画色*α + 背景色*(1-α)


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
        dl = LEFT / (ratio*y)       #画素左端の相対位置
        il = int(math.floor(dl))    #上の整数部分
        for x in range(LEFT, RIGHT+1):
            dr = (x+1) / (ratio*y)
            ir = int(math.floor(dr))
            if il == ir:            #左と右端の色が等しい
                alpha = 1 if ir else 0
            else:
                alpha = abs(il%2) * (1-(dl-il)) + abs(ir%2) * (dr-ir)
                for i in range(il+1, ir):
                    alpha += abs(i % 2)
                alpha /= ir-il
            glColor4d(1, 1, 1, alpha)
            glVertex2i(x, y)
            dl = dr
            il = ir
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