
# Midpoint circle algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)

def circle(r,xc,yc):

    xcoordinates=[]
    ycoordinates=[]
    xcoordinates=xcoordinates+[-r+xc,r+xc,0+xc,0+xc]
    ycoordinates=ycoordinates+[0+yc,0+yc,-r+yc,r+yc]
    p=1-r
    x=0
    y=r
    while x<y:
        x=x+1
        if p<0:
            p=p+(2*x)+1
        else:
            y=y-1
            p=p+(2*x)-(2*y)+1
        xcoordinates=xcoordinates+[x+xc,-x+xc,x+xc,-x+xc,y+xc,-y+xc,y+xc,-y+xc]
        ycoordinates=ycoordinates+[y+yc,y+yc,-y+yc,-y+yc,x+yc,x+yc,-x+yc,-x+yc]

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,1.2,0.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)
    for i in range(len(xcoordinates)):
        glVertex2f(xcoordinates[i],ycoordinates[i])
        print(xcoordinates[i],ycoordinates[i])
    glEnd()
    glFlush()

def main():

    r = int(input("Enter the radius of the circle "))
    print("Enter the coordinates of the center (xc,yc) ")
    xc = int(input())
    yc = int(input())

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow(" Midpoint Circle Algorithm")
    glutDisplayFunc(lambda: circle(r,xc,yc))
    init()
    glutMainLoop()

main()