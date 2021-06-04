# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:17:43 2021

@author: Esteban Henao
"""

def main():
#    squares = []
#    for i in range(1,101):
#        if i % 3 != 0:
#            squares.append(i**2)


     squares = [i**2 for i in range(1,101) if i % 3 != 0]
     numbs = [i for i in range(1, 100000) if i % 4 == 0 and i % 6 == 0 
              and i % 9 == 0]
     print (squares)
     print("")
     print("")
     print("OTRA LISTA DE DATOS")
     print("")
     print("")
     
     print (numbs)
    
if __name__ == '__main__':
    main()