# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:20:46 2020

@author: appedu
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z=hit.pos.x, hit.pos.y, hit.pos.z
        blockID=mc.getBlock(x,y,z)
        print("ID"+str(blockID))
        mc.postToChat("ID"+str(blockID))
        