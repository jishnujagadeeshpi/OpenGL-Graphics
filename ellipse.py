
# Ellipse drawing algorithms

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
    glClearColor(0.0,0.0,0.0,1.0)
    gluOrtho2D(-500.0,500.0,-500.0,500.0)

def setpixel(x,y):
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    

def nonpolar(xc,yc,xr,yr):

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.0)

    if xr>yr:
        x = xr
        y = 0
        setpixel(x+xc,y+yc)
        setpixel(-x+xc,-y+yc)

        while x>0:
            x=x-0.1
            y=(yr*math.sqrt(1-(x/xr)*(x/xr)))
            setpixel(x+xc,y+yc)
            setpixel(-x+xc,y+yc)
            setpixel(x+xc,-y+yc)
            setpixel(-x+xc,-y+yc)
    else:
        x=0
        y=yr
        setpixel(x+xc,y+yc)
        setpixel(-x+xc,-y+yc)

        while y>0:
            y=y-0.1
            x=((xr*math.sqrt(1-(y/yr)*(y/yr))))
            setpixel(x+xc,y+yc)
            setpixel(-x+xc,y+yc)
            setpixel(x+xc,-y+yc)
            setpixel(-x+xc,-y+yc)
    glFlush()

def polar(xc,yc,xr,yr):

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glPointSize(4.0)

    theta=0
    pi=math.pi

    for i in range(90):
        x=xr*math.cos(pi/180*i)
        y=yr*math.sin(pi/180*i)
        setpixel(x+xc,y+yc);
        setpixel(-x+xc,y+yc)
        setpixel(-x+xc,-y+yc)
        setpixel(x+xc,-y+yc)
    glFlush()

def main():

    print(" Enter the (xc,yc) coordinate ")
    xc = int(input())
    yc = int(input())
    print("\n Enter the length of radius in x and y axis ")
    xr = int(input())
    yr = int(input())
    c = 0
    c = int(input("\n 1 Nonpolar method\n 2 Polar method\n "))

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)

    if c==1:
        glutCreateWindow(" Nonpolar method ")
        glutDisplayFunc(lambda: nonpolar(xc,yc,xr,yr))
        init()
        glutMainLoop()
    elif c==2:
        glutCreateWindow(" Polar method ")
        glutDisplayFunc(lambda: polar(xc,yc,xr,yr))
        init()
        glutMainLoop()
    else:
        print("Invalid choice")
        exit()

main()
