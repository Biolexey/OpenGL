from OpenGL.GL import *
from OpenGL.GLUT import *
import sys
sys.path.append("..")
from chapter8.lines import window, init, reshape, W, H, points

def display():
    glClear(GL_COLOR_BUFFER_BIT)        #背景の消去
    glBegin(GL_POINTS)                  #点描画の開始
    for i in range(len(points)):
        if points[i][0] >= points[i][1]:#横長なら
            n = int(points[i][0]) + 1   #表示ピクセル個数
            d = points[i][1] / points[i][0]
            for x in range(n):
                y = int(d*x)
                r = d*x - y             #実際の座標とのずれ
                glColor3d(r, r, r)      #ずれの分だけ色を薄く
                glVertex2i(x, y)
                glColor3d(1-r, 1-r, 1-r)#ずれの分だけ色を濃く
                glVertex2i(x, y+1)
        else:
            n = int(points[i][1]) + 1   #表示ピクセル個数
            d = points[i][0] / points[i][1]
            for y in range(n):
                x = int(d*y)
                r = d*y - x             #実際の座標とのずれ
                glColor3d(r, r, r)      #ずれの分だけ色を薄く
                glVertex2i(x, y)
                glColor3d(1-r, 1-r, 1-r)#ずれの分だけ色を濃く
                glVertex2i(x+1, y) 
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
