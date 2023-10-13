# jdaniels
# small football game made for fun

import pygame 
import time 


pygame.display.init()
screen = pygame.display.set_mode((800,600))
done = False
ballx = 400
bally = 300

while done == False:
    screen.fill((0,0,0))
    pygame.event.pump()
    pressedList = pygame.key.get_pressed()

    if pressedList[pygame.K_ESCAPE]:
        done=True
    if pressedList[pygame.K_w] or pressedList[pygame.K_UP]:
        bally -= .1
    if pressedList[pygame.K_s] or pressedList[pygame.K_DOWN]:
        bally += .1
    if pressedList[pygame.K_a] or pressedList[pygame.K_LEFT]:
        ballx -= .1
    if pressedList[pygame.K_d] or pressedList[pygame.K_RIGHT]:
        ballx += .1
    #block
    if ballx > 800 :
        ballx=800
    if ballx < 0:
        ballx=0
    if bally > 600:
        bally=600
    if bally < 0:
        bally=0
    #booster arrows
    if pressedList[pygame.K_UP] and pressedList[pygame.K_RSHIFT]:
        bally -= 1
    if pressedList[pygame.K_DOWN] and pressedList[pygame.K_RSHIFT]:
        bally += 1
    if pressedList[pygame.K_LEFT]and pressedList[pygame.K_RSHIFT]:
        ballx -= 1
    if pressedList[pygame.K_RIGHT] and pressedList[pygame.K_RSHIFT]:
        ballx += 1
    #booster wasd
    if pressedList[pygame.K_w] and pressedList[pygame.K_RSHIFT]:
        bally -= 1
    if pressedList[pygame.K_s] and pressedList[pygame.K_RSHIFT]:
        bally += 1
    if pressedList[pygame.K_a]and pressedList[pygame.K_RSHIFT]:
        ballx -= 1
    if pressedList[pygame.K_d] and pressedList[pygame.K_RSHIFT]:
        ballx += 1



    pygame.draw.circle(screen, (0,255,0), ((int(ballx)), (int(bally))), 50,0)
    pygame.display.flip()

pygame.display.quit
