import sys
sys.path.append("..")
from chapter15.myTranslateCanvas import MyTranslateCanvas
from chapter12.cube import Cube

def main():
    canvas = MyTranslateCanvas()
    dispObj = Cube()
    canvas.init(dispObj)
    canvas.loop()

if __name__ == "__main__":
    main()