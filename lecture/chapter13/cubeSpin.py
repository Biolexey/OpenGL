import sys
from mySpinCanvas import MySpinCanvas
import sys
sys.path.append("..")
from chapter12.cube import Cube

def main():
    canvas = MySpinCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == '__main__':               # 起動の確認 (コマンドラインからの起動)
    main()                                 # main関数の呼出