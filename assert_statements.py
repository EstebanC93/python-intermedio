# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:17:39 2021

@author: Esteban Henao
"""

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    num = input("Ingresa un numero: ")
    assert num.isnumeric(), "Debes ingresar un numero"
    print(divisors(int(num)))
    print("Termino el programa")        
        
    
if __name__ == '__main__':
    main() 