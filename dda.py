
# DDA line algorithm

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math
import sys


def init():
    glClearColor(0.0,0.0,0.1,1.0)             # for setting the background color
    gluOrtho2D(-50.0,50.0,-50.0,50.0)         # for setting the 2d plane

def draw(x1,y1,x2,y2):                        # function for plotting the line

    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0,1.0,1.0)                    # Color of the line to be drawn
    glPointSize(5.0)                          # Size of the point to be plotted
    glBegin(GL_POINTS)

    dx = x2-x1
    dy = y2-y1

    if abs(dx)>abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)
    xinc = dx/steps
    yinc = dy/steps

    for k in range(0,steps+1):
        glVertex2f(round(x1),round(y1))
        print(round(x1),round(y1))
        x1+=xinc
        y1+=yinc

    glEnd()
    glFlush()


def main():

    print("Enter A(x1,y1) and B(x2,y2) of the line to be drawn ")                # user inputs

    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(50,50)
    glutCreateWindow("DDA Algorithm")                                           # name of the window
    glutDisplayFunc(lambda: draw(x1,y1,x2,y2))                                  # calling the plotting function
    init()
    glutMainLoop()

main()
