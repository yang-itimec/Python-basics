# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 19:08:30 2018

@author: PENG YANG YANG
"""
########################
# TEMA 1 - EJERCICIO 6 #
########################

'''
Ejercicios de recursividad

1.	Crear una función que recursivamente divida el elemento final entre la suma de los elementos anteriores de una lista. 
Y entre el producto de los elementos anteriores 
2.	Crear una función que sea el doble de la función de Fibonacci
3.	Crear una función que replique la tabla del 7 sin hacer multiplicaciones, añadiendo la opción de que exista el 0.

Nota: Puede que para algunos ejercicios sea necesario utilizar más de una función

.

'''

%reset -f

#%% 1.	Crear una función que recursivamente divida el elemento final entre la suma de los elementos anteriores de una lista. 
#   Y entre el producto de los elementos anteriores 

lista = [1,2,3,4,5,6,7,8]

def suma_recursiva(lista):
    if len(lista)==1:
        return 0
    else:
        return lista[-2]+suma_recursiva(lista[:-1])
        
suma_recursiva(lista)

def producto_recursivo(lista):
    if len(lista)==1:
        return 0
    elif len(lista)==2:
        return lista[-2]
    else:
        return lista[-2]*producto_recursivo(lista[:-1])

producto_recursivo(lista)

def function1(lista):
    return lista[-1]/suma_recursiva(lista)

function1(lista)

def function2(lista):
    return lista[-1]/producto_recursivo(lista)

function2(lista)

#%% 2.	Crear una función que sea el doble de la función de Fibonacci

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
    
def fib_doble(n):
        return fib(n)*2
   
def fib_doble_2(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2*fib(n-1)+2*fib(n-2)

fib(28)
fib_doble(28)
fib_doble_2(28)

#%% 3.	Crear una función que replique la tabla del 7 sin hacer multiplicaciones, añadiendo la opción de que exista el 0.

def tabla7(n):
    if n == 0:
        print(7,'x',n,'=',(n)*7)
        return 0
    else:
        print(7,'x',n,'=',(n)*7)
        return tabla7(n-1)+7
            
tabla7(100)
