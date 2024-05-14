import pygame
import random
import sys
pygame.init()
size=width,heigt=(400,300)

sc=pygame.display.set_mode(size)
def draw():
    for i in range(20000):
        sc.fill(pygame.Color("black"),(random.random()*width,random.random()*heigt,1,1))

while 1:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()
    sc.fill((0,255,0))
    draw()
    pygame.display.update()
