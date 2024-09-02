import pygame
from vektor import *
from fisk import *




#husk at flippe over på skærmen

def main():
    pygame.init()
    stimme = []

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    n = 0
    while n<10:
       position = Vector(n*10,n*10)
       velocity = Vector(n*2+1,n*2+1)
       i = n
       i = Fisk(position,velocity,'fish.png') 
       position = Vector(n*10,n*10)
       velocity = Vector(n*2+1,n*2+1)
 
       stimme.append(i)
       n+=1
    #fisk = Fisk(position,velocity,'fish.png')


    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        for x in stimme:
            x.update()
            x.draw(screen)
            


        pygame.display.flip()
        clock.tick(60) 
main() 
pygame.quit()

