#bullsEye by joshGara

from graphics import *

def draw_ci(cX, cY, size, color, win):
    circle = Circle(Point(cX, cY), size)
    circle.setFill(color)
    circle.draw(win)

ciSz = 50


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)


draw_ci(250, 250, ciSz, "dark blue", bullWin)
draw_ci(250, 250, ciSz - 10, "white", bullWin)
draw_ci(250, 250, ciSz - 20, "dark blue", bullWin)
draw_ci(250, 250, ciSz - 30, "white", bullWin)
draw_ci(250, 250, ciSz - 40, "dark blue", bullWin)




bullWin.getMouse()
bullWin.close()
