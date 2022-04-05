import sys
sys.path.append("..")
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from chapter17.myShadeCanvas import MyShadeCanvas
from chapter18.textureCube import TextureCube, getArgs
import numpy as np

class ShadedTextureCube(TextureCube):
    def __init__(self, texfile):
        super().__init__(texfile)
        self.diffuse = (0.8, 0.8, 0.8, 1.0)
        self.specular = (1.0, 1.0, 1.0, 1.0)
        self.shininess = 100

    def display(self):
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
                                            #陰影付きテクスチャマッピング
        self.material()
        glShadeModel(GL_FLAT)
        for i in range(len(self.faces)):    #面番号
            glBegin(GL_POLYGON)
            glNormal3dv(normal(self.vertices[self.faces[i][0]],
                               self.vertices[self.faces[i][1]],
                               self.vertices[self.faces[i][2]]))#法線ベクトルの指定
            for j in range(len(self.faces[i])):  #頂点番号
                glTexCoord2dv(self.texCoord[i%len(self.texCoord)][j])
                                            #テクスチャ座標値の指定
                glVertex3dv(self.vertices[self.faces[i][j]])
            glEnd() 
            
    def material(self):
        glMaterialfv(GL_FRONT, GL_AMBIENT_AND_DIFFUSE, self.diffuse)
                                            #環境成分と拡散成分の設定
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.specular)
                                            #鏡面成分の設定
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)
                                            #減衰係数の設定       

def normal(p0, p1, p2):
    p0, p1, p2 = (np.array(p0), np.array(p1), np.array(p2))
    return tuple(np.cross(p1-p0, p2-p0))    #p1-p0とp2-p0の外積

def main():                              
  canvas = MyShadeCanvas()                  # MyGLCanvasの作成
  dispObj = ShadedTextureCube(getArgs())                       # Cubeオブジェクトの作成
  canvas.init(dispObj)                   # OpenGLの初期化
  canvas.loop()                          # コールバックメソッドの設定とループ起動

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
  main()                                 # main関数の呼出