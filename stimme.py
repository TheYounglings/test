from fisk import *
from vektor import *
import random
import pygame

class Stimme():
    def __init__(self,antal,screen, img):
        self.__stimme = []
        self.__antal = antal
        self.screen = screen
        self.__img = pygame.image.load(img)
        self.__img = pygame.transform.scale(self.__img, (50,50))
    
    def update(self):
       n = 0
       while n< self.__antal :
        velocity = Vector(random.uniform(1,4),random.uniform(-1,-4))
        i = n
        position = Vector(random.uniform(250,500),random.uniform(250,500))
        i = Fisk(position,velocity,self.__img,self.screen,random.uniform(25,250)) 
        self.__stimme.append(i)
        n+=1
    
    def draw(self,seperationFactor,allignmentFactor,cohessionFactor):
        for x in self.__stimme:
            x.update(self.__stimme,seperationFactor,allignmentFactor,cohessionFactor)
            x.draw()
            if x == 1:
               print(x.x)