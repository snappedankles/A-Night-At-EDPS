#You can find all of the performance task information in Brightspace. Be sure to complete and submit the Software Design portion of this task in Brightspace before you start programming.

import pygame
import sys
import os
import random
import time
from timeit import default_timer as timer
from pygame import mixer
import pygame.mixer

pygame.mixer.init()

def audio (sound, volume):
  
  pygame.mixer.music.load(sound)
  pygame.mixer.music.set_volume(volume)  
  pygame.mixer.music.play(0, 0.0)


#initialize pygame
pygame.init()
width = 800
height = 600
audio('sounds/opencams.mp3',1)
#screen variables
screen = pygame.display.set_mode((width, height),pygame.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()
screenControl = 0
#colours
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
YELLOW = (255,255,0)
c = (255, 255, 255)
v = (0, 0, 0)
c2 = (255, 255, 255)
v2 = (0, 0, 0)
clr = (0, 255, 0)
#enemy character variables
nmySpot = 0
nmysizeX = 70
nmysizeY = 160
nmyX = 100
nmyY = 100
nmylve = 0
nmywin = []
nmywntme = 0
nmymve = 0
nmyDoor = 1
nmyWndw = 0
nmymve2 = 0
nmypath = []
nmypath.append(nmyDoor)
nmypath.append(nmyWndw)
#player variables
flashlightTime = 0
doorclose = False
doorholdtime = 0
#images
bkgrndImg = pygame.image.load('images/background.jpg')
bkgrndImg = pygame.transform.scale(bkgrndImg, (width, height))
bkgrnd = pygame.Rect((0, 0), (width, height))

deskImg = pygame.image.load('images/desk.png')
deskImg = pygame.transform.scale(deskImg, (600, 350))
desk = pygame.Rect((0, 410), (350, 250))

computerImg = pygame.image.load('images/computer.png')
computerImg = pygame.transform.scale(computerImg, (250, 250))
computer = pygame.Rect((50, 280), (350, 250))

compscrnImg = pygame.image.load('images/compscreen.png')
compscrnImg = pygame.transform.scale(compscrnImg, (150, 100))
compscrn = pygame.Rect((140, 330), (160, 100))

staticImg = pygame.image.load('images/staticscreen.jpg')
staticImg = pygame.transform.scale(staticImg, (width, height))
static = pygame.Rect((0, 0), (width, height))

cam1Img = pygame.image.load('images/cam1.jpg')
cam1Img = pygame.transform.scale(cam1Img, (width, height))
camera1 = pygame.Rect((0, 0), (width, height))

cam2Img = pygame.image.load('images/cam2.jpg')
cam2Img = pygame.transform.scale(cam2Img, (width, height))
camera2 = pygame.Rect((0, 0), (width, height))

cam3Img = pygame.image.load('images/cam3.jpg')
cam3Img = pygame.transform.scale(cam3Img, (width, height))
camera3 = pygame.Rect((0, 0), (width, height))

hallflshImg = pygame.image.load('images/fnlhall.jpg')
hallflshImg = pygame.transform.scale(hallflshImg, (width, height))
hallflsh = pygame.Rect((0, 0), (width, height))

halldrkImg = pygame.image.load('images/halldrk.jpg')
halldrkImg = pygame.transform.scale(halldrkImg, (width, height))
halldrk = pygame.Rect((0, 0), (width, height))

nmyImg = pygame.image.load('images/nmy.png')

doorImg = pygame.image.load('images/door.jpg')
doorImg = pygame.transform.scale(doorImg, (width, height))

wndwImg = pygame.image.load('images/window.jpg')
wndwImg = pygame.transform.scale(wndwImg, (width, height))

wndwflshImg = pygame.image.load('images/wndwflsh.jpg')
wndwflshImg = pygame.transform.scale(wndwflshImg, (width, height))

clsdwndwImg = pygame.image.load('images/clsdwndw.png')
clsdwndwImg = pygame.transform.scale(clsdwndwImg, (width, height))

frmRct = pygame.Rect((0, 0), (width, height))

frmImg1 = pygame.image.load('images/frame1death.gif')
frmImg1 = pygame.transform.scale(frmImg1, (width, height))

frmImg2 = pygame.image.load('images/frame2death.gif')
frmImg2 = pygame.transform.scale(frmImg2, (width, height))

frmImg3 = pygame.image.load('images/frame3death.gif')
frmImg3 = pygame.transform.scale(frmImg3, (width, height))

frmImg4 = pygame.image.load('images/frame4death.gif')
frmImg4 = pygame.transform.scale(frmImg4, (width, height))

frmImg5 = pygame.image.load('images/frame5death.gif')
frmImg5 = pygame.transform.scale(frmImg5, (width, height))

frmImg6 = pygame.image.load('images/frame6death.gif')
frmImg6 = pygame.transform.scale(frmImg6, (width, height))

frmImg7 = pygame.image.load('images/frame7death.gif')
frmImg7 = pygame.transform.scale(frmImg7, (width, height))

frmImg8 = pygame.image.load('images/frame8death.gif')
frmImg8 = pygame.transform.scale(frmImg8, (width, height))

frmImg9 = pygame.image.load('images/frame9death.gif')
frmImg9 = pygame.transform.scale(frmImg9, (width, height))

nmywin.append(frmImg1)
nmywin.append(frmImg2)
nmywin.append(frmImg3)
nmywin.append(frmImg4)
nmywin.append(frmImg5)
nmywin.append(frmImg6)
nmywin.append(frmImg7)
nmywin.append(frmImg8)
nmywin.append(frmImg9)
o = 1


#time variables
Time = 0
am_pm = 0
AM_PM = "12 AM"
variableusedtofixautogoingtowindowbug = 0
power = 0

#main loop
main = True
while main:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      main = False
      pygame.quit()
      sys.exit()
  mouseX, mouseY = pygame.mouse.get_pos()
  if screenControl == 1:
    power += 1
  if screenControl == 8:
    power += 0.20
  if screenControl == 7:
    power += 0.20
  if screenControl == 3 or screenControl == 4 or screenControl == 5 or screenControl == 6:
    power += 3
  if screenControl == 9:
    power += 2
  if power < 100000:
    clr = (0, 255, 0)
  elif power > 100000 and power < 160000:
    clr = (255, 200, 0)
  elif power > 160000 and power < 220000:
    clr = (255, 0, 0)
  if power >= 220000:
    screenControl = 11
  #print(power)
  
  if screenControl != 0 and screenControl != 2:
    variableusedtofixautogoingtowindowbug += 1
    Time += 1
    if Time == 25000:
      am_pm += 1
      Time = 0
    if am_pm == 1:
      AM_PM = "1 AM"
    elif am_pm == 2:
      AM_PM = "2 AM"
    elif am_pm == 3:
      AM_PM = "3 AM"
    elif am_pm == 4:
      AM_PM = "4 AM"
    elif am_pm == 5:
      AM_PM = "5 AM"
    elif am_pm == 6:
      AM_PM = "6 AM"
    nmymve += 1
    if nmymve >= 4000:
      nmySpot += 1
      nmymve = 0
    if nmySpot == 7 and nmymve == 1:
      path = random.choice(nmypath)
      #path = nmypath[1]
      print(nmymve)
      #print(path)
      o = 1
      if path == nmypath[0]:
        nmyDoor = 0
      elif path == nmypath[1]:
        nmyWndw = 0
    elif nmySpot < 7:
      path = 3
    
    
      

        
    

     
 
  #title screen
  if screenControl == 0:
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 40)
    text = font.render("A Night at EDPs", True, WHITE)
    screen.blit(text, (50, 100))
    font2 = pygame.font.Font('freesansbold.ttf', 40)
    text2 = font2.render('Start Game', True, c, v)
    textRect = text2.get_rect()
    textRect.center = (160, 220)    
    screen.blit(text2, textRect)
