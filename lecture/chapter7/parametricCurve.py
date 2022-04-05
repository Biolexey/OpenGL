import numpy as np

class ParametricCurve(object):
    def __init__(self, canvas):
        self.canvas = canvas

    def drawCurve(self, ts=0, te=0, offset=np.array((0, 0)), nop=128):
        """
        ts, te = 描画対象のパラメタ値(開始、終了)
        offset = 平行移動ベクトル
        nop = 描画セグメント数
        
        """
        dt = (te - ts) / nop                                    #1セグメント分のパラメータ
        prevPnt = self.evaluate(ts) + offset                    #最初の点座標
        prevIn = self.canvas.inside(prevPnt)                    #最初の点が表示領域内にいるか判定
        for i in range(nop):                                    #線分列の数だけ反復
            currPnt = self.evaluate(ts + dt*(i+1)) + offset     #次の点座標
            currIn = self.canvas.inside(currPnt)
            if prevIn or currIn:                                #両端のどちらかが表示領域内にあれば
                self.canvas.drawPolyline([prevPnt, currPnt])
            prevPnt, prevIn = currPnt, currIn                   #点を更新