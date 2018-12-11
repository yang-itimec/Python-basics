# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 18:33:16 2018

@author: PENG YANG YANG
"""
########################
# TEMA 1 - EJERCICIO 4 #
########################

'''
Ejercicios de Iteraciones

1.	Crear y mostrar una secuencia numérica con un valor incremental de 5, hasta el valor 150. Realizarlo de tres maneras diferentes.
2.	Crear un función que diga si un numero es par o impar.
3.	Utilizando la función “for” crear un valor “a” y uno “b” de forma que b sea igual al cuadrado de “a”, del 1 al 50.
4.	Crea un frase y analiza si existe la letra “a” y la “o”
'''

%reset -f

#%% 1.	Crear y mostrar una secuencia numérica con un valor incremental de 5, hasta el valor 150. Realizarlo de tres maneras diferentes.

a = 5                    
while a > 0:              
   print (a)
   a = a + 5
   if a > 150:
      break

#%% 1.2
    
for a in range(5,155,5):
    print(a)
    
#%% 1.3

while a <= 150:
    print(a)
    a = a + 5

#%% 2.	Crear un función que diga si un numero es par o impar.

def par_impar(x):
    if x%2 == 0:
        print('Par!')
    else:
        print('Impar!')

par_impar(3549)
par_impar(6548)

#%% 3.	Utilizando la función “for” crear un valor “a” y uno “b” de forma que b sea igual al cuadrado de “a”, del 1 al 50.

for a in range(1,50):
    b = a**2
    print(a,b)

#%% 4.	Crea un frase y analiza si existe la letra “a” y la “o”
    
frase = input('Introduce una frase: ')

if ('a' in frase or 'o' in frase) == True:
    print('Contiene a u o')
else:
    print('No contiene a u o')