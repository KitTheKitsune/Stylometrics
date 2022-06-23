#HW5.py
#compares an unknown image to those of the great artists
#by Kendrick Smith

from HW5part1 import *

def main():
    ofile= open("mysteryPaintings.txt", "w")
    takeImage("mystery1",ofile)
    takeImage("mystery2",ofile)
    takeImage("mystery3",ofile)
    read()

def read():
    infile= open("mysteryPaintings.txt", "r")
    mysteryPainting=infile.readline()
    i=0
    while mysteryPainting!="":
        i=i+1
        if i<6:
            if i==1:
                image=mysteryPainting
            elif i==2:
                mysteryPainting=mysteryPainting.split()
                r=mysteryPainting[0]
                g=mysteryPainting[1]
                b=mysteryPainting[2]
            elif i==4:
                brightness=mysteryPainting
            elif i==5:
                compare(r,g,b,brightness)
        elif i<11:
            if i==6:
                image=mysteryPainting
            elif i==7:
                mysteryPainting=mysteryPainting.split()
                r=mysteryPainting[0]
                g=mysteryPainting[1]
                b=mysteryPainting[2]
            elif i==9:
                brightness=mysteryPainting
            elif i==0:
                compare(r,g,b,brightness)
        else:
            if i==11:
                image=mysteryPainting
            elif i==12:
                mysteryPainting=mysteryPainting.split()
                r=mysteryPainting[0]
                g=mysteryPainting[1]
                b=mysteryPainting[2]
            elif i==14:
                brightness=mysteryPainting
            elif i==15:
                compare(r,g,b,brightness)
def compare(r,g,b,B):
    artists= open("Paintings.txt", "r")
    text=artists.readline()
    i=0
    while text!="":
        i=i+1
        if i<6:
            if i==1:
                image1=text
            elif i==2:
                text=text.split()
                R1=text[0]
                G1=text[1]
                B1=text[2]
            elif i==4:
                Brightness1=text
        elif i<11:
            if i==6:
                image2=text
            elif i==7:
                text=text.split()
                R2=text[0]
                G2=text[1]
                B2=text[2]
            elif i==9:
                Brightness2=text
        elif i<16:
            if i==11:
                image3=text
            elif i==12:
                text=text.split()
                R3=text[0]
                G3=text[1]
                B3=text[2]
            elif i==14:
                Brightness3=text
        elif i<21:
            if i==16:
                image4=text
            elif i==17:
                text=text.split()
                R4=text[0]
                G4=text[1]
                B4=text[2]
            elif i==19:
                Brightness4=text
        elif i<26:
            if i==21:
                image5=text
            elif i==22:
                text=text.split()
                R5=text[0]
                G5=text[1]
                B5=text[2]
            elif i==24:
                Brightness5=text
        else:
            if i==26:
                image6=text
            elif i==27:
                text=text.split()
                R6=text[0]
                G6=text[1]
                B6=text[2]
            elif i==29:
                Brightness6=text
    #distance = | trained value - mystery value | / mystery value
    D=0
    D=D+abs(R1-r)/r
    D=D+abs(G1-g)/g
    D=D+abs(B1-b)/b
    Picture1=D
    D=0
    D=D+abs(R2-r)/r
    D=D+abs(G2-g)/g
    D=D+abs(B2-b)/b
    Picture2=D
    D=0
    D=D+abs(R3-r)/r
    D=D+abs(G3-g)/g
    D=D+abs(B3-b)/b
    Picture3=D
    D=0
    D=D+abs(R4-r)/r
    D=D+abs(G4-g)/g
    D=D+abs(B4-b)/b
    Picture4=D
    D=0
    D=D+abs(R5-r)/r
    D=D+abs(G5-g)/g
    D=D+abs(B5-b)/b
    Picture5=D
    D=0
    D=D+abs(R6-r)/r
    D=D+abs(G6-g)/g
    D=D+abs(B6-b)/b
    Picture6=D
    distance=[Picture1,Picture2,Picture3,Picture4,Picture5,Picture6]
    Best=min(distance).index()
    print("Picture",int(Best)+1,"is most similar to our mystery painting")
       
main()
    
