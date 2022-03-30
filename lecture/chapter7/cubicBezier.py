import sys
import numpy as np
sys.path.append("..")
from chapter5.myCanvas import MyCanvas
from parametricCurve import ParametricCurve

class CubicBezierCurve(ParametricCurve):
    def __init__(self, canvas, points):
        super().__init__(canvas)
        self.points = points

    def drawCurve(self, ts=0, te=1):
        super().drawCurve(ts, te)
        self.canvas.drawPolyline(self.points, color="blue")
        for i in range(len(self.points)):
            self.canvas.drawMarker(self.points[i], fill="blue")
    
    def evaluate(self, t):
        return (1-t)**3     * self.points[0] + \
             3*(1-t)**2 * t * self.points[1] + \
             3*(1-t) * t**2 * self.points[2] + \
                       t**3 * self.points[3]



def main():
    N = 4
    if len(sys.argv) > 2*N:
        pnts = sys.argv[1]
    else:
        pnts = input("x0 y0 x1 y1 x2 y2 x3 y3 / [] = ").split(" ")
        if len(pnts) < 2*N:
            pnts = ["-0.9", "-0.8", "-0.5", "0.8", "0.3", "0.6", "0.8", "-0.9"]

    points = []
    for i in range(N):
        points.append(np.array((float(pnts[2*i]), float(pnts[2*i+1]))))

    canvas = MyCanvas()
    CubicBezierCurve(canvas, points).drawCurve()
    canvas.mainloop()

if __name__ == "__main__":
    main()