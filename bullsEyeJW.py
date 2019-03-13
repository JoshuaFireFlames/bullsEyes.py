#bullsEye by joshGara

from graphics import *

def draw_ci(cX, cY, size, color, bullWin):
    circle = Circle(Point(cX, cY),Point(cX, cY))
    circle.setFill(color)
    circle.draw(bullWin)

ciSz = 50


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)

circle  = Circle(Point(250, 250), 30)
circle.setFill(color_rgb(34,139,34))
circle.draw(bullWin)

bullWin.getMouse()
bullWin.close()
