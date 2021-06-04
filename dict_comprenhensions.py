# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 07:50:48 2021

@author: Esteban Henao
"""
import math

def main():
    
#   dict = {}
   
#   for i in range(1,101):
#       if i % 3 !=0:
#           dict[i] = i**3

    #dict = {i : i**3 for i in range(1,101) if i % 3 != 0}
    
    dict = {i : math.sqrt(i) for i in range(1, 1001)}
    
    print(dict)

if __name__ == '__main__':
    main()