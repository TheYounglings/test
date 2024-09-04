import pygame
from vektor import *
from fisk import *
from stimme import *



#husk at flippe over på skærmen

def main():
    pygame.init()


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    fishes = Stimme(40)
    fishes.update()



    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        
        fishes.draw(screen)

            


        pygame.display.flip()
        clock.tick(60) 
main() 
pygame.quit()

