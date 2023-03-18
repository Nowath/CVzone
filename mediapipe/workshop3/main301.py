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
BACKGROUND_IMG_SIZE = (800,500)
BOAT_SIZE = (75,75)
#BALLON_IMG_SIZE = (75,150)
background_img = pygame.image.load('./img/NOA.png').convert_alpha()
background_img = pygame.transform.smoothscale(background_img,BACKGROUND_IMG_SIZE)
boat_img = pygame.image.load('./img/BOAT/PNG/Boat4_water_animation_color2/Boat4_water_frame1.png').convert_alpha()
boat_img = pygame.transform.smoothscale(boat_img,BOAT_SIZE)
boat_img = pygame.transform.rotate(boat_img,180)
#ballon_img = pygame.image.load('./img/ballon.png').convert_alpha()
#ballon_img = pygame.transform.smoothscale(ballon_img,BALLON_IMG_SIZE)
#rectballon = ballon_img.get_rect()

rectNew  = pygame.Rect(500, 0, 200, 200)

score = 0
score_text = font1.render('SCORE : {}'.format(score),True,(0,0,0))

Time = 0

running = True
start_time = time.time()
final_time = 30

boat1_pos_x = random.randint(100,700)
boat1_pos_y = 600

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
    else:
        ret,frame = cap.read()
        frame = cv2.flip(frame,1)
        hands,frame = detector.findHands(frame, flipType=False)
        
        boat1_hit_point = pygame.Rect(boat1_pos_x,boat1_pos_y,50,50)
        
        if(boat1_pos_y < -100):
            boat1_pos_y = 500
            boat1_pos_x = random.randint(100,700)
        else:
            boat1_pos_y -= 10
            
        if hands:
            hand1 = hands[0]
            hand_x,hand_y,hand_z = hand1['lmList'][8]
            hand_hit_point = pygame.Rect(hand_x,hand_y,100,100)
            if hand_hit_point.colliderect(boat1_hit_point):
                score += 1
                score_text = font1.render('SCORE : {}'.format(score),True,(0,0,0)) 
                boat1_pos_y = 500
                boat1_pos_x = random.randint(100,700)
        
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
        screen.blit(background_img,(0,5))
        screen.blit(boat_img,(boat1_pos_x,boat1_pos_y))
        screen.blit(score_text,(0,5))
        Time_text = font1.render('Time : {}'.format(time_remain),True,(0,0,0))
        screen.blit(Time_text,(650,5))
    #update screen
    pygame.display.update()
    clock.tick(fps)
pygame.quit()