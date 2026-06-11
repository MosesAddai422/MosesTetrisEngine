#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest

from tetris_engine import Tetris
from keyclasses import Builder

class enginetest(unittest.TestCase):
    
    """function to test whether the peakheight function correctly computes the height of the remaining blocks in the grid"""
    def test_peakheight(self):
        board = Tetris()
        self.assertEqual(board.peakheight(), 0) #initializing height as 0 for empty grid
        
        board.restblocks = {(0,0),(9,5),(5,1)} #inserting mock blocks at specific coordinates on the grid
        self.assertEqual(board.peakheight(),6) #testing function and comparing its response to ground truth height
        
    
    """function to test whether the Builder class produces shapes that contain only four unit squares"""
    def test_shapegen(self):
        
        shapemap = {
            'Q': Builder.qshape,
            'L': Builder.lshape,
            'I': Builder.ishape,
            'T': Builder.tshape,
            'Z': Builder.zshape,
            'S': Builder.s_shape,
            'J': Builder.jshape,
        }
        
        for name, builder in shapemap.items():
            piece = builder()
            self.assertEqual(len(piece.squares), 4) #comparing total number of shape pieces from Builder to four
            
            
    """function to test the functionality of the engine's line clearing ability when a row is filled as well as shifting of blocks down to vacated space""" 
    def test_lineclearing(self):
        board = Tetris()
        
        #scenario where row 0 and 1 are completely full with a block on top
        fullrow0 = {(x,0) for x in range(10)}
        fullrow1 = {(x,1) for x in range(10)}
        floatblock = {(5,2)}
        
        board.restblocks = fullrow0.union(fullrow1,floatblock)
        
        #running line clearing function
        board.cleaner()
        
        #expected block after two rows have been cleared
        expected_blocks = {(5,0)}
        
        self.assertEqual(board.restblocks, expected_blocks) #comparing remaining blocks with expected blocks
        


if __name__ == "main":
    unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        