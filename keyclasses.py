#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""class for unit square"""
class UnitSquare:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        
    def move(self, dx = int, dy = int):
        self.x += dx
        self.y += dy
        
    def __repr__(self):
        return f"({self.x,self.y})"
    
"""class to build and control the predefined custom pieces"""
class CustomPiece: 
    def __init__(self):
        self.squares = []
        
    def addsquare(self, square:UnitSquare): #function to build a custom piece square by square
        self.squares.append(square)
        
    @property
    def coordinates(self):
        return {(sq.x,sq.y) for sq in self.squares}
    
    def move(self, dx = int, dy = int): #function to move the piece as a whole
        for square in self.squares:
            square.move(dx,dy)
            
    #function to project a piece's future location based on a specific movement        
    def futurecoord(self, dx:int, dy:int):
        return {(sq.x+dx, sq.y+dy) for sq in self.squares}
            
"""class to execute building of pieces"""
class Builder:
    #function for q piece(square shape)
    def qshape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(1, 1))
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(1, 2))
        shape.addsquare(UnitSquare(2, 2))
        return shape
    
    #function for z piece
    def zshape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(3, 1))
        shape.addsquare(UnitSquare(2, 2))
        shape.addsquare(UnitSquare(1, 2))
        return shape
    
    #function for s piece
    def s_shape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(1, 1))
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(2, 2))
        shape.addsquare(UnitSquare(3, 2))
        return shape
        
    #function for t piece
    def tshape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(2, 2))
        shape.addsquare(UnitSquare(1, 2))
        shape.addsquare(UnitSquare(3, 2))
        return shape
    
    #function for i piece(horizontal bar shape)
    def ishape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(1, 1))
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(3, 1))
        shape.addsquare(UnitSquare(4, 1))
        return shape
        
    #function for l piece
    def lshape() -> CustomPiece:
        shape = CustomPiece()
        shape.addsquare(UnitSquare(1, 1))
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(1, 2))
        shape.addsquare(UnitSquare(1, 3))
        return shape
        
    #function for j piece
    def jshape() -> CustomPiece():
        shape = CustomPiece()
        shape.addsquare(UnitSquare(1, 1))
        shape.addsquare(UnitSquare(2, 1))
        shape.addsquare(UnitSquare(2, 2))
        shape.addsquare(UnitSquare(2, 3))
        return shape
    


        
        