#if mouse is in play button, button colours will invert
    if mouseX >= textRect.left and mouseX <= textRect.right and mouseY >= textRect.top and mouseY <= textRect.bottom:
      c = (0, 0, 0)
      v = (255, 255, 255)
      screen.blit(text2, textRect)
    else:
      c = (255, 255, 255)
      v = (0, 0, 0)
#if mouse is clicked in play button, screen is changed
    if mouseX >= textRect.left and mouseX <= textRect.right and mouseY >= textRect.top and mouseY <= textRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
      screen.blit(text2, textRect)
      textRect.center = (900, 900)
      nmymve = 0
      nmySpot = 0
    #if mouse clicks this button, it brings up an instuctions/how to play screen      
    font3 = pygame.font.Font('freesansbold.ttf', 40)
    text3 = font3.render('Instructions', True, c2, v2)
    textRect1 = text3.get_rect()
    textRect1.center = (170, 270)    
    screen.blit(text3, textRect1)
    if mouseX >= textRect1.left and mouseX <= textRect1.right and mouseY >= textRect1.top and mouseY <= textRect1.bottom:
      c2 = (0, 0, 0)
      v2 = (255, 255, 255)
      screen.blit(text3, textRect1)
    else:
      c2 = (255, 255, 255)
      v2 = (0, 0, 0)
    if mouseX >= textRect1.left and mouseX <= textRect1.right and mouseY >= textRect1.top and mouseY <= textRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 2
      pygame.display.update()    
      screen.blit(text3, textRect1)
      textRect1.center = (900, 900)
  ######################
  if screenControl == 2:
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 40)
    instruction1 = font.render("-Survive until 6 am", True, WHITE)
    screen.blit(instruction1, (10, 100)) 
    instruction2a = font.render("-Click the door, or window", True, WHITE)
    screen.blit(instruction2a, (10, 140)) 
    instruction2b = font.render("to move there", True, WHITE)
    screen.blit(instruction2b, (10, 180)) 
    instruction3 = font.render("-Click the screen to open cams", True, WHITE)
    screen.blit(instruction3, (10, 220))
    instruction4 = font.render("-Click c while at door/window to close", True, WHITE)
    screen.blit(instruction4, (10, 260))
    instruction5 = font.render("-Click space for light at door/window", True, WHITE)
    screen.blit(instruction5, (10, 300))
    instruction6 = font.render("-Close door/window if EDP is close", True, WHITE)
    screen.blit(instruction6, (10, 340))
    instruction7 = font.render("-Use light if EDP in far door/window", True, WHITE)
    screen.blit(instruction7, (10, 380))
    ####################################
    font3 = pygame.font.Font('freesansbold.ttf', 40)
    text3 = font3.render('Back to menu', True, c2, v2)
    textRect1 = text3.get_rect()
    textRect1.center = (400, 500)    
    screen.blit(text3, textRect1)
    if mouseX >= textRect1.left and mouseX <= textRect1.right and mouseY >= textRect1.top and mouseY <= textRect1.bottom:
      c2 = (0, 0, 0)
      v2 = (255, 255, 255)
      screen.blit(text3, textRect1)
    else:
      c2 = (255, 255, 255)
      v2 = (0, 0, 0)
    if mouseX >= textRect1.left and mouseX <= textRect1.right and mouseY >= textRect1.top and mouseY <= textRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 0
      pygame.display.update()    
      screen.blit(text3, textRect1)
      textRect1.center = (900, 900)

  ####################################
    #actual game screen
  if screenControl == 1:
    screen.fill(BLACK)
    screen.blit(bkgrndImg, bkgrnd)
    screen.blit(deskImg, desk)
    screen.blit(computerImg, computer)
    screen.blit(compscrnImg, compscrn)
    if mouseX >= compscrn.left and mouseX <= compscrn.right and mouseY >= compscrn.top and mouseY <= compscrn.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 3
    door = pygame.draw.rect(screen, BLACK,(452, 100, 135, 350), 0)
    if mouseX >= door.left and mouseX <= door.right and mouseY >= door.top and mouseY <= door.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 7
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
    if variableusedtofixautogoingtowindowbug >= 100 and mouseX >= 50 and mouseX <= 250 and mouseY >= 90 and mouseY <= 290 and pygame.mouse.get_pressed()[0]:
      screenControl = 8
    fnt = pygame.font.Font('freesansbold.ttf', 20)
    powr = fnt.render('click p to check power screen', True, c2, v2)
    screen.blit(powr, (0, 0))
    key_npt = pygame.key.get_pressed()
    if key_npt[pygame.K_p]:
      screenControl = 9
  ###################################
  if screenControl == 3:
    screen.fill(BLACK)
    screen.blit(staticImg, static)
    audio('sounds/opencams.mp3', 0.7)
    









    
    
    #camera 1 button
    font = pygame.font.Font('freesansbold.ttf', 40)
    cam1 = font.render('cam1', True, c2, v2)
    camRect1 = cam1.get_rect()
    camRect1.center = (450, 400)    
    screen.blit(cam1, camRect1)    
    if mouseX >= camRect1.left and mouseX <= camRect1.right and mouseY >= camRect1.top and mouseY <= camRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 4
      pygame.display.update()    
      screen.blit(cam1, camRect1)
      camRect1.center = (900, 900)
    #camera 2 button
    cam2 = font.render('cam2', True, c2, v2)
    camRect2 = cam2.get_rect()
    camRect2.center = (560, 400)    
    screen.blit(cam2, camRect2)    
    if mouseX >= camRect2.left and mouseX <= camRect2.right and mouseY >= camRect2.top and mouseY <= camRect2.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 5
      pygame.display.update()    
      screen.blit(cam2, camRect2)
      camRect2.center = (900, 900)
     #camera 3 button 
    cam3 = font.render('cam3', True, c2, v2)
    camRect3 = cam3.get_rect()
    camRect3.center = (670, 400)    
    screen.blit(cam3, camRect3)    
    if mouseX >= camRect3.left and mouseX <= camRect3.right and mouseY >= camRect3.top and mouseY <= camRect3.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 6
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    #leave cameras
    close = font.render('Close Cameras', True, c2, v2)
    closeRect = close.get_rect()
    closeRect.center = (400, 500)    
    screen.blit(close, closeRect)    
    if mouseX >= closeRect.left and mouseX <= closeRect.right and mouseY >= closeRect.top and mouseY <= closeRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
