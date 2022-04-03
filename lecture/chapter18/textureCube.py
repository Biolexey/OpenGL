import sys
sys.path.append("..")
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from chapter15.myTranslateCanvas import MyTranslateCanvas

#from PIL import Image                       #PILモジュールimport

import cv2

class TextureCube():
    def __init__(self, texfile):
        self.vertices = ((-1, -1, -1), ( 1, -1, -1), ( 1,  1, -1), (-1,  1, -1),
                         (-1, -1,  1), ( 1, -1,  1), ( 1,  1,  1), (-1,  1,  1))
                                            #頂点座標
        self.faces = ((1, 2, 6, 5), (2, 3, 7, 6), (4, 5, 6, 7),
                      (0, 4, 7, 3), (0, 1, 5, 4), (0, 3, 2, 1))
        
        """                                    #各面の頂点番列
        try:
            img = Image.open(texfile)
        except IOError as ex:               #例外処理
            print("failed open texture file", ex.args, texfile)
        w, h  = img.size
        """
        img = cv2.imread(texfile)
        if img is None:
            print("failed open texture file", texfile)
            sys.exit(1)
        h, w  = img.shape[:2]

        glEnable(GL_TEXTURE_2D)             #テクスチャの利用
        #texID = glGenTextures(1)            #テクスチャデータの生成(複数の時は必須)
        #glBindTexture(GL_TEXTURE_2D, texID) #テクスチャ番号の設定(複数の時は必須)
        glPixelStorei(GL_UNPACK_ALIGNMENT, 1)#テクスチャのメモリ格納状況
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, w, h, 0, GL_BGR, GL_UNSIGNED_BYTE, 
                     img)         #画像データのテクスチャメモリへの割り当て
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
                                            #テクスチャ縮小時の線形補間指定
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
                                            #テクスチャ拡大時の線形補間指定
        self.texCoord = (((0.0, 1.0), (1.0, 1.0), (1.0, 0.0), (0.0, 0.0)),
                         ((0.25, 0.75), (0.75, 0.75), (0.75, 0.25), (0.25, 0.25)))
                                            #テクスチャ座標
        
    def display(self):
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
                                            #単純なテクスチャマッピング
        for i in range(len(self.faces)):    #面番号
            glBegin(GL_POLYGON)
            for j in range(len(self.faces[i])):  #頂点番号
                glTexCoord2dv(self.texCoord[i%len(self.texCoord)][j])
                                            #テクスチャ座標値の指定
                glVertex3dv(self.vertices[self.faces[i][j]])
            glEnd()

def getArgs():
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = input("texture file = ").split(" ")
    return args[0]

def main():                              
  canvas = MyTranslateCanvas()                  # MyGLCanvasの作成
  dispObj = TextureCube(getArgs())                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出