import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter15.myTranslateCanvas import MyTranslateCanvas

class ColorCube():
    def __init__(self):
        self.vertices = ((-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
                         (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1))
                                            #頂点位置

        self.faces = ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7),
                      (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1))
                                            #各面の頂点番列

        self.colors = ((0, 1, 1), (1, 0, 1), (1, 1, 0), (0, 1, 0),
                       (0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1))
                                            #各面の描画色
    def display(self):
        #glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_QUADS)                   #四角形描写の開始
        for i in range(len(self.faces)):
            for j in range(len(self.faces[i])):
                glColor3dv(self.colors[self.faces[i][j]])
                glVertex3dv(self.vertices[self.faces[i][j]])
        glEnd()
        glFlush()

def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = ColorCube()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出