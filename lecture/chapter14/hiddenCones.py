import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
import math
from chapter13.myRotateCanvas import MyRotateCanvas
from wireCones import WireCones

class HiddenCones(WireCones):
    def __init__(self):
        super().__init__()
    
    def displayFaces(self):
        glColor3dv((0, 0, 0))
        glBegin(GL_POLYGON)             #円錐底面の描画
        for i in range(1, len(self.circle)):
            glVertex3dv(self.circle[len(self.circle)-i])
        glEnd()
        glBegin(GL_TRIANGLE_FAN)        #円錐側面の描画
        glVertex(self.apex)
        for i in range(len(self.circle)):
            glVertex3dv(self.circle[i])
        glEnd()
    
    def display(self):
        glEnable(GL_POLYGON_OFFSET_FILL)#面のオフセット
        glPolygonOffset(1, 1)           #オフセット量
        NOC = 16                        #円錐の個数
        for i in range(NOC):
            t = 2 * math.pi * i / NOC
            glPushMatrix()
            glTranslated(1.6*math.sin(t), 0, 1.6*math.cos(t))   #半径1.6上に円錐を配置
            glScaled(0.3, 1.4, 0.3)
            self.displayEdges()
            self.displayFaces()
            glPopMatrix()

def main():
    canvas = MyRotateCanvas()
    dispObj = HiddenCones()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == "__main__":
    main()