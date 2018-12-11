# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:49:29 2018

@author: PENG YANG YANG
"""
########################
# TEMA 1 - EJERCICIO 5 #
########################

'''
Ejercicios Funciones

1.	Crear una función que divida un número por tres.
2.	Crear una función que eleve a la 10 un determinado valor.
3.	Crear una función que calcule el área de una circunferencia.
4.	Crear una función que calcule el área de un triángulo.
5.	Crear una función que determine si un número es impar.

'''

%reset -f

#%% 1.	Crear una función que divida un número por tres.

def dividir3(x):
    return x/3

#%% 2.	Crear una función que eleve a la 10 un determinado valor.

def power10(x):
    return x**10

#%% 3.	Crear una función que calcule el área de una circunferencia.

def area_circulo(**kwargs):
    from math import pi
    radio = kwargs.get('radio', None)
    diametro = kwargs.get('diametro', None)
    if radio != None and diametro != None:    
        if diametro / 2 != radio:
            print('Valores erróneos')
            raise ValueError
    elif radio == None and diametro == None:    
        print('Valores Vacíos')
        raise ValueError
    if radio != None:
        area = pi*(radio**2)
    elif diametro != None:    
        radio = diametro / 2
        area = pi*(radio**2)
    return area

print(area_circulo(radio = 2))
print(area_circulo(diametro = 2))
print(area_circulo(radio = 2, diametro = 4))
print(area_circulo(radio = 2, diametro = 6))

#%% 4.	Crear una función que calcule el área de un triángulo.

def area_triangulo(base, altura):
    return base*altura/2

#%% 5.	Crear una función que determine si un número es impar.

def impar(x):
    if x%2 == 0:
        print('Par!')
    else:
        print('Impar!')