#######################################
  if screenControl == 4:
    screen.fill(BLACK)
    screen.blit(cam1Img, camera1)
    if nmySpot == 1:
      nmysizeX = 30
      nmysizeY = 75
      nmyX = 300
      nmyY = 300
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    elif nmySpot == 2:
      nmysizeX = 90
      nmysizeY = 225
      nmyX = 600
      nmyY = 450
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #camera 1 button
    font = pygame.font.Font('freesansbold.ttf', 40)
    cam1 = font.render('cam1', True, c2, v2)
    camRect1 = cam1.get_rect()
    camRect1.center = (450, 400)    
    screen.blit(cam1, camRect1)    
    if mouseX >= camRect1.left and mouseX <= camRect1.right and mouseY >= camRect1.top and mouseY <= camRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 4
      pygame.display.update()    
      screen.blit(cam1, camRect1)
      camRect1.center = (900, 900)
    #camera 2 button
    cam2 = font.render('cam2', True, c2, v2)
    camRect2 = cam2.get_rect()
    camRect2.center = (560, 400)    
    screen.blit(cam2, camRect2)    
    if mouseX >= camRect2.left and mouseX <= camRect2.right and mouseY >= camRect2.top and mouseY <= camRect2.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 5
      pygame.display.update()    
      screen.blit(cam2, camRect2)
      camRect2.center = (900, 900)
     #camera 3 button 
    cam3 = font.render('cam3', True, c2, v2)
    camRect3 = cam3.get_rect()
    camRect3.center = (670, 400)    
    screen.blit(cam3, camRect3)    
    if mouseX >= camRect3.left and mouseX <= camRect3.right and mouseY >= camRect3.top and mouseY <= camRect3.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 6
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    #leave cameras
    close = font.render('Close Cameras', True, c2, v2)
    closeRect = close.get_rect()
    closeRect.center = (400, 500)    
    screen.blit(close, closeRect)    
    if mouseX >= closeRect.left and mouseX <= closeRect.right and mouseY >= closeRect.top and mouseY <= closeRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
