import pygame
from vektor import *


class Fisk():
    def __init__(self,pos,vel,img):
        self.__pos = pos
        self.__vel = vel
        self.__img = img
        self.__vec = vel
        self.__img = pygame.image.load(self.__img)
        self.__img = pygame.transform.scale(self.__img, (50,50))

    def borderControl(self):
        if self.__pos.x > 800-50 or self.__pos.x<0:
            self.__vec.x = self.__vec.x * -1
        
        if self.__pos.y>600-50 or self.__pos.y<0:
            self.__vec.y = self.__vec.y * -1

        return(self.__vec)
    
    def update(self):
        self.__pos = self.__pos + self.__vel
        #self.borderControl()
        self.__vel.x = self.__vec.x
        self.__vel.y = self.__vel.y

    def draw(self,screen):
        screen.blit(self.__img,(self.__pos.x,self.__pos.y))  
    
