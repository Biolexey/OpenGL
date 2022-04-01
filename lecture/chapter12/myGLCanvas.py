import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class MyGLCanvas():
    def __init__(self, width=500, height=500):
        self.width, self.near = width, height
        self.FOV, self.near, self.far = 25, 1, 20
        self.depth, self.rotX, self.rotY, self.rotZ = -10, 20, -30, 0
        self.objectID = 0
        glutInit(sys.argv)                  #glutの初期化
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
        glutInitWindowSize(width, height)
        glutInitWindowPosition(0, 0)
        glutCreateWindow(b"OpenGL")   

    def init(self, dispObj):
        glClearColor(0, 0, 0, 1)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        self.objectID = glGenLists(1)       #ディスプレイリストの作成
        glNewList(self.objectID, GL_COMPILE)#ディスプレイリストへの登録開始
        dispObj.display()
        glEndList()                         #ディスプレイリストへの登録終了
    
    def argsInit(self, args):
        if len(args) == 1 and args[0] != "":#文字列が一個の場合
            FOV = float(args[0])
        if len(args) == 2:
            near, far = float(args[0]), float(args[1])
        if len(args) == 3:
            rotX, rotY, rotZ = float(args[0]), float(args[1]), float(args[2])
                    
    def reshape(self, width, height):
        self.cameraInit(width, height)      #カメラ（レンズ・フィルム）の設定
        self.positionInit()                 #初期位置の設定

    def cameraInit(self, width, height):
        self.width, self.height = width, height
        aspect = width / height             #アスペクト比
        glViewport(0, 0, width, height)
        glMatrixMode(GL_PROJECTION)         #透視投影行列を指定
        glLoadIdentity()                    #行列の初期化
        gluPerspective(self.FOV, aspect, self.near, self.far)#透視投影行列の設定関数
        glMatrixMode(GL_MODELVIEW)          #視野変換行列の指定
        glLoadIdentity()

    def positionInit(self):
        glTranslated(0, 0, self.depth)

    def display(self):
        glPushMatrix()                      #行列の複写(待機)
        glRotated(self.rotX, 1, 0, 0)
        glRotated(self.rotY, 0, 1, 0)
        glRotated(self.rotZ, 0, 0, 1)
        self.coredisplay()
        glPopMatrix()                       #複写行列の回復

    def coredisplay(self):                  #描画本体関数
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glCallList(self.objectID)           #ディスプレイリストの呼び出し
        glutSwapBuffers()                   #ダブルバッファの切り替え

    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMainLoop()
    
def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input("FOV / near far / rotX rotY rotZ / [] = ").split(" ")
    return args