#---------------------------------------------
#Matthew Busch 3/18/20 Midterm Coding Portion
#---------------------------------------------

import pygame
from pygame.locals import *

vector = pygame.math.Vector2


#---------------------------------------
# Ship Class
#---------------------------------------

#for this portion of the class I am using the pygame.math.vector and NOT my own written vector class

#the original ship class uses midBottom for centering and spawning, however i prefer to have a defined location as a spawn
#I included the original method as well as a commet

class Ship():
    def __init__(self, game, startingPos = vector(0,0)):
        self.game = game
        self.scren = game.screen

        self.startingPos = vector(startingPos)

        self.image = pygame.image.load('images/ship.jpg')
        self.rect = self.image.get_rect()
        self.rect.topleft = vector(startingPos)
        #-------------------------------0
        #original method below
        #self.screenRect = game.screen.get_rect()
        #self.rect.midbottom = self.screenRect.midbottom
        #-------------------------------

        #initialized to not move at start
        self.velocity = vector(0,0)

        self.lasers = pygame.sprite.Group()

    def center_ship(self):
        self.rect.topleft = self.startingPos

    def fire(self):
        self.lasers.add(Laser(self.game))

    def remove_lasers(self):
        #deletes all lasers, the method to remove individual lasers was in update?
        self.lasers.remove()

    def move(self):
        #using pygame.math.vector, we do not need to split attributes into x&y
        self.rect.topleft += self.velocity
        self.game.limit_on_screen(self.rect)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):

        self.move()
        self.draw()
        #assuming that this is implemented the same way as before and ship still manages lasers etc..~~~
        for laser in self.lasers.sprites():
            laser.update()
        for laser in self.lasers.copy():
            if laser.rect.bottom < 0:
                self.lasers.remove(laser)

        pygame.sprite.groupcollide(self.lasers, self.game.fleet.aliens, True, True)
        if not self.game.fleet.aliens:
            self.game.restart()



#---------------------------------------
# Vector Class
#---------------------------------------
class Vector():
def __init__(self, x = 0, y = 0):
    self.x = x
    self.y = y

def __repr__ (self):
    return "Vector({}{})".format(self.x, self.y)

def __add__(self, other):
    return Vector(self.x + other.x, self.y + other.y)

def __sub__(self, other):
    return self.__add__(- other)
    #returning the added negative

def __mul__(self, k:float):
    return vector(k+self.x,k+self.y)

def __rmul__(self, k:float):
    return k * self
def __truediv__(self, k:float):
    return 1/k*self

def __neg__(self):
    return -1 * self
#the equality operator was listed as __eq__(self) but should be __eq__(self, other) because it's testing equality against another Vector
def __eq__(self,other):
    return self.x == other.x and self.y == other.y


@staticmethod
def test(): # feel free to change the test code
 v = Vector(x=5, y=5)
 u = Vector(x=4, y=4)
 print('v is {}'.format(v))
 print('u is {}'.format(u))
 print('uplusv is {}'.format(u + v))
 print('uminusv is {}'.format(u – v))
 print('ku is {}'.format(3 * u))
 print('-u is {}'.format(-1 * u))
def main():
 Vector.test()
