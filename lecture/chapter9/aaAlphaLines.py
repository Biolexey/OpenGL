from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
sys.path.append("..")
from chapter8.lines import window,display, reshape, W, H

def init():
    glClearColor(1, 1, 1, 1)
    glEnable(GL_LINE_SMOOTH)        #線分アンチエイリアス有効
    glEnable(GL_BLEND)              #αブレンディング（加重平均）
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)   #描画色*α + 背景色*(1-α)

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
