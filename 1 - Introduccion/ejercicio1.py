# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 16:52:18 2018

@author: PENG YANG YANG
"""

########################
# TEMA 1 - EJERCICIO 1 #
########################

'''
Ejercicios Python básico.

Operaciones básicas
1.	Sumar 22,8 y 35,3
2.	Restar 25-10
3.	Multiplicar 3,14 por 5.
4.	Dividir 50 entre 4.
5.	Calcular de dos maneras la raíz cuadrada de 125.

Creación de variables simples
1.	Crear variables con las operaciones anteriores.

Comprobación de la clase
1.	Comprobar la clase de las variables creadas.

Creación de cadenas.
1.	Crear tres cadenas: Nombre y apellidos, lugar de nacimiento y lugar de residencia. 
2.	Comprobar el tipo de dato cada una de las cadenas.

Concatenación de cadenas.
1.	Crear la frase  “Me llamo ” “, nací en “ “ pero vivo en “ con vuestros datos concatenando frases.
2.	Medir la longitud de la cadena creada.

Extracción elementos de la cadena
1.	Extraer la ciudad en la que vivís.
2.	Extraer vuestras iniciales.

Transformar en mayúsculas/minúsculas.
 
1.	Poner todo con minúsculas.
 
 
 
Comprobar si existen ciertos elementos.
 
1.	Comprobar si existe vuestro nombre.
2.	Comprobar el número de veces que aparece la letra “a”.
 
 
Separar una cadena
 
1.	Separar vuestra cadena por espacios.
 
 
Transformar una cadena.
 
1.	Poner vuestros datos en mayúsculas.
 

Creación de listas
1.	Crear dos listas con los días de la semana y los días del mes del curso.
2.	Analizar el tipo de dato del primer elemento de cada lista.
3.	Concatenar las dos listas.
4.	Crear una lista encadenando los elementos de la lista 1
5.	Comprobar si existe el lunes y el día 18 en la lista concatenada.
6.	Eliminar el viernes y su correspondiente día del mes.
7.	Añadir el fin de semana y sus días del mes correspondientes en su lugar.



'''

%reset -f

#######################
# Operaciones básicas #
#######################

#%% 1.	Sumar 22,8 y 35,3

22.8 + 35.3

#%% 2.	Restar 25-10

25 - 10

#%% 3.	Multiplicar 3,14 por 5.

3.14 * 5

#%% 4.	Dividir 50 entre 4.

50 / 4

#%% 5.	Calcular de dos maneras la raíz cuadrada de 125.

125 ** 0.5

#%% 5.2

import math

math.sqrt(125)

#################################
# Creación de variables simples #
#################################

#%% 1.	Crear variables con las operaciones anteriores.

a = 22.8 + 35.3
b = 25 - 10
c = 3.14 * 5
d = 50 / 4
e1 = 125 ** 0.5
try:
    e2 = math.sqrt(125)
except:
    import math

    e2 = math.sqrt(125)

############################
# Comprobación de la clase #
############################

#%% 1.	Comprobar la clase de las variables creadas.

type(a)
type(b)
type(c)
type(d)
type(e1)
type(e2)

########################
# Creación de cadenas. #
########################

#%% 1.	Crear tres cadenas: Nombre y apellidos, lugar de nacimiento y lugar de residencia. 

nombre_apellidos = 'Peng Yang Yang'
lugar_nacimiento = 'Santurtzi'
lugar_residencia = 'Santurtzi'


#%% 2.	Comprobar el tipo de dato cada una de las cadenas.

bool = [type(nombre_apellidos) == str, 
        type(lugar_nacimiento) == str, 
        type(lugar_residencia) == str]

if False in bool:
    print('Revisar las cadenas introducidas')
else:
    print('Cadenas introducidas correctas')
#############################
# Concatenación de cadenas. #
#############################

#%% 1.	Crear la frase  “Me llamo ” “, nací en “ “ pero vivo en “ con vuestros datos concatenando frases.

print('Me llamo', nombre_apellidos, 'nací en', lugar_nacimiento, 'pero vivo en', lugar_residencia)

if lugar_nacimiento == lugar_residencia:
    frase = 'Me llamo ' + nombre_apellidos + ' nací en ' + lugar_nacimiento + ' y vivo en ' + lugar_residencia
else:
    frase = 'Me llamo ' + nombre_apellidos + ' nací en ' + lugar_nacimiento + ' pero vivo en ' + lugar_residencia

print(frase)

#%% 2.	Medir la longitud de la cadena creada.

len(frase)

#####################################
# Extracción elementos de la cadena #
#####################################

#%% 1.	Extraer la ciudad en la que vivís.

frase_ciudad_vida = frase.split('vivo en ')
frase_ciudad_vida[1]

#%% 2.	Extraer vuestras iniciales.

iniciales = frase.split('Me llamo ')[1].split(' ')[0:3]
iniciales = [x[0] for x in iniciales]
iniciales = ''.join(iniciales)

########################################
# Transformar en mayúsculas/minúsculas.#
########################################
 
#%% 1.	Poner todo con minúsculas.

iniciales_minus = iniciales.lower()

###########################################
# Comprobar si existen ciertos elementos. #
###########################################
 
#%% 1.	Comprobar si existe vuestro nombre.

if (nombre_apellidos in frase) == True:
    print('Existe!')
else:
    print('No existe... :(')

#%% 2.	Comprobar el número de veces que aparece la letra “a”.

frase.count('a')

######################
# Separar una cadena #
######################
 
#%% 1.	Separar vuestra cadena por espacios.

frase_espacios = frase.split(' ')

###########################
# Transformar una cadena. #
###########################
 
#%% 1.	Poner vuestros datos en mayúsculas.

NOMBRE_APELLIDOS = nombre_apellidos.upper()
LUGAR_NACIMIENTO = lugar_nacimiento.upper()
LUGAR_RESIDENCIA = lugar_residencia.upper()

if lugar_nacimiento == lugar_residencia:
    frase = 'Me llamo ' + NOMBRE_APELLIDOS + ' nací en ' + LUGAR_NACIMIENTO + ' y vivo en ' + LUGAR_RESIDENCIA
else:
    frase = 'Me llamo ' + NOMBRE_APELLIDOS + ' nací en ' + LUGAR_NACIMIENTO + ' pero vivo en ' + LUGAR_RESIDENCIA

print(frase)
 
######################
# Creación de listas #
######################

#%% 1.	Crear dos listas con los días de la semana y los días del mes del curso.

dias_sem =['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
dias_diciembre = []
dias = 1
while dias <= 31:
    dias_diciembre.append(dias)
    dias = dias + 1

#%% 2.	Analizar el tipo de dato del primer elemento de cada lista.

type(dias_sem[0])
type(dias_diciembre[0])

#%% 3.	Concatenar las dos listas.

dias_concatenadas = dias_sem + dias_diciembre

#%% 4.	Crear una lista encadenando los elementos de la lista 1

dias_encadenadas = []
i = 5
for j in dias_diciembre:
    if i >6:
        i=0
    dias_encadenadas.append(dias_sem[i] + ' ' + str(j))
    i = i + 1
    
dias_encadenadas

#%% 5.	Comprobar si existe el lunes y el día 18 en la lista concatenada.

Lunes in dias_concatenadas
18 in dias_concatenadas

#%% 6.	Eliminar el viernes y su correspondiente día del mes.
dias_encadenadas2 = dias_encadenadas[:]

for j in dias_encadenadas2:
    if ('Viernes' in j) == True:
        dias_encadenadas2.remove(j)

#%% 7.	Añadir el fin de semana y sus días del mes correspondientes en su lugar.

dias_encadenadas3 = dias_encadenadas[:]

for j in dias_encadenadas3:
    if ('Viernes' in j) == True:
        ix = dias_encadenadas3.index(j)
        dias_encadenadas3[ix] = dias_encadenadas3[ix:ix+3]
        
print(dias_encadenadas3)
        