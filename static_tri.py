# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Feb 2, 2020

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: Jenish Kevadia
"""

def check_tri(var1, var2, var3):
    """
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
    """
    if not(isinstance(var1, int) and isinstance(var2, int) and isinstance(var3, int)):
        return 'InvalidInput'
    if var1 > 200 or var2 > 200 or var3 > 200:
        return 'InvalidInput'
    if var1 <= 0 or var2 <= 0 or var3 <= 0:
        return 'InvalidInput'
    if (var1 > (var2 + var3)) or (var2 > (var1 + var3)) or (var3 > (var1 + var2)):
        return 'NotATriangle'
    if var1 == var2 and var2 == var3 and var3 == var1:
        return 'Equilateral'
    elif ((var1 ** 2) + (var2 ** 2)) == (var3 ** 2):
        return 'Right'
    elif (var1 != var2) and  (var2 != var3) and (var1 != var3):
        return 'Scalene'
    else:
        return 'Isoceles'
