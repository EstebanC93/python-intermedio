# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 06:35:56 2021

@author: Esteban Henao
"""

def read():
    numbers = []
    with open(r'C:\Users\Esteban Henao\Desktop\python\python intermedio\archivos\numbers.txt',
              "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    
    
def write():
    names = ["Esteban", "Zlatan", "Rocío", "Carlos", "Ñoño"]
    with open(r'C:\Users\Esteban Henao\Desktop\python\python intermedio\archivos\names.txt',
              "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")
            
            
def append():
    names = ["George", "Rene", "Antonella", "Karol", "Enzo"]
    with open(r'C:\Users\Esteban Henao\Desktop\python\python intermedio\archivos\names.txt',
              "a", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")


def main():
    append()
    
    
if __name__ == '__main__':
    main()