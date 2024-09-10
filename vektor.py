from math import sqrt
class Vector():
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    
    def get(self):
        return(self.__x,self.__y)
    

    @property
    def x(self):
        return(self.__x)
    
    @property
    def y(self):
        return(self.__y)
    
    @x.setter
    def x(self,x):
        self.__x = x
    
    @y.setter
    def y(self,y):
        self.__y = y
    
    def __str__(self):
        return("{self.__x} og {self.__y}")
    
    def __add__(self,Victor):
        return(Vector(self.__x + Victor.x, self.__y + Victor.y))
    
    def __sub__(self,Victor):
        return(Vector(self.__x - Victor.x, self.__y - Victor.y))
    
    def __mul__(self,multiplicator):
        return(Vector(self.__x * multiplicator, self.__y * multiplicator))
    
    def getLength(self):
        return(sqrt(self.__x**2 + self.__y**2))
    
    def scallar(self,Victor):
        return(self.__x * Victor.x + self.__y * Victor.y)
#Vector1 = Vector(2,2)
#Vector2 = Vector(4,2)

#print(Vector1.get())
#print(Vector2.get())

#Vector3 = 
# Vector1 + Vector2
#print(Vector3.get())

#Vector4 = Vector1 - Vector2
#print(Vector4.get())

#Vector5 = Vector2 * 3
#print(Vector5.get())

#print(Vector4.getLength())

#print(Vector1.scallar(Vector2))

