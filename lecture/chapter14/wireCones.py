import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
import math
from chapter13.myRotateCanvas import MyRotateCanvas

class WireCones():
    def __init__(self):
        self.apex = (0, 1, 0)           #円錐の頂点
        NOP = 20                        #正20角錐
        self.circle = []
        for i in range(NOP+1):
            t = 2 * math.pi * i / NOP
            self.circle.append((math.sin(t), -1, math.cos(t)))
    
    def displayEdges(self):
        glColor3dv((1, 1, 0))
        glBegin(GL_LINE_LOOP)           #円錐底面描画
        for i in range(1, len(self.circle)):
            glVertex3dv(self.circle[len(self.circle)-i])
        glEnd()
        glBegin(GL_LINES)               #円錐側面描画
        for i in range(1, len(self.circle)):
            glVertex3dv(self.apex)
            glVertex3dv(self.circle[i])
        glEnd()

    def display(self):
        NOC = 16                        #円錐の個数
        for i in range(NOC):
            t = 2 * math.pi * i / NOC
            glPushMatrix()
            glTranslated(1.6*math.sin(t), 0, 1.6*math.cos(t))   #半径1.6上に円錐を配置
            glScaled(0.3, 1.4, 0.3)
            self.displayEdges()
            glPopMatrix()

def main():
    canvas = MyRotateCanvas()
    dispObj = WireCones()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == "__main__":
    main()

