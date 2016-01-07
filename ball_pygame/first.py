# -*- coding:utf-8 -*-
from pygame.locals import *
from func import *
import math
#from gate import *
from rotate import *
import threading
from time import ctime,sleep
import datetime
from pong import *
NUM = 0

def init():
    pygame.init()
    global info
    pygame.mixer.init()
    window_size = Rect(0, 0,640,480)
    pygame.display.set_caption('弹球碰撞')
    screen = pygame.display.set_mode(window_size.size)
    background_image = load_image('background.jpg')
    screen.blit(background_image, (0, 0))
    return screen

def start():
    global NUM
    NUM = 1
    sound_state = 1
    screen = init()
    load_text(u"开始游戏",screen,40,(320,200),(255,255,255))
    load_text(u"退出游戏",screen,40,(320,300),(255,255,255))
    load_text(u"游戏帮助",screen,40,(320,400),(255,255,255))
    back_music_file = load_sound('backmusic.mp3')
    pygame.mixer.music.load(back_music_file)
    pygame.mixer.music.play(-1, 0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        selectmode()
                    elif click(pos[0],pos[1]) == 1:
                         sound_state = -sound_state
                    elif click(pos[0],pos[1]) == 2:
                        help()
                    elif click(pos[0],pos[1]) == -1:
                        pygame.quit()
                        sys.exit()

            elif event.type == KEYDOWN:
                if event.key == 13:
                    selectlevel()
        if sound_state == 1:
            volume_image = load_image("volume1.png")
            pygame.mixer.music.unpause()
        else:
            volume_image = load_image("volume2.png")
            pygame.mixer.music.pause()
        screen.blit(volume_image,(600,0))
        pygame.display.flip()

def fail():
    screen = init()
    load_text(u"失败",screen,40,(320,100),(255,0,0))
    load_text(u"重新开始",screen,40,(320,200),(255,255,255))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        run()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def fail2():
    screen = init()
    load_text(u"失败",screen,40,(320,100),(255,0,0))
    load_text(u"重新开始",screen,40,(320,200),(255,255,255))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        test()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def selectmode():
    screen = init()
    back_img_file = load_image('back.png')
    screen.blit(back_img_file,(0,0))
    load_text(u"牛刀小试",screen,40,(320,200),(255,255,255))
    load_text(u"大展身手",screen,40,(320,300),(255,255,255))
    load_text(u"娱乐模式",screen,40,(320,400),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                       test()
                    if click(pos[0],pos[1]) == -1:
                       #run()
                       selectlevel()
                    if click(pos[0],pos[1]) == 2:
                       pygame.mixer.music.pause()
                       pong()
                    if 0 <= pos[0] <= 40 and 0 <= pos[1] <= 40:
                        start()
        pygame.display.flip()

def passgate1():
    global NUM
    screen = init()
    load_text(u"成功",screen,40,(320,100),(255,0,0))
    load_text(u"下一关",screen,40,(320,200),(255,255,255))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        NUM = NUM + 1
                        run()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def passgate2():
    global NUM
    screen = init()
    load_text(u"成功",screen,40,(320,100),(255,0,0))
    load_text(u"下一关",screen,40,(320,200),(255,255,255))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        NUM = NUM + 1
                        test()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def selectlevel():
    global NUM
    screen = init()
    back_img_file = load_image('back.png')
    screen.blit(back_img_file,(0,0))
    load_text(u"关卡选择",screen,40,(320,100),(255,255,255))
    load_text("1",screen,50,(120,200),(255,255,255))
    load_text("2",screen,50,(240,200),(255,255,255))
    load_text("3",screen,50,(360,200),(255,255,255))
    load_text("4",screen,50,(480,200),(255,255,255))
    load_text("5",screen,50,(120,300),(255,255,255))
    load_text("6",screen,50,(240,300),(255,255,255))
    load_text("7",screen,50,(360,300),(255,255,255))
    load_text("8",screen,50,(480,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if 0 <= pos[0] <= 40 and 0 <= pos[1] <= 40:
                        start()
                    else:
                        NUM = judgelevel(pos[0],pos[1])
                        run()


        pygame.display.flip()


def help():
    screen = init()
    back_img_file = load_image('back.png')
    screen.blit(back_img_file,(0,0))
    load_text(u"1.单击鼠标，小球沿着鼠标方向前进",screen,32,(320,100),(255,255,255))
    load_text(u"2.小球碰到木板或边界会发生反弹",screen,32,(320,200),(255,255,255))
    load_text(u"3.规定时间内小球碰到目标球则游戏成功",screen,32,(320,300),(255,255,255))
    load_text(u"4.娱乐模式左键加球，右键减球",screen,32,(320,400),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            pos = pygame.mouse.get_pos()
                            if 0 <= pos[0] <= 40 and 0 <= pos[1] <= 40:
                                start()

        pygame.display.flip()

def thread():
    back_music_file = load_sound('backmusic.mp3')
    pygame.mixer.music.load(back_music_file)
    pygame.mixer.music.play(-1, 0)
    sleep(1)
    #fail()

def thread2(count):
    while(1):
        if count < 0:
            return 1
        sleep(2)



def run():
    global NUM
    pygame.init()
    start = datetime.datetime.now()
    width = 640
    height = 480
    screen = pygame.display.set_mode((width,height))
    background = load_image("background.jpg")
    ball = Ball()
    if NUM == 1:
        barrierlist = [Barrier(1,o=(320,200),angle=math.pi,rad=math.pi/50,length=200,is_rotate = False,is_ud = False,is_lr = False)
                       #Barrier(2,o=(450,200),angle=5,rad=math.pi/50,length=200,is_rotate = False,is_ud = False,is_lr = False)
                       ]
        goal = Goal()
    if NUM == 2:
        barrierlist = [Barrier(1,o=(250,200),angle=0,rad=math.pi/50,length=150,is_rotate = False,is_ud = True,is_lr = False),
                       Barrier(2,o=(450,200),angle=5,rad=math.pi/50,length=200,is_rotate = False,is_ud = False,is_lr = True)
                       ]
        goal = Goal()
    if NUM == 3:
        barrierlist = [Barrier(1,o=(80,int(80*1.732)),angle=math.pi/3,length=220,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(2,o=(320,275),angle=0,length=150,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(3,o=(395,200),angle=math.pi/2,length=150,rad = 0,is_rotate = False,is_ud = False,is_lr = False)]
        goal = Goal(posx=335,posy=215)
    if NUM == 5:
        barrierlist = [Barrier(1,o=(100,300),angle=0,length=150,rad = math.pi/200,is_rotate = True,is_ud = False,is_lr = False),
                                 Barrier(2,o=(425,80),angle=math.pi/4,length=150,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                                 Barrier(3,o=(int(425+75*1.414),80),angle=-1*math.pi/4,length=150,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                                 Barrier(4,o=(int(425+75*1.414),int(80+75*1.414)),angle=math.pi/4,length=150,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                                 Barrier(5,o=(400,300),angle=0,length=300,rad = 0),
                       ]
        goal = Goal(posx=int(400+65*1.414),posy=int(105+10*1.414))
    if NUM == 4:
        barrierlist = [Barrier(1,o=(240,240),angle=math.pi/2,length=150,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                             Barrier(2,o=(400,240),angle=math.pi/2,length=80,rad = 0,D = 80, is_rotate = False,is_ud = True,is_lr = False),
                             Barrier(3,o=(320,165),angle=0,length=150,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                             Barrier(4,o=(320,315),angle=0,length=150,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                   ]
        goal = Goal(posx=325,posy=240)
    if NUM == 6:
        barrierlist = [Barrier(1,o=(180,140),angle=math.pi/4,length=round(120*1.414),rad = 0,D=40, is_rotate = False,is_ud = True,is_lr = True),
                       Barrier(2,o=(460,340),angle=math.pi/4,length=round(120*1.414),rad = 0,D=40, is_rotate = False,is_ud = True,is_lr = True),
                       Barrier(3,o=(320,80),angle=0,length=160,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(4,o=(320,400),angle=0,length=160,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(5,o=(120,240),angle=math.pi/2,length=80,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(6,o=(520,240),angle=math.pi/2,length=80,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(7,o=(180,340),angle=0,length=120,rad = math.pi/80,is_rotate = True,is_ud = False,is_lr = False),
                       Barrier(8,o=(460,140),angle=math.pi/2,length=120,rad = math.pi/80, is_rotate =True,is_ud = False,is_lr = False),
                       Barrier(9,o=(220,240),angle=0,length=120,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(10,o=(420,240),angle=0,length=120,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                   ]
        goal = Goal(posx=320,posy=240)
    if NUM == 7:
        barrierlist = [Barrier(1,o=(80,400),angle=-1*math.pi/4,length=round(160*1.414),rad = 0,D=40, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(2,o=(80,220),angle=math.pi/2,length=120,rad = 0,D=40, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(3,o=(440,260),angle=math.pi/2,length=180,rad = math.pi/60, is_rotate = True,is_ud = False,is_lr = False),
                       Barrier(4,o=(160,80),angle=math.pi/4,length=round(160*1.414),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(5,o=(400,80),angle=0,length=80,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(6,o=(500,140),angle=-1*math.pi/4,length=round(120*1.414),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(7,o=(600,200),angle=0,length=80,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(8,o=(240,240),angle=0,length=160,rad = 0, is_rotate =False,is_ud = False,is_lr = False),
                       Barrier(9,o=(320,300),angle=math.pi/2,length=120,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(10,o=(560,360),angle=0,length=160,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(11,o=(480,340),angle=math.pi/2,length=40,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                   ]
        goal = Goal(posx=600,posy=280)
    if NUM == 8:
        barrierlist = [Barrier(1,o=(80,80),angle=math.pi/4,length=round(120*1.414),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(2,o=(80,400),angle=-1*math.pi/4,length=round(120*1.414),rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(3,o=(560,80),angle=-1*math.pi/4,length=round(120*1.414),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(4,o=(560,400),angle=math.pi/4,length=round(120*1.414),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(5,o=(320,120),angle=0,length=200,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(6,o=(320,360),angle=0,length=200,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(7,o=(280,240),angle=math.pi/2,length=60,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(8,o=(360,240),angle=math.pi/2,length=60,rad = 0, is_rotate =False,is_ud = False,is_lr = False),
                       Barrier(9,o=(120,240),angle=math.pi/2,length=140,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(10,o=(520,240),angle=math.pi/2,length=140,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(11,o=(40,240),angle=math.pi/2,length=60,rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(12,o=(600,240),angle=math.pi/2,length=60,rad = 0,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(13,o=(80,180),angle=math.atan(0.5),length=40*math.sqrt(5),rad = 0, is_rotate =False,is_ud = False,is_lr = False),
                       Barrier(14,o=(560,180),angle=math.atan(0.5)*-1,length=40*math.sqrt(5),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(15,o=(560,300),angle=math.atan(0.5),length=40*math.sqrt(5),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(16,o=(80,300),angle=math.atan(0.5)*-1,length=40*math.sqrt(5),rad = 0, is_rotate = False,is_ud = False,is_lr = False),
                   ]
        goal = Goal(posx=320,posy=240)

    elif NUM > 8:
        final()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if ball.speed == [0,0]:
                        ball.speed = [int((pos[0]-ball.pos[0])/distance(pos,ball.pos)*50),int((pos[1]-ball.pos[1])/distance(pos,ball.pos)*50)]
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    esc()
        screen.blit(background,(0,0))
        for barrier in barrierlist:
            barrier.draw(screen)
        end = datetime.datetime.now()
        count = 10 - (end - start).seconds
        load_text(str(count),screen,35,(620,20),(255,255,0))
        """
        threads = []
        t1 = threading.Thread(target=thread,args=())
        t2 = threading.Thread(target=thread,args=(count))
        threads.append(t1)
        threads.append(t2)
        t1.start()
        t2.start()
        """
        if counter(count) == 1:
            fail()

        if sucess((ball.pos[0],goal.pos[0]),(ball.pos[1],goal.pos[1])) == 1:
            if NUM > 8:
                final()
            else:
                passgate1()
        ball.draw(screen,barrierlist,width,height)
        goal.draw(screen)
        pygame.display.update()
        pygame.time.delay(5)



def test():
    pygame.init()
    width = 640
    height = 480
    start = datetime.datetime.now()
    screen = pygame.display.set_mode((width,height))
    background = load_image("background.jpg")
    ball = Ball()
    goal = Goal()
    if NUM == 3:
        barrierlist = [Barrier(1, o=(320,240),angle=math.pi/4,rad=0,length=150,is_rotate = False,is_ud = False,is_lr = False),
                       Barrier(2, o=(520,240),angle=math.pi/4,rad=math.pi/100,length=150,is_rotate = True,is_ud = False,is_lr = False)]
    if NUM == 2:
        barrierlist = [Barrier(1, o=(250,200),angle=0,rad=0,length=150,is_rotate = False,is_ud = True,is_lr = False),
                       Barrier(2, o=(450,200),angle=5,rad=0,length=200,is_rotate = False,is_ud = False,is_lr = True)]
    if NUM == 1:
        barrierlist = [Barrier(1, o=(120,300),angle=math.pi/4,length=120,rad = 0,is_rotate=False,is_lr=False,is_ud=False),
                       Barrier(2, o=(520,300),angle=math.pi/4,length=120,rad = 0,is_rotate=False,is_lr=False,is_ud=False),
                       Barrier(3, o=(520,60),angle=-1*math.pi/4-math.pi/10,length=120,rad = 0,is_rotate=False,is_lr=False,is_ud=False),
                       Barrier(4, o=(220,60),angle=-1*math.atan(0.5),length=220,rad = 0,is_rotate=False,is_lr=False,is_ud=False),
                       ]
        goal = Goal(posx=280,posy=40)
    if NUM > 3:
        final()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if ball.speed == [0,0]:
                    if event.key == pygame.K_LEFT:
                        if ball.pos[0] <= 20:
                            pass
                        else:
                            ball.pos= (ball.pos[0]-20,ball.pos[1])
                    if event.key == pygame.K_RIGHT:
                        if ball.pos[0] >= 620:
                            pass
                        else:
                            ball.pos= (ball.pos[0]+20,ball.pos[1])
                if event.key == K_SPACE:
                    if ball.speed == [0,0]:
                        ball.speed = [0,5]
            if event.type == pygame.KEYDOWN:
                if event.key == 27:
                    esc2()
        screen.blit(background,(0,0))
        end = datetime.datetime.now()
        count = 10 - (end - start).seconds
        load_text(str(count),screen,35,(620,20),(255,255,0))

        if counter(count) == 1:
            fail2()
        if sucess((ball.pos[0],goal.pos[0]),(ball.pos[1],goal.pos[1])) == 1:
            passgate2()

        ball.draw(screen,barrierlist,width,height)
        goal.draw(screen)
        for barrier in barrierlist:
            barrier.draw(screen)
        pygame.display.update()
        pygame.time.delay(5)

def esc():
    screen = init()
    load_text(u"重新开始",screen,40,(320,200),(255,255,0))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        run()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def esc2():
    screen = init()
    load_text(u"重新开始",screen,40,(320,200),(255,255,0))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,0))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        test()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()

def final():
    global NUM
    screen = init()
    load_text(u"您已经通关",screen,40,(320,100),(255,0,0))
    load_text(u"重新开始",screen,40,(320,200),(255,255,255))
    load_text(u"返回主菜单",screen,40,(320,300),(255,255,255))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type ==  MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                if judgeClick(pressed_array) == 0:
                    pos = pygame.mouse.get_pos()
                    if click(pos[0],pos[1]) == 0:
                        NUM = 1
                        run()
                    elif click(pos[0],pos[1]) == -1:
                        start()
        pygame.display.flip()


if __name__ == '__main__':
    start()
