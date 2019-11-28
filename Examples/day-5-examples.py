# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 09:54:37 2019

@author: Ahmad ALaarg
"""
"""

class Person:
    def say_hello(self):
        print('Hello')


p = Person()
p.say_hello()


# -----------------------------
class Vehicle:

    def __init__(self, name, color):
        self.__name = name  # __name is private to Vehicle class
        self.__color = color

    def getColor(self):  # getColor() function is accessible to class Car
        return self.__color

    def setColor(self, color):  # setColor is accessible outside the class
        self.__color = color

    def getName(self):  # getName() is accessible outside the class
        return self.__name


class Car(Vehicle):

    def __init__(self, name, color, model):
        # call parent constructor to set name and color  
        super().__init__(name, color)
        self.__model = model

    def getDescription(self):
        return self.getName() + self.__model + " in " + self.getColor() + " color"


# in method getDescrition we are able to call getName(), getColor() because they are
# accessible to child class through inheritance

c = Car("Ford Mustang", "red", "GT350")
print(c.getDescription())
print(c.getName())  # car has no method getName() but it is accessible through class Vehicle


# -----------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def whoami(self):
        return "I am " + self.name

    def __del__(self):
        print('I have been deleted')


p1 = Person('tom')
print(p1.whoami())
print(p1.name)
del p1


class Encapsulation(object):
    def __init__(self, a, b, c):
        self.Apublic = a
        self._Bprotected = b
        self.__Cprivate = c
        def getprivate (self):
            return self.__Cprivate
        
x = Encapsulation(11,13,17)
print (x.Apublic)
print( x._Bprotected )
print( x.__Cprivate )
print (x.getprivate ())

"""

class Circle:
    def __init__(self, radius) :
        self.__radius = radius

    def setRadius (self, radius) :
        self.__radius = radius
        
    def getRadius (self) :
        return self.__radius  
    
    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)

c1 = Circle (4)
print(c1.getRadius())
c2 = Circle (5)
print(c2.getRadius())
c3 = c1 + c2
print(c3.getRadius())














