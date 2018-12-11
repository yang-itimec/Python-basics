# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:20:49 2018

@author: PENG YANG YANG
"""
########################
# TEMA 1 - EJERCICIO 3 #
########################

'''
Ejercicios control de flujo y condicionales


1.	Crear una lista con 10 elementos numéricos.
2.	Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.
3.	Invertir el orden de la lista y realizar la misma comprobación.
4.	Añadir la posibilidad de que sea igual.
5.	Transformar el séptimo número para que se satisfaga la igualdad.
6.	Realizar la comprobación.
'''

%reset -f

#%% 1.	Crear una lista con 10 elementos numéricos.

import random

lista = random.sample(range(100), 10)
    
#%% 2.	Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.

if lista[2] > lista[6]:
    print('Elemento 3 mayor que elemento 7:', lista[2], '>', lista[6])
else:
    print('Elemento 3 menor o igual que elemento 7:', lista[2], '<=', lista[6])


#%% 3.	Invertir el orden de la lista y realizar la misma comprobación.

lista_inv = list(reversed(lista))

if lista_inv[2] > lista_inv[6]:
    print('Elemento 3 mayor que elemento 7:', lista_inv[2], '>', lista_inv[6])
else:
    print('Elemento 3 menor o igual que elemento 7:', lista_inv[2], '<=', lista_inv[6])

#%% 4.	Añadir la posibilidad de que sea igual.

if lista_inv[2] > lista_inv[6]:
    print('Elemento 3 mayor que elemento 7:', lista_inv[2], '>', lista_inv[6])
elif lista_inv[2] == lista_inv[6]:
    print('Elemento 3 igual que elemento 7:', lista_inv[2], '=', lista_inv[6])
else:
    print('Elemento 3 menor que elemento 7:', lista_inv[2], '<', lista_inv[6])

#%% 5.	Transformar el séptimo número para que se satisfaga la igualdad.

lista2 = lista[:]
lista2[6] = lista[2]

#%% 6.	Realizar la comprobación.

if lista2[2] > lista2[6]:
    print('Elemento 3 mayor que elemento 7:', lista2[2], '>', lista2[6])
elif lista2[2] == lista2[6]:
    print('Elemento 3 igual que elemento 7:', lista2[2], '=', lista2[6])
else:
    print('Elemento 3 menor que elemento 7:', lista2[2], '<', lista2[6])