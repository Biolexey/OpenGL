import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter13.mySpinCanvas import MySpinCanvas
from chapter15.quaternion import Quaternion
from chapter15.rotMatrix import RotMatrix

class MyTranslateCanvas(MySpinCanvas):
    def __init__(self):
        super().__init__()  
        self.ident = Quaternion.identity()
        #self.ident = RotMatrix.identity()  

    def motion(self, x, y):
        deltaX, deltaY = x-self.x, y-self.y         #カーソル移動分の回転量
        TRANSRATIO = 5                              #平行移動量の調整パラメタ
        if self.buttondown == GLUT_LEFT_BUTTON:
            SPINRATIO = 50
            self.angle = (deltaX**2 + deltaY**2)**0.5 * SPINRATIO / \
                min(self.width, self.height)
            modelMatrix = glGetDoublev(GL_MODELVIEW_MATRIX)
            projMatrix = glGetDoublev(GL_PROJECTION_MATRIX)
            viewport = glGetIntegerv(GL_VIEWPORT)
            originX, originY, originZ = \
                gluProject(0, 0, 0, modelMatrix, projMatrix, viewport)
            self.axisX, self.axisY, self.axisZ = \
                gluUnProject(originX+deltaY, originY+deltaX, originZ,
                             modelMatrix, projMatrix, viewport)

        if self.buttondown == GLUT_RIGHT_BUTTON:
            self.offset[0] += deltaX * TRANSRATIO / self.height
            self.offset[1] -= deltaY * TRANSRATIO / self.height
          
        self.x, self.y = x, y           #カーソル位置の更新
        self.idle()
    
    def positionInit(self):
        self.offset = [0, 0, self.depth]
        self.state = self.ident.rotAroundAxis(self.rotX, 1, 0, 0)\
                               .rotAroundAxis(self.rotY, 0, 1, 0)\
                               .rotAroundAxis(self.rotZ, 0, 0, 1)

    def idle(self):
        self.state = self.state.rotAroundAxis(
                     self.angle, self.axisX, self.axisY, self.axisZ)
        self.display()

    def display(self):
        glLoadIdentity()
        glMultMatrixd(self.state.setMatrix(self.offset))
        self.coredisplay()   