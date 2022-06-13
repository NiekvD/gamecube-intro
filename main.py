import pygame
from pygame.locals import *
 
pygame.init()
clock = pygame.time.Clock()
size = 500, 500
screen = pygame.display.set_mode(size,0,32)
pygame.display.set_caption('GAME')
x, y = 338/2, 338/2
 
sprite=pygame.image.load('gamecube-up.png')
loop = True
while loop:
    screen.blit(sprite,(x,y))
 
    for event in pygame.event.get():
        if event.type==QUIT:
            loop = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 85
        y += 45
    if keys[pygame.K_RIGHT]:
        x += 85
        y -= 45
    if keys[pygame.K_UP]:
        x -= 85
        y -= 45
    if keys[pygame.K_DOWN]:
        x += 85
        y += 45
    if keys[pygame.K_ESCAPE]:
        screen.fill((0,0,0))
    pygame.display.flip()
    clock.tick(12)

 
pygame.quit()