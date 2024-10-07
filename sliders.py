import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
import pygame_widgets


class Slider_w_labels:
    def __init__(self,screen,i,minV,maxV,text):
        self.slider = Slider(screen,90,40+i*40,200,10, min=minV,max = maxV,step = 1)
        self.outputValue = TextBox(screen,60,30+i*40,25,25,fontSize = 15)
        self.outputText = TextBox(screen, 10,30+i*40, 50,25, fontSize=15)
        self.outputValue.disable()
        self.outputText.disable()
        self.outputText.setText(text)
        
    def update(self):
        self.outputValue.setText(self.slider.getValue())