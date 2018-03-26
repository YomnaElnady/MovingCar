from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
import numpy as np
x=0
y=0
angle=0
def myInit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)

def blocks(xp):
    glLoadIdentity()
    glColor3f(1, 1, 1)
    glTranslate(xp+y, 0, 1)
    glScale(1.5, 0.1, 1)
    glutSolidCube(2)

def draw():
    global y
    global x
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)


    glLoadIdentity()
    glColor3f(0,0,0)
    glTranslate(y, 0.25 * 5, 2)
    glScale(20, 0.5, 3)
    glutSolidCube(2)

    blocks(-20)
    blocks(-15)
    blocks(-10)
    blocks(-5)
    blocks(0)
    blocks(5)
    blocks(10)
    blocks(15)
    blocks(20)

    glLoadIdentity()
    glColor3f(1, 0, 0)
    glTranslate(x, 0, 0)
    glScale(1, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glTranslate(x, 0.25 * 5, 0)
    glScale(0.5, 0.25, 0.5)
    glutSolidCube(5)

    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x + 2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x - 2.5, -2.5 * 0.25, 2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)

    glLoadIdentity()
    glColor3f(0, 0, 1)
    glTranslate(x + 2.5, -2.5 * 0.25, -2.5 * 0.5)
    glRotatef(angle, 0, 0, 1)
    glutWireTorus(0.125, 0.5, 12, 8)
# hidden Torus..
#   glLoadIdentity()
#   glColor3f(0, 0, 1)
#   glTranslate(x - 2.5, -2.5 * 0.25, -2.5 * 0.5)
#   glRotatef(angle, 0, 0, 1)
#   glutWireTorus(0.125, 0.5, 12, 8)



    if x <= 6:
       x+=0.001
       angle-=0.1
    else:
       x= -6
    if y<=5:
       y+=0.0005
    else:
       y=0
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutCreateWindow(b"car")
glutInitWindowSize(500,500)
myInit()
glutDisplayFunc(draw)
glutIdleFunc(draw)
glutMainLoop()
