from OpenGL.GL import *

class Polyhedron():
    def __init__(self, vertices=(), faces=(), edges=(), colors=()):
        self.vertices, self.faces, self.edges, self.colors = \
            vertices, faces, edges, colors

    def display(self):
        for i in range(len(self.faces)):
            glBegin(GL_POLYGON)             #多角形描画開始
            glColor3dv(self.colors[i])
            for j in range(len(self.faces[i])):
                glVertex3dv(self.vertices[self.faces[i][j]])
            glEnd()
            
