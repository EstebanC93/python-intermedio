# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:48:15 2021

@author: Esteban Henao
"""

def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def main():
    try: #try para cuando ingresan valores no numericos
        num = int(input("Ingresa un numero: "))
        if num < 0:
            #raise para cuando ingresan valores negativos
            raise Exception('Numeros negativos no validos')
        print(divisors(num))
        print("Termino el programa")
    except ValueError: #except del try
        print("Debes ingresar un numero")
    except Exception: #except del raise
        print("Debes ingresar numeros positivos")
        
        
    
if __name__ == '__main__':
    main()