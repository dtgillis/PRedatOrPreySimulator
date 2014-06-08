'''
Created on Mar 10, 2014

@author: dtgillis
'''
 

import numpy as np 
import Animal.baseAnimal as bA 
import matplotlib.pyplot as plt
import random
def doStuff():
    awolf =  bA.wolf()
    asheep = bA.sheep()
    awolf.x = 100*random.random()
    awolf.y = 100*random.random()
    
    awolf.sex=1
    awolf.moveAround()
    achild = awolf.giveBirth()
    achild.beBorn(awolf)
    achild.age=1
    i=0
    points_wolf = []
    points_sheep = []  
    while i < 10000:
        i+=1
        asheep.moveAround()
        awolf.moveAround()
        achild.x = awolf.x
        achild.y = awolf.y
        points_wolf.append((awolf.x,awolf.y))
        points_sheep.append((asheep.x,asheep.y))
    point_np_sheep = np.array(points_sheep)
    point_np_wolf = np.array(points_wolf)
    plt.plot(point_np_sheep[:,0],point_np_sheep[:,1])
    plt.plot(point_np_wolf[:,0],point_np_wolf[:,1])
    plt.show()
        
        
    


if __name__ == '__main__':
    doStuff()