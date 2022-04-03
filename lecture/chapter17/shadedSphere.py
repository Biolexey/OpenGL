import sys
sys.path.append("..")
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from chapter17.myShadeCanvas import MyShadeCanvas
from chapter17.shadedSubdivision import ShadedSubdivision, getArgs

class ShadedSphere(ShadedSubdivision):
    def __init__(self, times):
        super().__init__(times)

    def triangle(self, p0, p1, p2):
        glShadeModel(GL_SMOOTH)                 #フラットからスムーズシェーディングに変更
        glBegin(GL_POLYGON)
        glNormal3dv(tuple(p0))
        glVertex3dv(tuple(p0))
        glNormal3dv(tuple(p1))
        glVertex3dv(tuple(p1))
        glNormal3dv(tuple(p2))
        glVertex3dv(tuple(p2))
        glEnd()

def main():                              
  canvas = MyShadeCanvas()                  # MyGLCanvasの作成
  dispObj = ShadedSphere(getArgs())                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出