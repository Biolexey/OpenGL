import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
import chapter10.cubePosition as cp

FOV, near, far = 25, 1, 20
depth, rotX, rotY, rotZ = -10, 20, -30, 0

def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input("FOV / near far / rotX rotY rotZ / [] = ").split(" ")
    return args

def argsInit(args):
    global FOV, near, far
    global rotX, rotY, rotZ
    if len(args) == 1 and args[0] != "":        #文字列が一個の場合
        FOV = float(args[0])
    if len(args) == 2:
        near, far = float(args[0]), float(args[1])
    if len(args) == 3:
        rotX, rotY, rotZ = float(args[0]), float(args[1]), float(args[2])

def reshape(width, height):
    aspect = width / height             #アスペクト比
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)         #透視投影行列を指定
    glLoadIdentity()                    #行列の初期化
    gluPerspective(FOV, aspect, near, far)#透視投影行列の設定関数
    glMatrixMode(GL_MODELVIEW)          #視野変換行列の指定
    glLoadIdentity()
    glTranslate(0, 0, depth)            #平行移動行列(z軸)

def display():
    glPushMatrix()                      #行列の複写(待機)
    glRotated(rotX, 1, 0, 0)
    glRotated(rotY, 0, 1, 0)
    glRotated(rotZ, 0, 0, 1)
    cp.display()
    glPopMatrix()                       #複写行列の回復

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

def main():
    cp.window()
    cp.init()
    argsInit(getArgs())
    loop()

if __name__ == "__main__":
    main() 