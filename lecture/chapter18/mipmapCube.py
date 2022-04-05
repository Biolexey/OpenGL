import sys
sys.path.append("..")
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from chapter15.myTranslateCanvas import MyTranslateCanvas
from chapter18.textureCube import TextureCube, getArgs

class MipmapCube(TextureCube):
    def __init__(self, texfile):
        super().__init__(texfile)
        glGenerateMipmap(GL_TEXTURE_2D)         #mipmapの作成
        glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER,
                       GL_LINEAR_MIPMAP_LINEAR) #テクスチャ縮小時のmipmap補完作成
    
def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = MipmapCube(getArgs())                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出