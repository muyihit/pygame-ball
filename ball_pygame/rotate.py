# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 11:06:51 2015

@author: xuezheng
"""

import os,sys
import pygame
import random
import math
from pygame.locals import *
import hanshu

def distance(x,y):
    return math.sqrt((x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1]))
def pointToline(x,y,z):
    a = z[1] - y[1]
    b = y[0] - z[0]
    c = z[1]*y[0] - z[0]*y[1]
    return math.fabs(a * x[0] + b * x[1] + c) / math.sqrt(a * a + b * b)
    
def get_angle(x):
    a = hanshu.vector_length(x)
    return -1*math.acos(math.fabs(x[0])/a) if x[1]*x[0]>=0 else math.acos(math.fabs(x[0])/a)
    
class Barrier(object):
    def __init__(self, ID, o, angle, rad, is_rotate = False, is_ud = False,is_lr = False, width=10, length = 200,D = 100):

        self.o = o
        self.rad = rad
        self.angle = angle
        self.length = length
        
        self.width = width
        self.is_ud = is_ud
        self.is_lr = is_lr
        self.color = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        self.is_rotate = is_rotate
        
        self.start = hanshu.transform(self.o, self.angle, self.length)[0]
        self.end = hanshu.transform(self.o, self.angle, self.length)[1]
        self.lr_move = (1,0)
        self.ud_move = (0,1)
        
        self.ID = ID
        self.D = D
    def rotate(self):
        v = (self.start[0]-self.end[0],self.start[1]-self.end[1])
        angle = get_angle(v) + self.rad
        center = ((self.start[0] + self.end[0])/2.0, (self.start[1] + self.end[1])/2.0)
        temp = hanshu.vector_length(v)/2.0
        self.start = (center[0]+temp*math.cos(angle),center[1] - temp * math.sin(angle))
        self.end = (center[0]-temp*math.cos(angle),center[1] + temp * math.sin(angle))
    def lr(self):
        
        if self.start[0] < self.D or self.end[0] < self.D:
            self.lr_move = (-self.lr_move[0], -self.lr_move[1])
        if self.start[0] > 640-self.D or self.end[0] > 640-self.D:
            self.lr_move = (-self.lr_move[0], -self.lr_move[1])
            
        self.start = hanshu.vector(self.start, self.lr_move, '+')
        self.end = hanshu.vector(self.end, self.lr_move, '+')
        
    def ud(self):
        
        if self.start[1] < self.D or self.end[1] < self.D:
            self.ud_move = (-self.ud_move[0], -self.ud_move[1])
        if self.start[1] > 480-self.D or self.end[1] > 480-self.D:
            self.ud_move = (-self.ud_move[0], -self.ud_move[1])
            
        self.start = hanshu.vector(self.start, self.ud_move, '+')
        self.end = hanshu.vector(self.end, self.ud_move, '+')
        
    def draw(self,surface):
        if self.is_rotate:
            self.rotate()
        if self.is_lr:
            self.lr()
        if self.is_ud:
            self.ud()
        pygame.draw.line(surface,self.color,self.start,self.end, self.width)

class Goal(object):
    def __init__(self, posx=320, posy=0,radius = 20):
        self.pos = (posx,posy)
        self.radius = radius
    def draw(self,surface):
        pygame.draw.circle(surface,(0,255,255),self.pos,self.radius,0)

class Ball(object):
    def __init__(self, posx=320, posy=460,radius = 20,speed = [0,0]):
        self.pos = (posx,posy)
        self.radius = radius
        self.speed = speed
        self.is_lunch = False
        self.is_next = True
        self.ID = 0
    def set_speed(self,speed):
        self.speed = (speed[0]*.6,speed[1]*.6)
    def move(self,surface,width,height):
        self.pos = (self.pos[0]+self.speed[0],self.pos[1]+self.speed[1])
        if self.pos[0]-self.radius < 0 or self.pos[0] + self.radius > width:
            self.speed[0]*=-1
            self.ID = 0
        if self.pos[1]-self.radius < 0 or self.pos[1] + self.radius > height:
            self.speed[1]*=-1
            self.ID = 0
    def draw(self,surface,barrier_list,width,height):
        
        self.move(surface,width,height)
        self.collision(barrier_list)
        pygame.draw.circle(surface,(0,221,30),self.pos,self.radius,0)
    def collision(self,barrier_list):
        if not barrier_list:
            pass
        else:
            for barrier in barrier_list:
                result = hanshu.boom(self.pos, self.speed, self.radius, barrier.start, barrier.end, barrier.rad, self.ID, barrier.ID)
                self.speed = [int(result[0][0]), int(result[0][1])]
                self.ID = result[1]
