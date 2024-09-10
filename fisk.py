import pygame
from vektor import *



class Fisk():
    def __init__(self,pos,vel,img,screen,d):
        self.__pos = pos
        self.__vel = vel
        self.__img = img
        self.__vec = vel
        self.__startVelx= self.__vel.x*0.2
        self.__startVely= self.__vel.y*0.2
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.__d = d

    def borderControl(self):
        if self.__pos.x > 800-50 or self.__pos.x<0:
            self.__vec.x = self.__vec.x * -1
        
        if self.__pos.y>600-50 or self.__pos.y<0:
            self.__vec.y = self.__vec.y * -1

        return(self.__vec)
    
    def bordercontrol2(self):
        self.__velocity = self.__vel
        if(self.__pos.x<self.__d):
            self.__velocity.x +=(self.__startVelx*1-self.__startVelx*self.__pos.x/self.__d)

        if(self.__pos.y<self.__d):
            self.__velocity.y +=(self.__startVely*1 - self.__startVely * (self.__pos.y/self.__d))

        if(self.__pos.x+50>self.w-self.__d):
            self.__velocity.x +=(-self.__startVelx*1 + self.__startVelx*(self.w-self.__pos.x-50)/self.__d )

        if(self.__pos.y+50>self.h-self.__d):
            self.__velocity.y += (-self.__startVely * 1 + self.__startVely * (self.h-self.__pos.y-50)/self.__d)
        
        return(self.__velocity)

    def update(self):
        self.__pos = self.__pos + self.__vel
        self.__vel = self.bordercontrol2()
        #self.__vel.x = self.__vec.x
        #
        # self.__vel.y = self.__vel.y

    def draw(self):
        self.screen.blit(self.__img,(self.__pos.x,self.__pos.y))  
    