####################################
  if screenControl == 5:
    screen.fill(BLACK)
    screen.blit(cam2Img, camera2)
    if nmySpot == 3:
      nmysizeX = 120
      nmysizeY = 300
      nmyX = 250
      nmyY = 90
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    elif nmySpot == 4:
      nmysizeX = 300
      nmysizeY = 900
      nmyX = 500
      nmyY = 350
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #camera 1 button
    font = pygame.font.Font('freesansbold.ttf', 40)
    cam1 = font.render('cam1', True, c2, v2)
    camRect1 = cam1.get_rect()
    camRect1.center = (450, 400)    
    screen.blit(cam1, camRect1)    
    if mouseX >= camRect1.left and mouseX <= camRect1.right and mouseY >= camRect1.top and mouseY <= camRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 4
      pygame.display.update()    
      screen.blit(cam1, camRect1)
      camRect1.center = (900, 900)
    #camera 2 button
    cam2 = font.render('cam2', True, c2, v2)
    camRect2 = cam2.get_rect()
    camRect2.center = (560, 400)    
    screen.blit(cam2, camRect2)    
    if mouseX >= camRect2.left and mouseX <= camRect2.right and mouseY >= camRect2.top and mouseY <= camRect2.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 5
      pygame.display.update()    
      screen.blit(cam2, camRect2)
      camRect2.center = (900, 900)
     #camera 3 button 
    cam3 = font.render('cam3', True, c2, v2)
    camRect3 = cam3.get_rect()
    camRect3.center = (670, 400)    
    screen.blit(cam3, camRect3)    
    if mouseX >= camRect3.left and mouseX <= camRect3.right and mouseY >= camRect3.top and mouseY <= camRect3.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 6
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    #leave cameras
    close = font.render('Close Cameras', True, c2, v2)
    closeRect = close.get_rect()
    closeRect.center = (400, 500)    
    screen.blit(close, closeRect)    
    if mouseX >= closeRect.left and mouseX <= closeRect.right and mouseY >= closeRect.top and mouseY <= closeRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
  #####################################
  if screenControl == 6:
    screen.fill(BLACK)
    screen.blit(cam3Img, camera3)
    if nmySpot == 5:
      nmysizeX = 240
      nmysizeY = 600
      nmyX = 600
      nmyY = 100
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    elif nmySpot == 6:
      nmysizeX = 120
      nmysizeY = 300
      nmyX = 400
      nmyY = 200
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #camera 1 button
    font = pygame.font.Font('freesansbold.ttf', 40)
    cam1 = font.render('cam1', True, c2, v2)
    camRect1 = cam1.get_rect()
    camRect1.center = (450, 400)    
    screen.blit(cam1, camRect1)    
    if mouseX >= camRect1.left and mouseX <= camRect1.right and mouseY >= camRect1.top and mouseY <= camRect1.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 4
      pygame.display.update()    
      screen.blit(cam1, camRect1)
      camRect1.center = (900, 900)
    #camera 2 button
    cam2 = font.render('cam2', True, c2, v2)
    camRect2 = cam2.get_rect()
    camRect2.center = (560, 400)    
    screen.blit(cam2, camRect2)    
    if mouseX >= camRect2.left and mouseX <= camRect2.right and mouseY >= camRect2.top and mouseY <= camRect2.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 5
      pygame.display.update()    
      screen.blit(cam2, camRect2)
      camRect2.center = (900, 900)
     #camera 3 button 
    cam3 = font.render('cam3', True, c2, v2)
    camRect3 = cam3.get_rect()
    camRect3.center = (670, 400)    
    screen.blit(cam3, camRect3)    
    if mouseX >= camRect3.left and mouseX <= camRect3.right and mouseY >= camRect3.top and mouseY <= camRect3.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 6
      pygame.display.update()    
      screen.blit(cam3, camRect3)
      camRect3.center = (900, 900)
    #leave cameras
    close = font.render('Close Cameras', True, c2, v2)
    closeRect = close.get_rect()
    closeRect.center = (400, 500)    
    screen.blit(close, closeRect)    
    if mouseX >= closeRect.left and mouseX <= closeRect.right and mouseY >= closeRect.top and mouseY <= closeRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
      screen.blit(close, closeRect)
      closeRect.center = (900, 900)
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
############################
  #hall view
  if screenControl == 7:
    screen.fill(BLACK)
    screen.blit(halldrkImg, halldrk)
    key_npt = pygame.key.get_pressed()
    if key_npt[pygame.K_SPACE]:
        screen.blit(hallflshImg, hallflsh)
    leave = font.render('Leave Door', True, c2, v2)
    leaveRect = leave.get_rect()
    leaveRect.center = (400, 500)    
    screen.blit(leave, leaveRect)    
    if mouseX >= leaveRect.left and mouseX <= leaveRect.right and mouseY >= leaveRect.top and mouseY <= leaveRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1   
      screen.blit(leave, leaveRect)
      leaveRect.center = (900, 900)
      pygame.display.update() 
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
      #if flash light is on and enemies location is in the 7th or 8th spot, then the enemy will appear in the hallway
      #show image at end of hall
    if key_npt[pygame.K_SPACE] and path == nmypath[0] and nmySpot == 7:
      nmysizeX = 90
      nmysizeY = 200
      nmyX = 300
      nmyY = 140
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #show image at front of hall
    elif key_npt[pygame.K_SPACE] and path == nmypath[0] and nmySpot == 8:
      nmysizeX = 270
      nmysizeY = 600
      nmyX = 300
      nmyY = 160
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #if held long enough enemy leaves
    if key_npt[pygame.K_SPACE] and path == nmypath[0] and nmySpot == 7:
      nmylve += 1
      if nmylve >= 1000:
        nmymve2 = 0
        nmySpot = 0
        nmylve = 0
        nmyDoor = 0
        
    if nmylve < 1000 and path == nmypath[0] and nmySpot == 7 and not key_npt[pygame.K_SPACE]:
      nmylve = 0
    if key_npt[pygame.K_c]:
      screen.fill(BLACK)
      screen.blit(doorImg, (0, 0))
      #if door is closed for long enough enemy leaves
    if nmySpot == 8 and path == nmypath[0] and key_npt[pygame.K_c]:
      nmylve += 1
      if nmylve >= 1000:
        nmySpot = 0
        nmylve = 0
        nmyDoor = 0
        nmymve2 = 0
    if nmylve < 1000 and path == nmypath[0] and nmySpot == 8 and not key_npt[pygame.K_c]:
      nmylve = 0
        
    if key_npt[pygame.K_SPACE] and path == nmypath[0] and nmySpot == 8:
      flashlightTime += 1
      print(flashlightTime) 
      if flashlightTime >= 20:
        screen.fill(BLACK)
          #time.sleep(1)
        screenControl = 11
    else:
      flashlightTime = 0
