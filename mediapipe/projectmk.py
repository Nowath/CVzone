import pygame
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy
import random
import time


pygame.init()

#clock for fps
fps = 30
clock = pygame.time.Clock()

#Webcam
cap = cv2.VideoCapture(1)
cap.set(3,800) #width
cap.set(4,500) #height
detector = HandDetector(detectionCon = 0.8, maxHands = 2)

screen = pygame.display.set_mode((800,500))
title = pygame.display.set_caption('My Game')

#font
font1 = pygame.font.Font('./font/LINESeedSans_Rg.ttf',30)

#img
BOAT_SIZE = (75,75)
BOOM_SIZE = (75,75)
BEACH_SIZE = (800,500)
#BALLON_IMG_SIZE = (75,150)
boat_img = pygame.image.load('./img/BOAT/PNG/Boat4_water_animation_color2/Boat4_water_frame1.png').convert_alpha()
boom_img = pygame.image.load('./img/BOOM.png').convert_alpha()
beach_img = pygame.image.load('./img/Beach.png').convert_alpha()
boom_img = pygame.transform.smoothscale(boom_img,BOOM_SIZE)
boat_img = pygame.transform.smoothscale(boat_img,BOAT_SIZE)
beach_img = pygame.transform.smoothscale(beach_img,BEACH_SIZE)
beach_img = pygame.transform.rotate(beach_img,180)
boat_img = pygame.transform.rotate(boat_img,90)
#ballon_img = pygame.image.load('./img/ballon.png').convert_alpha()
#ballon_img = pygame.transform.smoothscale(ballon_img,BALLON_IMG_SIZE)
#rectballon = ballon_img.get_rect()

rectNew  = pygame.Rect(500, 0, 200, 200)

score = 0
score_text = font1.render('SCORE : {}   WIN :10'.format(score),True,(0,0,0))

Time = 0

running = True
start_time = time.time()
final_time = 30

boat1_pos_x = 0
boat1_pos_y = random.randint(100,400)

boom1_pos_x = 0
boom1_pos_y = random.randint(100,400)

while running:
    time_remain = int(final_time - (time.time() - start_time))
    for event in pygame.event.get():
            if(event.type == pygame.QUIT) :
                running = False
                cap.release()
    if (time_remain <= 0):
        screen.fill((0,0,0))
        game_over_text = font1.render('Game Over!',True,(255,255,255))
        score_text2 = font1.render('SCORE : {}'.format(score),True,(255,255,255))
        screen.blit(game_over_text,(300,250))
        screen.blit(score_text2,(325,300))
        cap.release()
    elif (score == 10):
        screen.fill((255,255,255))
        game_win_text = font1.render('WIN!',True,(0,0,0))
        screen.blit(game_win_text,(350,250))
        final_time = 1000
        cap.release()
    elif (score < 0):
        screen.fill((0,0,0))
        game_over_text = font1.render('Game Over!',True,(255,255,255))
        score_text2 = font1.render('SCORE : {}'.format(score),True,(255,255,255))
        screen.blit(game_over_text,(300,250))
        screen.blit(score_text2,(325,300))
        cap.release()
    else:
        ret,frame = cap.read()
        frame = cv2.flip(frame,1)
        hands,frame = detector.findHands(frame, flipType=False)
        
        boat1_hit_point = pygame.Rect(boat1_pos_x,boat1_pos_y,50,50)
        boom1_hit_point = pygame.Rect(boom1_pos_x,boom1_pos_y,50,50)
        
        if(boat1_pos_x > 900):
            boat1_pos_x = random.randint(-350,-100)
            boat1_pos_y = random.randint(100,400)
        else:
            boat1_pos_x += 10
        if(boom1_pos_x > 800):
            boom1_pos_x = random.randint(-600,-300)
            boom1_pos_y = random.randint(100,400)
        else:
            boom1_pos_x += 10
        if hands:
            hand1 = hands[0]
            hand_x,hand_y,hand_z = hand1['lmList'][8]
            hand_hit_point = pygame.Rect(hand_x,hand_y,100,100)
            if hand_hit_point.colliderect(boat1_hit_point):
                score += 1
                score_text = font1.render('SCORE : {}'.format(score),True,(0,0,0)) 
                boat1_pos_y = random.randint(100,400)
                boat1_pos_x = 0
            elif(hand_hit_point.colliderect(boom1_hit_point)):
                score -= 2
                score_text = font1.render('SCORE : {}'.format(score),True,(0,0,0)) 
                boom1_pos_y = random.randint(100,400)
                boom1_pos_x = 0
        
        # Convert Webcam
        frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        frameRGB = numpy.rot90(frameRGB)
        
        img = pygame.surfarray.make_surface(frameRGB).convert()
        img = pygame.transform.flip(img,True,False)
        img = pygame.transform.scale(img,(800,600))
        
        #print(rectballon.colliderect(rectNew))
        #boat1_pos_x += 5
        
        #Game Scene
        screen.blit(img,(0,0))
        screen.blit(boat_img,(boat1_pos_x,boat1_pos_y))
        screen.blit(boom_img,(boom1_pos_x,boom1_pos_y))
        screen.blit(beach_img,(80,0))
        screen.blit(score_text,(0,5))
        Time_text = font1.render('Time : {}'.format(time_remain),True,(0,0,0))
        screen.blit(Time_text,(650,5))
    #update screen
    pygame.display.update()
    clock.tick(fps)
pygame.quit()