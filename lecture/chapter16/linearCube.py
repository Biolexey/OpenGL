import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter15.myTranslateCanvas import MyTranslateCanvas

class LinearCube():
    def __init__(self):
        self.vertices = (-1, -1, -1,   1, -1, -1,   1,  1, -1,  -1,  1, -1,
                         -1, -1,  1,   1, -1,  1,   1,  1,  1,  -1,  1,  1)
                                            #頂点位置

        self.indices = (1, 2, 6, 5,  2, 3, 7, 6,  4, 5, 6, 7,
                        0, 4, 7, 3,  0, 1, 5, 4,  0, 3, 2, 1)
                                            #各面の頂点番列

        self.colors = (0, 1, 1,  1, 0, 1,  1, 1, 0,  0, 1, 0,
                       0, 0, 1,  1, 0, 1,  1, 1, 1,  0, 1, 1)
                                            #各面の描画色
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        QUADS, FACES, SIZE = 4, 6, 3
        glBegin(GL_QUADS)                   #四角形描写の開始
        for i in range(FACES):                              #面番号
            for j in range(QUADS):                          #頂点番号
                index = self.indices[i*QUADS+j]*SIZE        #頂点データの先頭位置
                glColor3dv(self.colors[index: index+SIZE])
                glVertex3dv(self.vertices[index: index+SIZE])
        glEnd()
        glFlush()

def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = LinearCube()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出