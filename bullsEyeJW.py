#bullsEye by joshGara

from graphics import *

ciSz = 50


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)

Circle  = Circle(Point(250, 250), 30)
Circle.setFill(color_rgb(34,139,34))
Circle.draw(bullWin)

bullWin.getMouse()
bullWin.close()
