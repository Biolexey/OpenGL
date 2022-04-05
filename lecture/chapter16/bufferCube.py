import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter16.linearCube import LinearCube
from chapter15.myTranslateCanvas import MyTranslateCanvas
import numpy as np

class BufferCube(LinearCube):
    def __init__(self):
        super().__init__()
        BYTE, SIZE, STRIDE = (4, 3, 0)
        self.buffers = glGenBuffers(3)          #バッファオブジェクトの作成
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[0])
        glBufferData(GL_ARRAY_BUFFER, len(self.vertices)*BYTE,
                     np.array(self.vertices, dtype=np.float32),
                     GL_STATIC_DRAW)
        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(SIZE, GL_FLOAT, STRIDE, None)
        glBindBuffer(GL_ARRAY_BUFFER, self.buffers[1])
        glBufferData(GL_ARRAY_BUFFER, len(self.colors)*BYTE,
                     np.array(self.colors, dtype=np.float32),
                     GL_STATIC_DRAW)
        glEnableClientState(GL_COLOR_ARRAY)
        glColorPointer(SIZE, GL_FLOAT, STRIDE, None)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.buffers[2])
        glBufferData(GL_ELEMENT_ARRAY_BUFFER, len(self.indices)*BYTE,
                     np.array(self.indices, dtype=np.uint32),
                     GL_STATIC_DRAW)

    def display(self):
        print(self.indices)
        glDrawElements(GL_QUADS, len(self.indices), GL_UNSIGNED_INT, None)

def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = BufferCube()                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == "__main__":               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出             
