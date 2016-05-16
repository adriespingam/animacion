# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:03:19 2016

@author: adrian
"""
from OpenGL.GLUT import *
from OpenGL.GL import *
from OpenGL.GLU import *
from time import sleep 
year = 0
day =0.0
partes=0
giro=0.0
def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)
def mueve():
    global partes 
    partes+=0.5
    glutPostRedisplay()

def display():
    global partes,day,giro,year
    if partes==360.0: 
        partes=0.0
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    
    glPushMatrix()
    glScalef(0.5,0.5,0.5)
    
    glPushMatrix()
    glRotatef (GLfloat(day), 1.0, 1.0, 0.0)
    glColor3f(1.0,1.0,0.0)
    glutSolidSphere(1, 16, 16)
    glPopMatrix()
    
    glPushMatrix() 
    glRotatef (partes, 0.0, 1.0, 0.0) 
    glTranslatef (2.0, 0.0, 0.0) 
    glColor3f(1.0,0.35,1.0) 
    glutSolidSphere(0.2, 10, 8)
    glPopMatrix()
    
    glPushMatrix() 
    glRotatef (partes, 0.0, 1.0, 0.0) 
    glTranslatef (1.5, 0.0, 0.0)     
    glScalef(0.5,0.5,0.5) 
    glColor3f(1.0,0.5,1.0) 
    glutSolidSphere(0.2, 10, 8)
    glPopMatrix() 
    
    glPushMatrix() 
    glRotatef (partes, 0.0, 1.0, 0.0) 
    glTranslatef (-1.5, 0.0, 0.0) 
    glScalef(0.5,0.5,0.5) 
    glColor3f(0.2,0.5,1.0) 
    glutSolidSphere(0.2, 10, 8) 
    glPopMatrix() 
 
    glPushMatrix() 
    glRotatef (partes, 0.0, 1.0, 0.0) 
    glTranslatef (-2.0, 0.0, 0.0)              
    glScalef(1.5,1.5,1.5) 
    glColor3f(0.304,0.2,1.0) 
    glutSolidSphere(0.2, 10, 8) 
    glPopMatrix() 
    
    
    glPopMatrix() 
    
    glutSwapBuffers() 
    sleep(0.02) 
    mueve()
    
def reshape (w,h):
    glViewport (0, 0, GLsizei(w), GLsizei(h))
    glMatrixMode (GL_PROJECTION)
    glLoadIdentity ()
    h_float=GLfloat (h)
    w_float=GLfloat(w)
    gluPerspective(60.0, w/h, 1.0, 20.0)
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity()
    gluLookAt (0.0, 4.0,5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0) 

def keyboard (key,x,y): 
    global day,year
    if  key ==  'd': 
        day = (day + 10) % 360 
        glutPostRedisplay() 
     
    if  key ==  'D': 
        day = (day - 10) % 360 
        glutPostRedisplay() 
     
    if  key ==  'y': 
        year = (year + 5) % 360 
        glutPostRedisplay() 
     
    if  key ==  'Y': 
        year = (year - 5) % 360 
        glutPostRedisplay()  
     
    if  key ==  'q': 
        sys.exit()  

glutInit(sys.argv) 
glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB) 
glutInitWindowSize (1600., 800) 
glutInitWindowPosition (0, 0) 
glutCreateWindow ("Robot que baila") 
init () 
glutDisplayFunc(display) 
glutReshapeFunc(reshape) 
glutKeyboardFunc(keyboard) 
glutMainLoop() 
