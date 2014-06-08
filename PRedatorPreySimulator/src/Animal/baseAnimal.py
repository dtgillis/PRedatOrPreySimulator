'''
Created on Mar 10, 2014

@author: dtgillis
'''

import random as rand
import math
class Animal(object):
    '''
    classdocs
    '''



    def __init__(self):
        '''
        Constructor
        '''
        # initiate some stuff
        self.x=0
        self.y=0
        self.sex=0
        self.health=1.0
        self.descendants=[]
        self.speed=1.0
        self.age=0.0
    
    def beBorn(self,parent):
        '''
        Into the breach my friend
        '''
        tmp = rand.random()
        if tmp < .5:
            self.sex=1
        else:
            self.sex=0
        self.x=parent.x
        self.y=parent.y
        self.health=.8
        
    def giveBirth(self):
        '''
        Prepare to be dissapointed 
        '''
        child = Animal()
        child.beBorn(self)
        self.descendants.append(child)
        return child 
    
    def moveAround(self):
        '''
        Random walk movement for a time step
        '''
        # choose random direction 
        theta = rand.random() * ( 2 * math.pi)
        self.x+= self.speed*math.cos(theta)
        self.y+= self.speed*math.sin(theta)

    def eatFood(self):
        '''
        Hungry why wait?
        '''
        
        
        
        
class wolf(Animal):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        Animal.__init__(self)
        
    
    def giveBirth(self):
        '''
        Prepare to be dissapointed 
        '''
        child = wolf()
        child.beBorn(self)
        self.descendants.append(child)
        return child 

class sheep(Animal):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        Animal.__init__(self)
        
    
    def giveBirth(self):
        '''
        Prepare to be dissapointed 
        '''
        child = sheep()
        child.beBorn(self)
        self.descendants.append(child)
        return child 

             
        
        