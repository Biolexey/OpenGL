import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
sys.path.append("..")
from chapter12.myGLCanvas import MyGLCanvas

class MyRotateCanvas(MyGLCanvas):
    def __init__(self):
        super().__init__()
        self.x, self.y = -1, -1             #直前のカーゾルの位置
        self.buttondown = -1                #押されたボタン番号

    def mouse(self, button, state, x, y):
        if state == GLUT_DOWN:              #マウスプレス時
            self.buttondown = button
            self.x, self.y = x, y
        if state == GLUT_UP:
            self.buttondown = -1

    def motion(self, x, y):
        if self.buttondown == GLUT_LEFT_BUTTON:#左ボタンがプレスの時
            thetaX, thetaY = (360*(y-self.y)/self.height, 360*(x-self.x)/self.width)
                                            #カーソル移動分の回転量
            self.rotX, self.rotY = self.rotX+thetaX, self.rotY+thetaY
                                            #物体の姿勢回転角
            self.x, self.y = x, y           #カーソル位置の更新
            self.display()

    def loop(self):
        glutReshapeFunc(self.reshape)
        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutMainLoop()
        