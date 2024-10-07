import pygame
from vektor import *
from fisk import *
from stimme import *
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import pygame_widgets
from sliders import *



#husk at flippe over på skærmen

def main():
    pygame.init()
    


    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    fishes = Stimme(15,screen,'fish.png')
    fishes.update()

    Slider1 = Slider_w_labels(screen,1,0,99,"Sep")
    Slider2 = Slider_w_labels(screen,2,0,10,"Ali")
    Slider3 = Slider_w_labels(screen,3,0,1000,"Coh")

    # slider = Slider(screen, 90, 40, 200, 10, min=0, max=99, step=1)
    # outputValue = TextBox(screen, 60, 30, 25, 25, fontSize=15)
    # outputText = TextBox(screen, 10,30, 50,25, fontSize=15)

    # outputValue.disable()
    # outputText.disable()
    # outputText.setText("min slider")


    running = True
    while running:   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  
        screen.fill((0, 128, 255))
        
        fishes.draw(Slider1.slider.getValue(),Slider2.slider.getValue()/10,Slider3.slider.getValue()/10000)

        # outputValue.setText(slider.getValue())   
        Slider1.update()
        Slider2.update()
        Slider3.update()
        pygame_widgets.update(pygame.event.get())


        pygame.display.flip()
        clock.tick(60) 
main() 
pygame.quit()

