import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter16.linearCube import LinearCube
from chapter15.myTranslateCanvas import MyTranslateCanvas

class ArrayCube(LinearCube):
    def __init__(self):
        super().__init__()
        SIZE, STRIDE = 3, 0
        glEnableClientState(GL_VERTEX_ARRAY)        #頂点座標値配列の利用
        glVertexPointer(SIZE, GL_FLOAT, STRIDE, self.vertices)
        glEnableClientState(GL_COLOR_ARRAY)         #頂点描画色配列の利用
        glColorPointer(SIZE, GL_FLOAT, STRIDE, self.colors)

    def display(self):
        print(self.indices)
        glDrawElements(GL_QUADS, len(self.indices), GL_UNSIGNED_INT, self.indices)

def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = ArrayCube()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == "__main__":               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出