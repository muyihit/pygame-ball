# -*- coding:utf-8 -*-
import os
import sys
import pygame
import math
from pygame.locals import *
from first import *

fp = open('info.txt')

def distance(x,y):
    return math.sqrt((x[0]-y[0])*(x[0]-y[0])+(x[1]-y[1])*(x[1]-y[1]))
def pointToline(x,y,z):
    a = z[1] - y[1]
    b = y[0] - z[0]
    c = z[1]*y[0] - z[0]*y[1]
    return math.fabs(a * x[0] + b * x[1] + c) / math.sqrt(a * a + b * b)

def mo(pos):
    return math.sqrt(pos[0]*pos[0]+pos[1]*pos[1])

def unit_vector(pos):
    return pos[0]/mo(pos),pos[1]/mo(pos)

def normal_vector(pos):
    return pos[1],-1*pos[0]

def vector_multi(pos,times):
    return pos[0]*times,pos[1]*times

def vector_reduce(pos,pos1):
    return pos[0]-pos1[0],pos[1]-pos1[1]

def inner_product(pos1,pos2):
    return pos1[0]*pos2[0] + pos1[1]*pos2[1]

def is_collineated(pos,pos1,pos2):
    v1 = (pos[0]-pos1[0],pos[1]-pos1[1])
    v2 = (pos2[0]-pos1[0],pos2[1]-pos1[1])
    return inner_product(normal_vector(v1),v2) == 0

def get_angle(v1,v2):
    a,b = mo(v1),mo(v2)
    return math.fabs(inner_product(v1,v2)*1.0/(a*b))

def getwhichaspect(pos1,pos2,width,height,angle):
    ang = math.atan(height*1.0/width)
    x,y = math.cos(angle)*10,-1*math.sin(angle)*10
    x1,y1 = (pos2[0] - pos1[0])*10,(pos2[1] - pos1[1])*10
    return get_angle((x,y),(x1,y1)) >= math.cos(ang)

def crash_angle(speed,pos1,pos2):
    v = (pos1[0]-pos2[0],pos1[1]-pos2[1])
    value = vector_multi(unit_vector(v),2*inner_product(unit_vector(v),speed))
    return vector_reduce(value,v)

def crash_width(speed,angle):
    value = 2*(speed[0]*math.cos(angle)-speed[1]*math.sin(angle))
    centerx,centery = value * math.cos(angle),-1*value*math.sin(angle)
    new_speed = [centerx - speed[0],centery - speed[1]]
    return new_speed

def crash_height(speed,angle):
    angle = angle+math.pi/2
    reflect = inner_product(speed,(math.cos(angle),-1*math.sin(angle)))
    value = vector_multi((math.cos(angle),-1*math.sin(angle)),2*reflect)
    return value[0]-speed[0],value[1]-speed[1]
def pointToline(x,y,z):
    a = z[1] - y[1]
    b = y[0] - z[0]
    c = z[1]*y[0] - z[0]*y[1]
    return math.fabs(a * x[0] + b * x[1] + c) / math.sqrt(a * a + b * b)
def crash_width_rotate(speed,angle,pos,pos1):
    dis = pointToline(pos,pos1,(pos1[0]+math.cos(angle)*10,pos1[1]-math.sin(angle)*10))
    xuan = mo((pos1[0]-pos[0],pos1[1]-pos[1]))
    length = math.sqrt(xuan*xuan-dis*dis)
    speed_add = (length*-1*math.sin(angle),length*-1*math.cos(angle))
    new_speed = crash_width(speed,angle)
    return speed_add[0]+new_speed[0],speed_add[1]+new_speed[1]
def transform(pos,speed,radius,pos1,angle,width,height,point_list,is_rotate):
    for point in point_list:
        if is_collineated(pos,pos1,point):
            return crash_angle(speed,point,pos)
    if getwhichaspect(pos,pos1,width,height,angle):
        return crash_height(speed,angle)
    if is_rotate:
        return crash_width_rotate(speed,angle,pos,pos1)
    return crash_width(speed,angle)
def click(x,y):
    if 240 <= x <= 400 and 174 <= y <= 227:
        return 0;
    elif 240 <= x <= 400 and 274 <= y <= 327:
        return -1;
    elif 600 <= x <= 640 and 0 <= y <= 40:
        return 1;
    elif 240 <= x <= 400 and 374 <= y <= 427:
        return 2;

def init():
    pygame.init()
    pygame.mixer.init()
    window_size = Rect(0, 0,640,480)
    pygame.display.set_caption('弹球碰撞')
    screen = pygame.display.set_mode(window_size.size)
    background_image = load_image('background.jpg')
    screen.blit(background_image, (0, 0))
    return screen

def load_image(pic_name):
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(current_dir, 'image', pic_name)
    return pygame.image.load(path).convert()

def load_sound(soundfile_name):
    current_dir = os.path.split(os.path.abspath(__file__))[0]
    path = os.path.join(current_dir, 'sound', soundfile_name)
    return path


def load_text(txt,screen,size,pos,color):
    font1 = pygame.font.SysFont('stsong',size)
    text = font1.render(txt,True,color)
    text_pos = text.get_rect()
    text_pos.center = (pos[0],pos[1])
    screen.blit(text,text_pos)
    return screen

def load_txt(txt,screen,size,color):
    font1 = pygame.font.SysFont('stsong',size)
    text = font1.render(txt,True,color)
    text_pos = text.get_rect()
    screen.blit(text,text_pos)
    return screen

def judgeClick(pressed_array):
    for index in range(len(pressed_array)):
        if pressed_array[index]:
            if index == 0:
                return 0
            elif index == 1:
                return 1
            else:
                return 2

def sucess(pos1,pos2):
    if distance((pos1[0],pos2[0]),(pos1[1],pos2[1])) <= 40:
        return 1

def counter(count):
    if count <= 0:
        return 1

def judgelevel(x,y):
    if 109 <= x <= 131 and 167 <= y <= 233:
        return 1;
    elif 229 <= x <= 251 and 167 <= y <= 233:
        return 2;
    elif 349 <= x <= 371 and 167 <= y <= 233:
        return 3;
    elif 469 <= x <= 491 and 167 <= y <= 233:
        return 4;
    if 109 <= x <= 131 and 267 <= y <= 333:
        return 5;
    elif 229 <= x <= 251 and 267 <= y <= 333:
        return 6;
    elif 349 <= x <= 371 and 267 <= y <= 333:
        return 7;
    elif 469 <= x <= 491 and 267 <= y <= 333:
        return 8;