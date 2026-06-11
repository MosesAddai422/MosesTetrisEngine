#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from keyclasses import CustomPiece, Builder

class Tetris:
    def __init__(self, width: int = 10, height: int = 100 ):
        self.width = width
        self.height = height
        self.restblocks = set()
        self.activepiece = None
        
    """function to spawn new pieces and position them at designated starting points"""
    def newshape(self, shape:CustomPiece,targetcol = int):
        
        leftcoord = min(sq.x for sq in shape.squares)
        dx = targetcol - leftcoord #determining location on grid to initiate piece based on left-most column info from command
        shape.move(dx=dx, dy = self.height)
        #
        self.activepiece = shape
    
    """function to check contact with floor of grid or other resting blocks"""
    def contactcheck(self, nextcoords) -> bool:
        for x,y in nextcoords:
            #checking grid floor contact
            if y<0:
                return True
            #checking resting block contact
            if (x,y) in self.restblocks:
                return True
            
        return False
    
    """function to clear filled rows and shift higher blocks down"""
    def cleaner(self):
        cleanrows = 0
        for y in range(self.height):
            rowblocks = [x for x in range(self.width) if (x,y) in self.restblocks]
            
            #comparing length of blocks at the bottom to grid length
            if len(rowblocks) == self.width:
                cleanrows += 1
                
                #deleting filled row at bottom
                for x in range(self.width):
                    self.restblocks.remove((x,y))
                    
                #shifting all blocks one level down
                newresting = set() 
                for rx, ry in self.restblocks:
                    if ry>y:
                        newresting.add((rx,ry-1))
                    else: 
                        newresting.add((rx,ry))
                        
                self.restblocks = newresting 
                return self.cleaner()
            
    """function to compute height of remaining blocks"""
    def peakheight(self) -> int:
        if not self.restblocks:
            return 0
        peak = max(ry for rx,ry in self.restblocks)
        return peak +1
    
    """function to coordinate height check, movement of shapes,collision checks and filled row cleaning""" 
    def operator(self):
        if not self.activepiece: 
            return

        futurecoords = self.activepiece.futurecoord(dx = 0, dy = -1)
        
        #if there is contact with bottom of grid or rest block, the info is added to restblocks
        if self.contactcheck(futurecoords):
            for sq in self.activepiece.squares:
                self.restblocks.add((sq.x, sq.y))
                
            self.activepiece = None
            self.cleaner()
            
        else:
            self.activepiece.move(dx = 0, dy = -1)
            
    """function to clear the grid after each round or line"""
    def cleargrid(self):
        self.restblocks.clear()
        self.activepiece = None   
                    
                
                
#Execution 

"""map to match shapes to respective builders"""
board = Tetris()
shapemap = {
    'Q': Builder.qshape(),
    'L': Builder.lshape(),
    'I': Builder.ishape(),
    'T': Builder.tshape(),
    'Z': Builder.zshape(),
    'S': Builder.s_shape(),
    'J': Builder.jshape(),
}

"""function to take in input string and process commands within the string"""
def feeder(inp_string):
    commands = [cmd.strip() for cmd in inp_string.split(",") ]
    for cmd in commands:
        if not cmd:
            continue
        piecetype = cmd[0]
        targetcol = int(cmd[1])
        
        newpiece = shapemap.get(piecetype)
        board.newshape(newpiece,targetcol)
        
        while board.activepiece is not None:
            board.operator()
            
    peakheight = board.peakheight()
    print(peakheight)
    board.cleargrid()
    

"""main function to boot the game engine"""
def runengine():
    for line in sys.stdin:  
        stripline = line.strip()
        if not stripline:
            continue
        feeder(stripline)
    
if __name__ == "__main__":
    runengine()


     
            
        