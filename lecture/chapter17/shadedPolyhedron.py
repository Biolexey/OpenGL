import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np

class ShadedPolyhedron():
    def __init__(self, vertices=(), faces=(), diffuse=(), specular=(), shininess=0):
        self.vertices, self.faces, self.diffuse, self.specular, self.shininess = \
            vertices, faces, diffuse, specular, shininess

    def display(self):
        self.material()                     #反射率の設定
        glShadeModel(GL_FLAT)               #フラットシェーディングの利用
        for i in range(len(self.faces)):
            glBegin(GL_POLYGON)             #多角形描画開始
            glNormal3dv(normal(self.vertices[self.faces[i][0]],
                               self.vertices[self.faces[i][1]],
                               self.vertices[self.faces[i][2]]))#法線ベクトルの指定
            for j in range(len(self.faces[i])):
                glVertex3dv(self.vertices[self.faces[i][j]])#頂点座標値の設定
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