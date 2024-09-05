from fisk import *
from vektor import *

class Stimme():
    def __init__(self,antal):
        self.__stimme = []
        self.__antal = antal
    
    def update(self):
       n = 0
       while n< self.__antal :
        position = Vector(n*10,n*10)
        velocity = Vector(2+n,2+n)
        i = n
        i = Fisk(position,velocity,'fish.png') 
        position = Vector(n*10,n*10)
        velocity = Vector(n*2+1,n*2+1)
        self.__stimme.append(i)
        n+=1
    
    def draw(self,screen):
        for x in self.__stimme:
            x.update()
            x.draw(screen)