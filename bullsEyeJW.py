
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

rinS = False

while rinS == False:
    try:
        numB = int(input("How many bullsEyes would you like to have?"))
        if numB > 0:
            
            rinS = True
        else:
            print ("Trying using a Positive interger.")

    except ValueError:
        print("You should try using a whole number.")
        


bullWin = GraphWin("BullsEye", ciSz*10, ciSz*10)
bullWin.setCoords(0, 0, ciSz*10, ciSz*10)

for j in range (numB):
    ranX = randint(ciSz, ciSz * 9)
    ranY = randint(ciSz, ciSz * 9)
    ranSiz = randint(1, 20)
    ranR = randint(0,255)
    ranB = randint(0,255)
    ranG = randint(0,255)
    bColor1 = color_rgb(ranR, ranB, ranG)
    draw_be(ranX, ranY, ranSiz, 4, bColor1, "black", bullWin)


bullWin.getMouse()
bullWin.close()
