import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

eyeX, eyeY, eyeZ = 4, 3, 7              #デフォルトの視点位置
vertices = ((-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
            (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1))
                                        #頂点位置

faces = ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7),
         (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1))
                                        #各面の頂点番列

colors = (( 0,   1,   1), (  1, 0,   1), (  1,   1, 0),
          ( 0, 0.5, 0.5), (0.5, 0, 0.5), (0.5, 0.5, 0))
                                        #各面の描画色

def window(width=500, height=500):
    glutInit(sys.argv)                  #glutの初期化
    glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"OpenGL")         #windowの作成

def init(): #openglの初期化
    glClearColor(0, 0, 0, 1)
    glEnable(GL_DEPTH_TEST)             #奥行テストの実行
    glEnable(GL_CULL_FACE)              #背面除去の利用

def argsInit():
    global eyeX, eyey, eyeZ
    if len(sys.argv) > 3:
        args = sys.argv[1]
    else:
        args = input("eyeX, eyeY, eyeZ or [] = ").split(" ")
    if len(args) >= 3:
        eyeX, eyeY, eyeZ = float(args[0]), float(args[1]), float(args[2])

def reshape(width, height):
    global eyeX, eyey, eyeZ
    FOV, near, far = 25, 1, 20
    aspect = width / height             #アスペクト比
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(FOV, aspect, near, far)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(eyeX, eyeY, eyeZ, 0, 0, 0, 0, 1, 0)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glBegin(GL_QUADS)                   #四角形描写の開始
    for i in range(len(faces)):
        glColor3dv(colors[i])
        for j in range(len(faces[i])):
            glVertex3dv(vertices[faces[i][j]])
    glEnd()
    glFlush()

def loop():
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutMainLoop()

def main():
    window()
    init()
    argsInit()
    loop()

if __name__ == "__main__":
    main() 