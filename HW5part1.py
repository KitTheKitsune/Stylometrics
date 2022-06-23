#HW5.py
#calculates details of the paintings of the great artists
#by Kendrick Smith

from graphics import *
def main():
    #take in image
    ofile = open("Paintings.txt", "w")
    takeImage("Rembrandt1",ofile)
    takeImage("Rembrandt2",ofile)
    takeImage("Rembrandt3",ofile)
    takeImage("DaVinci1",ofile)
    takeImage("DaVinci2",ofile)
    takeImage("DaVinci3",ofile)

def takeImage(painting,ofile):
    rgbList = []
    win=GraphWin("Image", 400, 500)
    image = Image(Point(200,250), painting+".gif")
    image.draw(win)
    theWidth = image.getWidth()
    theHeight = image.getHeight()
    pixels = theWidth * theHeight
    brightness = 0
    avR = 0
    avG = 0
    avB = 0
    for i in range(0,theWidth,2):
        for j in range(0,theHeight):
            r,g,b = image.getPixel(i,j)
            rgbList[i] =  rgbList.append([r,g,b])
            store = int(round(0.299*r + 0.587*g + 0.114*b))
            avR=r + avR
            avG=g + avG
            avB=b + avB
            brightness = brightness + store
    print(painting,file=ofile)
    print(avR/pixels,avG/pixels,avB/pixels,file=ofile)
    print('',file=ofile)
    print(brightness/pixels,file=ofile)
    print('',file=ofile)

main()
