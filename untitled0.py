# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:56:33 2020

@author: appedu
"""
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
number=1
for i in range(8): 
    for j in range(nember):
        mc.spawnEntity(x,y,z,60)
    number = number*2
    mc.postToChat(")      
