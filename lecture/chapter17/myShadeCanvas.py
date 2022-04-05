import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter15.myTranslateCanvas import MyTranslateCanvas

class MyShadeCanvas(MyTranslateCanvas):
    def __init__(self):
        super().__init__()
        self.lid, self.pid = 0, 0           #光源番号と光源位置の初期化
        self.light = (GL_LIGHT0, GL_LIGHT1) #光源番号(以下、環境・拡散・鏡面成分と対応)
        self.ambient = ((0.1, 0.1, 0.1, 1.0), (0.3, 0.1, 0.1, 1.0))
        self.diffuse = ((1.0, 1.0, 1.0, 1.0), (1.0, 0.1, 0.1, 1.0))
        self.specular = ((0.9, 0.9, 0.9, 1.0), (0.9, 0.2, 0.2, 1.0))
        self.lightPosition = ((5.0, 5.0, 0.0, 1.0), (5.0, 5.0, 0.0, 0.0))
                                            #光源位置

    def init(self, dispObj):
        super().init(dispObj)
        glEnable(GL_LIGHTING)               #陰影描画の利用
        glEnable(GL_NORMALIZE)              #法線ベクトルの正規化
        for i in range(len(self.light)):
            glLightfv(self.light[i], GL_AMBIENT, self.ambient[i])
            glLightfv(self.light[i], GL_DIFFUSE, self.diffuse[i])
            glLightfv(self.light[i], GL_SPECULAR, self.specular[i])
        glEnable(self.light[self.lid])

    def keyboard(self,key, x, y):
        if key == b"l":
            glDisable(self.light[self.lid]) #現行の光源番号の無効化
            self.lid = (self.lid + 1) % len(self.light)#光源番号の再計算(一個ずらす)
            glEnable(self.light[self.lid])
        elif key == b"p":
            self.pid = (self.pid + 1) % len(self.lightPosition)#光源位置番号の再計算(一個ずらす)

        self.display()

    def display(self):
        glLoadIdentity()
        glLightfv(self.light[self.lid], GL_POSITION, self.lightPosition[self.pid])
        glMultMatrixd(self.state.setMatrix(self.offset))
        self.coredisplay()

    def loop(self):
        glutKeyboardFunc(self.keyboard)
        super().loop()