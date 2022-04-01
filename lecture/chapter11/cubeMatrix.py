import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
import chapter10.cubePosition as cp

def reshape(width, height):
    FOV, near, far = 25, 1, 20
    aspect = width / height             #アスペクト比
    glViewport(0, 0, width, height)     #ビューポートの設定
    glMatrixMode(GL_PROJECTION)         #透視投影行列を指定
    glLoadIdentity()                    #行列の初期化
    gluPerspective(FOV, aspect, near, far)#透視投影行列の設定関数
    glMatrixMode(GL_MODELVIEW)          #視野変換行列の指定
    glLoadIdentity()
    eyeXZ = (cp.eyeX**2 + cp.eyeZ**2)**0.5  #xz平面での視点と注視点の距離
    eyeXYZ = (eyeXZ**2 + cp.eyeY**2)**0.5#視点と注視点の距離
    translate = (1, 0,       0, 0,
                 0, 1,       0, 0,
                 0, 0,       1, 0,
                 0, 0, -eyeXYZ, 1)      #平行移動行列(z軸)
    glMultMatrixd(translate)            #平行移動行列の適用
    sinP, cosP = cp.eyeY/eyeXYZ, eyeXZ/eyeXYZ
    rotateX = (1,     0,    0, 0,
               0,  cosP, sinP, 0,
               0, -sinP, cosP, 0,
               0,     0,    0, 1)        #回転行列(x軸)
    glMultMatrixd(rotateX)
    sinT, cosT = cp.eyeX/eyeXZ, cp.eyeZ/eyeXZ
    rotateY = (cosT, 0, sinT, 0,
                  0, 1,    0, 0,
              -sinT, 0, cosT, 0,
                  0, 0,    0, 1)        #回転行列(y軸)
    glMultMatrixd(rotateY)

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(cp.display)
    glutMainLoop()

def main():
    cp.window()
    cp.init()
    cp.argsInit()
    loop()

if __name__ == "__main__":
    main() 
