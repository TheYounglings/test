import pygame
from vektor import *



class Fisk():
    def __init__(self,pos,vel,img,screen,d):
        self.__pos = pos
        self.__vel = vel
        self.__img = img
        self.__vec = vel
        self.__startVelxR = abs(self.__vel.x)
        self.__startVelyR = abs(self.__vel.y)
        self.__startVelx= abs(self.__vel.x*0.2)
        self.__startVely= abs(self.__vel.y*0.2)
        self.screen = screen
        self.w, self.h = pygame.display.get_surface().get_size()
        self.__d = d
    
    @property
    def pos(self):
        return(self.__pos)

    def borderControl(self):
        if self.__pos.x > 800-50 or self.__pos.x<0:
            self.__vec.x = self.__vec.x * -1
        
        if self.__pos.y>600-50 or self.__pos.y<0:
            self.__vec.y = self.__vec.y * -1

        return(self.__vec)
    
    def borderControl2(self):
        self.__velocity = self.__vel
        if(self.__pos.x<self.__d):
            self.__velocity.x +=(self.__startVelx*1-self.__startVelx*self.__pos.x/self.__d)

        if(self.__pos.y<self.__d):
            self.__velocity.y +=(self.__startVely*1 - self.__startVely * (self.__pos.y/self.__d))

        if(self.__pos.x+50>self.w-self.__d):
            self.__velocity.x +=(-self.__startVelx*1 + self.__startVelx*(self.w-self.__pos.x-50)/self.__d )

        if(self.__pos.y+50>self.h-self.__d):
            self.__velocity.y += (-self.__startVely * 1 + self.__startVely * (self.h-self.__pos.y-50)/self.__d)
        
        if self.__velocity.x > self.__startVelxR:
            self.__velocity.x = self.__startVelxR
        if self.__velocity.x < -self.__startVelxR:
            self.__velocity.x = -self.__startVelxR
        if self.__velocity.y > self.__startVelyR:
            self.__velocity.y = self.__startVelyR
        if self.__velocity.y < -self.__startVelyR:
            self.__velocity.y = -self.__startVelyR
        return(self.__velocity)
    
    def borderControl3(self):
        if self.__pos.x < 0-51:
            self.__pos.x = self.w
        
        if self.__pos.y < 0-51:
            self.__pos.y = self.h
        
        if self.__pos.x > self.w:
            self.__pos.x = -50

        
        if self.__pos.y > self.h:
            self.__pos.y = -50
    
    def seperation(self,flockFishes,tooClose=150, seperationFactor=10):
        seperationVector = Vector(0,0)
        for fish in flockFishes:
            if fish != self:
                distance = self.__pos.distance(fish.pos)
                if distance < tooClose:
                    seperationVector += (self.__pos - fish.pos).normalise()/distance
        return(seperationVector*seperationFactor)



    def update(self,flockFishes):
        self.__pos = self.__pos + self.__vel

        #self.borderControl3()

        self.__vel = self.borderControl2()

        self.__vel += self.seperation(flockFishes)
        # self.__vel.x = self.__vec.x
        
        # self.__vel.y = self.__vel.y


    def draw(self):
        self.screen.blit(self.__img,(self.__pos.x,self.__pos.y))  
    
