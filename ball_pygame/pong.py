# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from sys import exit
from random import *



def pong():
    if not pygame.font: print('Warning, fonts disabled')
    if not pygame.mixer: print('Warning, sound disabled')

    pygame.init()
    pygame.display.set_caption('弹球游戏')

    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 500
    SPEED = 1
    VOLUME = 5
    SCREEN_DEFAULT_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT + 20)
    SCREEN_DEFAULT_COLOR = (255, 255 ,255)
    READY = 0

    screen = pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
    screen.fill(SCREEN_DEFAULT_COLOR)
    bg = pygame.image.load('image\\bg.jpg').convert()
    font = pygame.font.Font('font\\TORK____.ttf', 14)
    new_sound = pygame.mixer.Sound('sound\\new.wav')
    bg_sound = pygame.mixer.Sound('sound\\bg.ogg')
    bg_sound.set_volume(0.1 * VOLUME)
    bg_sound.play(-1)
    new_sound.set_volume(0.1 * VOLUME)


    balls = []
    BALL_R = 30
    BALL_COLORS = [(255,165,0),(255,0,0),(135,206,235),(178,34,34),(34,139,34)]
    BALL_POINTS = [[40, 40],[40, 300],[400, 200],[150, 150],[80, 400]]
    BALL_VELOCITY = [[1.5, 1.2],[1.4, -1.3],[-1.5, -1.1],[-1.2, 1.5],[1.3, 1.1]]

    VOLUME_POINTS = []
    VOLUME_POINTS_START = []
    VOLUME_RECT_COLORS = []
    for p in range(170, 250, 7):
        VOLUME_POINTS.append([SCREEN_WIDTH - p,SCREEN_HEIGHT + 20])
    for ps in range(175, 250, 7):
        VOLUME_POINTS_START.append([SCREEN_WIDTH - ps, SCREEN_HEIGHT])
        VOLUME_RECT_COLORS.append((randint(0, 255), randint(0, 255), randint(0, 255)))

    for i in range(len(BALL_COLORS)):
        screen.fill(SCREEN_DEFAULT_COLOR)
        b = pygame.draw.circle(screen, BALL_COLORS[i], (int(BALL_POINTS[i][0]),int(BALL_POINTS[i][1])), BALL_R)
        balls.append(b)

    while 1:
        for event in pygame.event.get():
            if event.type ==  QUIT:
                bg_sound.stop()
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    SPEED += 0.1
                elif event.key == K_DOWN:
                    SPEED -= 0.1
                elif event.key == K_LEFT:
                    if VOLUME > 0:
                        VOLUME -= 1
                elif event.key == K_RIGHT:
                    if VOLUME <= 9:
                        VOLUME += 1
                elif event.key == K_f:
                    pygame.display.set_mode(SCREEN_DEFAULT_SIZE, FULLSCREEN, 32)
                elif event.key == 27:
                    pygame.display.set_mode(SCREEN_DEFAULT_SIZE, 0, 32)
            elif event.type == MOUSEBUTTONDOWN:
                pressed_array = pygame.mouse.get_pressed()
                for index in range(len(pressed_array)):
                    if pressed_array[index]:
                        if index == 0:
                            new_sound.play(-1)
                            c_color = (randint(0, 255), randint(0, 255), randint(0, 255))
                            x, y = (BALL_R+1, BALL_R+1)
                            c_r = randint(10, 100)
                            c_v = [randint(11, 19)* 0.1, randint(11, 19) * 0.1]
                            c = pygame.draw.circle(screen, c_color, (x, y), BALL_R)
                            BALL_COLORS.append(c_color)
                            BALL_POINTS.append([x, y])
                            BALL_VELOCITY.append(c_v)
                            balls.append(c)
                        elif index == 2:
                            if len(balls) > 1:
                                balls.pop(0)
                                BALL_COLORS.pop(0)
                                BALL_POINTS.pop(0)
                                BALL_VELOCITY.pop(0)
            elif event.type == MOUSEBUTTONUP:
                new_sound.stop()

        #print(balls)
        for i in range(len(balls)):
            screen.blit(bg, (-300, -100))
            #screen.fill(SCREEN_DEFAULT_COLOR)
            for n in range(len(balls)):
                pygame.draw.circle(screen, BALL_COLORS[n], (int(BALL_POINTS[n][0]),int(BALL_POINTS[n][1])), BALL_R)
            if ((((BALL_POINTS[i][0] - BALL_R) < 0) or ((BALL_POINTS[i][0] + BALL_R) > SCREEN_WIDTH))):
                BALL_VELOCITY[i][0] = -1 * BALL_VELOCITY[i][0]
            if ((((BALL_POINTS[i][1] - BALL_R) < 0) or ((BALL_POINTS[i][1] + BALL_R) > SCREEN_HEIGHT))):
                BALL_VELOCITY[i][1] = -1 * BALL_VELOCITY[i][1]

        for j in range(len(balls)):
            for k in range(len(balls)):
                b_x = (BALL_POINTS[j][0] - BALL_POINTS[k][0])**2
                b_y = (BALL_POINTS[j][1] - BALL_POINTS[k][1])**2
                b_r =(BALL_R*2)**2
                if (round((b_x + b_y), 2) <= round(b_r, 2)):
                    temp_x = BALL_VELOCITY[j][0]
                    temp_y = BALL_VELOCITY[j][1]
                    BALL_VELOCITY[j][0] = BALL_VELOCITY[k][0]
                    BALL_VELOCITY[j][1] = BALL_VELOCITY[k][1]
                    BALL_VELOCITY[k][0] = temp_x
                    BALL_VELOCITY[k][1] = temp_y

            BALL_POINTS[j][0] += round(SPEED, 1) * BALL_VELOCITY[j][0]
            BALL_POINTS[j][1] += round(SPEED, 1) * BALL_VELOCITY[j][1]

        pygame.draw.line(screen, (165,42,42),(0, SCREEN_HEIGHT), (SCREEN_WIDTH,SCREEN_HEIGHT))
        bg_sound.set_volume(0.1 * VOLUME)
        new_sound.set_volume(0.1 * VOLUME)
        pygame.draw.rect(screen,
                         (255, 255, 255),
                         Rect((VOLUME_POINTS_START[-1][0],
                               VOLUME_POINTS_START[-1][1]),
                              (VOLUME_POINTS[-10][0] - VOLUME_POINTS_START[-1][0],
                               20)))
        for v in range(VOLUME+1):
            if v > 0:
                pygame.draw.rect(screen,
                                 VOLUME_RECT_COLORS[v],
                                 Rect((VOLUME_POINTS_START[-v][0],
                                       VOLUME_POINTS_START[-v][1]),
                                      (VOLUME_POINTS[-v][0] - VOLUME_POINTS_START[-v][0],
                                       20)))

        game_info = 'Balls: ' + str(len(balls)) + '     Speed: ' + str(round(SPEED, 2)) + '   LastBall: ' + str(round(BALL_POINTS[-1][0])) + ',' + str(round(BALL_POINTS[-1][1]))
        text = font.render(game_info, True, (255,255,255))

        volume_text = font.render('Volume: ' + str(VOLUME), True, (255, 255, 255))
        screen.blit(text, (0, SCREEN_HEIGHT+5))

        screen.blit(volume_text, (SCREEN_WIDTH - 310, SCREEN_HEIGHT+5))
        pygame.display.update()
