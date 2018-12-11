# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:51:53 2018

@author: PENG YANG YANG
"""
########################
# TEMA 1 - EJERCICIO 2 #
########################

'''
Ejercicios mutaciones, alias y clonaciones

1-	Crear una lista con los meses del año (lista1).
2-	Crear un alias de la lista (lista2).
3-	Clonar la lista (lista3).
4-	Añadir a la lista1 “Fin de Año”
5-	Mostrar la lista2 y la lista3.
'''

%reset -f

#%% 1- Crear una lista con los meses del año (lista1).

lista1 = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
          'Septiembre','Octubre','Noviembre','Diciembre']
lista1

#%% 2- Crear un alias de la lista (lista2).

lista2 = lista1
lista2

#%% 3- Clonar la lista (lista3).

lista3 = lista1[:]
lista3

#%% 4- Añadir a la lista1 “Fin de Año”

lista1.append('Fin de Año')
lista1

#%% 5- Mostrar la lista2 y la lista3.

print(lista2)
print(lista3)