##################################
  #code for window
  if screenControl == 8:
    screen.fill(BLACK)
    key_npt = pygame.key.get_pressed()
    screen.blit(wndwImg, (0, 0))
    if key_npt[pygame.K_SPACE]:
      screen.blit(wndwflshImg, (0, 0))
    wndwlve = font.render('Leave Window', True, c2, v2)
    wndwRect = wndwlve.get_rect()
    wndwRect.center = (400, 500)    
    screen.blit(wndwlve, wndwRect) 
    if mouseX >= wndwRect.left and mouseX <= wndwRect.right and mouseY >= wndwRect.top and mouseY <= wndwRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
      pygame.display.update()    
    font = pygame.font.Font('freesansbold.ttf', 40)
    AM = font.render(AM_PM, True, c2, v2)
    AMRect = AM.get_rect()
    AMRect.center = (700, 20)    
    screen.blit(AM, AMRect) 
  #show enemy at far part of backyard
    if key_npt[pygame.K_SPACE] and path == nmypath[1] and nmySpot == 7:
      nmysizeX = 45
      nmysizeY = 100
      nmyX = 500
      nmyY = 190
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
    #shows enemy closer to the window
    elif key_npt[pygame.K_SPACE] and path == nmypath[1] and nmySpot == 8:
      nmysizeX = 150
      nmysizeY = 320
      nmyX = 400
      nmyY = 140
      nmyImg = pygame.transform.scale(nmyImg, (nmysizeX, nmysizeY))
      nmy = pygame.Rect((nmyX, nmyY), (nmysizeX, nmysizeY))
      screen.blit(nmyImg, nmy)
  #if light is shined and enemy at end of backyard, after a time period enemy leaves
    if key_npt[pygame.K_SPACE] and path == nmypath[1] and nmySpot == 7:
      nmylve += 1
      if nmylve >= 1000:
        nmymve2 = 0
        nmySpot = 0
        nmylve = 0
        nmyDoor = 0      
    
    #if c is clicked windows close
    if key_npt[pygame.K_c]:
      screen.blit(clsdwndwImg, (0, 0))
    #if window is closed and enemy is at front of backyard, after a time period enemy leaves
    if nmySpot == 8 and path == nmypath[1] and key_npt[pygame.K_c]:
      nmylve += 1
      if nmylve >= 200:
        nmySpot = 0
        nmylve = 0
        nmyDoor = 0
        nmymve2 = 0
    if nmylve < 200 and path == nmypath[1] and nmySpot == 8 and not key_npt[pygame.K_c]:
      nmylve = 0
    #if flashlight on enemy for too long while
    if key_npt[pygame.K_SPACE] and path == nmypath[1] and nmySpot == 8:
      flashlightTime += 1
      print(flashlightTime) 
      if flashlightTime >= 20:
        screen.fill(BLACK)
        screenControl = 11
    else:
      flashlightTime = 0
  ###############################
  if screenControl == 9:
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 40)
    pwr = font.render(f'{int(power)}', True, clr, BLACK)
    screen.blit(pwr, (350, 300))
    
    wndwlve = font.render('Leave screen', True, c2, v2)
    wndwRect = wndwlve.get_rect()
    wndwRect.center = (400, 500)    
    screen.blit(wndwlve, wndwRect) 
    if mouseX >= wndwRect.left and mouseX <= wndwRect.right and mouseY >= wndwRect.top and mouseY <= wndwRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 1
