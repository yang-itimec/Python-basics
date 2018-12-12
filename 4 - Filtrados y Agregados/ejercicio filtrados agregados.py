# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 14:56:54 2018

@author: PENG YANG YANG
"""
######################
# TEMA 4 - EJERCICIO #
######################

'''
Ejercicios filtrados y agregados

Filtrados:
1.	Crear una tabla como un subconjunto de SalePrice.
2.	Filtrar SalePrice según las variables de la nueva tabla, creando un nuevo Data Frame.
3.	Filtrar SalePrice según las observaciones de la nueva tabla, creando un nuevo Data Frame.
4.	Filtrar SalePrice según las observaciones de la nueva tabla, creando un nuevo Data Frame, quedándose con los elementos diferentes.
5.	Filtrar por los elementos de una variable, quedándose con los comunes (Eliminar alguna categoría para realizar el filtrado).
6.	Filtrar por una variable categorica y por una numérica.

Agregados:
1.	Agregar según una variable.
2.	Agregar según dos variables.
3.	Visualizar los elementos únicos de una variable, sin crear un nuevo conjunto de datos.
4.	Verticalizar por una y dos variables.
5.	Retornar a las tablas originales.
'''

%reset -f

#############
# FILTRADOS #
#############

#%% 1.	Crear una tabla como un subconjunto de SalePrice.

def pd_dfs_check(df1, df2):
    return df1.sort_index(axis=1).equals(df2.sort_index(axis=1))

dir ='C:/Users/ALUMNO/Downloads/Curso-Bilbao-C2B/4-Filtrados_y_Agregados/'
file = 'SalePrice.csv'

import pandas as pd

df = pd.read_csv( dir + file )

dff1 = df.iloc[100:200,0:20]

#%% 2.	Filtrar SalePrice según las variables de la nueva tabla, creando un nuevo Data Frame.

dff2 = df[df.columns.intersection(df1.columns)]

#%% 3.	Filtrar SalePrice según las observaciones de la nueva tabla, creando un nuevo Data Frame.

dff3 = df[df.index.isin(df1.index)]

#%% 4.	Filtrar SalePrice según las observaciones de la nueva tabla, creando un nuevo Data Frame, 
#   quedándose con los elementos diferentes.

dff4 = df[~df.index.isin(df1.index)]

#%% 5.	Filtrar por los elementos de una variable, quedándose con los comunes 
#   (Eliminar alguna categoría para realizar el filtrado).

dff5 = df.iloc[:,10:15] \
         .drop_duplicates()

#%% 6.	Filtrar por una variable categorica y por una numérica.

dff6a = df3[((df3['LotShape'] == 'IR1') | (df3['LotShape'] == 'IR2'))]
dff6b = df3[((df3['Id'] > 1600) & (df3['Id'] < 1651))]

#############
# AGREGADOS #
#############


#%% 1.	Agregar según una variable.

dfa1 = df.groupby(['Neighborhood',])['Id'] \
         .count() \
         .reset_index()

#%% 2.	Agregar según dos variables.

dfa2 = df.groupby(['Neighborhood','RoofStyle'])['Id'] \
         .count() \
         .reset_index()

#%% 3.	Visualizar los elementos únicos de una variable, sin crear un nuevo conjunto de datos.

dfa3 = pd.DataFrame(df['Neighborhood'].unique(), \
                    columns=['Neighborhood'])

#%% 4.	Verticalizar por una y dos variables.

dfa4a = pd.melt(df, id_vars = ['Id'])
dfa4b = pd.melt(df, id_vars = ['Id', 'Neighborhood'])

#%% 5.	Retornar a las tablas originales.

dfa5a = dfa4a.pivot(index = 'Id', \
                    columns = 'variable', \
                    values = 'value') \
             .reset_index() \
             .infer_objects()
dfa5b = dfa4b.pivot_table(index = ['Id', 'Neighborhood'], \
                          columns = 'variable', \
                          values = 'value', \
                          aggfunc = 'first') \
             .reset_index() \
             .infer_objects()

pd_dfs_check(df, dfa5b)
