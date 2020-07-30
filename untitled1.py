# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:00:20 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()
x,y,z=mc.player.getPos()
for i in range(5):
    r=random.randrange(1,5)
    #z+
    if r==1:
       mc.setBlock(x,y,z,x,y,z+4,1)
       z=z+4
    #z-
    if r==2:
        mc.setBlock(x,y,z,x,y,z-4,1)
        z=z-4
    #x-
    if r==3:
        mc.setBlock(x,y,z,x-4,y,z,1)
        x=x-4
    #x+
    if r==4:
        mc.setBlock(x,y,z,x+4,y,z,1)
        x = x+4
     
    
    