import math
import numpy as np
import sys
sys.path.append("..")
from chapter5.myCanvas import MyCanvas
from parametricCurve import ParametricCurve

class SineCurve(ParametricCurve):
    def __init__(self, canvas):
        super().__init__(canvas)

    def evaluate(self, t):
        return np.array((t, math.sin(t)))   #パラメータに対する座標を変換

class CosineCurve(ParametricCurve):
    def __init__(self, canvas):
        super().__init__(canvas)

    def evaluate(self, t):
        return np.array((t, math.cos(t)))

class TangentCurve(ParametricCurve):
    def __init__(self, canvas):
        super().__init__(canvas)

    def evaluate(self, t):
        return np.array((t, math.tan(t)))

def main():
    canvas = MyCanvas(r=8)
    offset = np.array((-math.pi, 0))
    canvas.drawPolyline([np.array((-4, 0)), np.array((4, 0))], color="blue")
    canvas.drawPolyline([np.array((-math.pi, -4)), np.array((-math.pi, 4))], color="blue")
    SineCurve(canvas).drawCurve(-1, 8, offset)
    CosineCurve(canvas).drawCurve(-1, 8, offset)
    TangentCurve(canvas).drawCurve(-1, 8, offset)
    canvas.mainloop()

if __name__ == "__main__":
    main()