##################################
  if screenControl == 11:
    nmywntme += 1
    if nmywntme == 5:
      screen.blit(nmywin[0], frmRct)
    elif nmywntme == 500:
      screen.blit(nmywin[1], frmRct)
    elif nmywntme == 750:
      screen.blit(nmywin[2], frmRct)
    elif nmywntme == 1000:
      screen.blit(nmywin[3], frmRct)
    elif nmywntme == 1250:
      screen.blit(nmywin[4], frmRct)
    elif nmywntme == 1500:
      screen.blit(nmywin[5], frmRct)
    elif nmywntme == 1750:
      screen.blit(nmywin[6], frmRct)
    elif nmywntme == 2000:
      screen.blit(nmywin[7], frmRct)
    elif nmywntme == 2250:
      screen.blit(nmywin[8], frmRct)
    if nmywntme == 2250:
      screenControl = 12
      nmywntme = 0
##################################  
  if screenControl == 12:
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 80)
    font2 = pygame.font.Font('freesansbold.ttf', 40)
    youLost = font.render("You Died!", True, WHITE, BLACK)
    screen.blit(youLost, (200, 100))
    goToMenu = font2.render('Return to Menu', True, c, v)
    rtrnRect = goToMenu.get_rect()
    rtrnRect.center = (400, 500)    
    screen.blit(goToMenu, rtrnRect)
