# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:23:39 2021

@author: Esteban Henao
"""

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    
    #metodo list comprenhesions
    
    #all_platzi_workers = [worker['name'] for worker in DATA 
    #                      if worker["organization"] == 'Platzi']
    
    #metodo high order functions
    
    all_platzi_workers = list(filter(lambda worker: worker["organization"],
                                     DATA))
    all_platzi_workers2 = list(map(lambda worker: worker["name"],
                                   all_platzi_workers))
    
    for worker in all_platzi_workers2:
        print(worker)
        
    print("---------------------------------------------------------------")
    
    #metodo high order functions
    
    #adults = list(filter(lambda worker: worker["age"] > 18, DATA))
    #adults = list(map(lambda worker: worker["name"], adults))
    #old = list(map(lambda worker: worker | {"old" : worker["age"] > 70},
    #               DATA)) #el operador | solo aplica para la version de
    #python 3.9 en adelante, como esta version es 3.8 no funciona
    
    #metodo list comprenhensions
    
    adult = [worker['name'] for worker in DATA
             if worker["age"] > 18]
    
    old = [worker["name"] for worker in DATA
           if worker["age"] > 70]
        
    for worker in adult:
        print(worker)
        
    for worker in old:
        print(worker)
     
    
if __name__ == '__main__':
    main()