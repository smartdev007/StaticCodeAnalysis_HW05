# -*- coding: utf-8 -*-
"""
Updated Feb 2, 2020
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Jenish Kevadia
"""

import unittest

from static_tri import check_tri

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(check_tri(4,3,5), ('Right'))
    def testRightTriangleB(self): 
        self.assertEqual(check_tri('1',3,5), ('InvalidInput'))
    def testRightTriangleC(self): 
        self.assertEqual(check_tri('',3,5), ('InvalidInput'))

    def testScaleneTriangleA(self): 
        self.assertEqual(check_tri(5,3,4), ('Scalene'))
    def testScaleneTriangleB(self): 
        self.assertEqual(check_tri(4,'a',0), ('InvalidInput'))
    def testScaleneTriangleC(self): 
        self.assertEqual(check_tri('','a',1), ('InvalidInput'))

    def testEquilateralTriangleA(self): 
        self.assertEqual(check_tri(1,1,1), ('Equilateral'))
    def testEquilateralTriangleB(self): 
        self.assertEqual(check_tri('1','a',1), ('InvalidInput'))
    def testEquilateralTriangleC(self): 
        self.assertEqual(check_tri('',1,1), ('InvalidInput'))
    
    def testIsoscelesTriangleA(self): 
        self.assertEqual(check_tri(1,2,1), ('Isoceles'))
    def testIsoscelesTriangleB(self): 
        self.assertEqual(check_tri(1,'',1), ('InvalidInput'))
    def testIsoscelesTriangleC(self): 
        self.assertEqual(check_tri(1,2,'1'), ('InvalidInput'))

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