#if mouse is in play button, button colours will invert
    if mouseX >= rtrnRect.left and mouseX <= rtrnRect.right and mouseY >= rtrnRect.top and mouseY <= rtrnRect.bottom:
      c = (0, 0, 0)
      v = (255, 255, 255)
      screen.blit(text2, textRect)
    else:
      c = (255, 255, 255)
      v = (0, 0, 0)
    if mouseX >= rtrnRect.left and mouseX <= rtrnRect.right and mouseY >= rtrnRect.top and mouseY <= rtrnRect.bottom and pygame.mouse.get_pressed()[0]:
      screenControl = 0

    
  if AM_PM == "6 AM":
    screenControl = 10
  if screenControl == 10:
    screen.fill(BLACK)
    font = pygame.font.Font('freesansbold.ttf', 40)
    win1 = font.render('6 AM', True, c2, v2)
    win1Rect = win1.get_rect()
    win1Rect.center = (400, 300)    
    screen.blit(win1, win1Rect)  
    
    win2 = font.render('The Police arrived!', True, c2, v2)
    win2Rect = win2.get_rect()
    win2Rect.center = (400, 400)    
    screen.blit(win2, win2Rect)  
    power = 0
    nmymve = 0
    nmySpot = 0
    Time = 0
    am_pm = 0
    AM_PM = "12 AM"
    variableusedtofixautogoingtowindowbug = 0
    power = 0
    
    
      
    
   
    pygame.display.update()

  
  pygame.display.update()