#bullsEye by joshGara

from graphics import *

def draw_ci(cX, cY, size, color, win):
    circle = Circle(Point(cX, cY), size)
    circle.setFill(color)
    circle.draw(win)

def draw_be(bX, bY, bSize, bColor1, bColor2, bWin):
    for i in range (5):
        if (i) % 2 == 1:
            cCol = bColor1
        else:
            cCol = bColor2
        draw_ci(bX, bY, bSize, cCol, bWin)
        bSize -= 10

ciSz = 50


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)

draw_be(ciSz*5, ciSz*5, ciSz, "dark blue", "white", bullWin)


bullWin.getMouse()
bullWin.close()
