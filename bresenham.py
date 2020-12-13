

# Bresenham Line drawing algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys


def init():
    glClearColor(0.0,0.0,0.1,1.0)
    gluOrtho2D(-50.0,50.0,-50.0,50.0)

def draw(x1,y1,x2,y2):

    dx = x2-x1
    dy = y2-y1
    m = dy/dx                   # slope of the line

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)
    glPointSize(5.0)
    glBegin(GL_POINTS)

    if m<1:

        glVertex2f(x1,y1)
        p = (2*dy)-dx
        while x1<x2:
            x1+=1
            if p<0:
                p = p+(2*dy)
            else:
                y1+=1
                p = p+(2*dy)-(2*dx)
            print(x1,y1)
            glVertex2f(x1,y1)
    else:
        
        glVertex2f(x1,y1)
        p = (2*dx)-dy
        while y1<y2:
            y1+=1
            if p<0:
                p = p+(2*dx)
            else:
                x1+=1
                p = p+(2*dx)-(2*dy)
            print(x1,y1)
            glVertex2f(x1,y1)

    glEnd()
    glFlush()

def main():

    print("Enter A(x1,y1) and B(x2,y2) of the line to be drawn ")

    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("Bresenham Algorithm")
    glutDisplayFunc(lambda: draw(x1,y1,x2,y2))
    init()
    glutMainLoop()

main()