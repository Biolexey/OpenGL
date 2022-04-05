import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from cube import Cube
from myGLCanvas import MyGLCanvas
from fractal import Fractal, getArgs

class MengerSponge(Fractal):
    def __init__(self, times):
        cube = Cube()
        nv = len(cube.vertices)                 #頂点数
        ne = len(cube.edges)                    #稜線数
        SCL = 1 / 3                             #縮小率
        vecs = []                               #平行移動用ベクトルリスト
        for i in range(nv):
            vecs.append(np.array(cube.vertices[i]) * (1-SCL))
                                                #頂点への平行移動ベクトル
        for i in range(ne):
            mid = (np.array(cube.vertices[cube.edges[i][0]]) + 
                   np.array(cube.vertices[cube.edges[i][1]])) / 2
            vecs.append(mid * (1-SCL))          #稜線中点への平行移動ベクトル
        super().__init__(cube, SCL, vecs, times)

def main():
    times, args = getArgs()
    canvas = MyGLCanvas()
    dispObj = MengerSponge(times)
    canvas.init(dispObj)
    canvas.argsInit(args)
    canvas.loop()

if __name__ == '__main__':               
  main()                