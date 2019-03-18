
#bullsEye by joshGara

from graphics import *
from random import*

def draw_ci(cX, cY, size, color, win):
    circle = Circle(Point(cX, cY), size)
    circle.setFill(color)
    circle.draw(win)

def draw_be(bX, bY, rings, rSize, bColor1, bColor2, bWin):
    bSize = rings * rSize
    for i in range (rings):
        if (i) % 2 == 1:
            cCol = bColor1
        else:
            cCol = bColor2
        draw_ci(bX, bY, bSize, cCol, bWin)
        bSize -= rSize

ciSz = 50


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)

for j in range (10):
    ranX = randint(ciSz, ciSz * 9)
    ranY = randint(ciSz, ciSz * 9)
    ranSiz = randint(1, 20)
    draw_be(ranX, ranY, ranSiz, 4, "dark blue", "red", bullWin)


bullWin.getMouse()
bullWin.close()
