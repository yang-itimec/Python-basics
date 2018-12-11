# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:19:15 2018

@author: PENG YANG YANG
"""
######################
# TEMA 3 - EJERCICIO #
######################

'''
Ejercicios ETL

1-	Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables diferentes en cada caso.
2-	Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables comunes y diferentes en cada caso.
3-	Realizar uniones de los tres primeros grupos:
    a.	Incluyendo todas las variables y todas las observaciones, por el índice.
    b.	Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.
    c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.
4-	Realizar uniones de los tres grupos creados en el punto 2:
    a.	Incluyendo todas las variables y todas las observaciones, por el índice.
    b.	Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.
    c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.
5-	Realizar dos grupos con observaciones comunes y variables únicas, incluyendo la Id en las dos tablas:
    a.	Incluyendo todas las variables y todas las observaciones, por la Id.
    b.	Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.
    c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de la otra tabla, por la Id.
6-	Realizar dos grupos con observaciones y variables comunes, incluyendo la Id en las dos tablas:
    a.	Incluyendo todas las variables y todas las observaciones, por la Id.
    b.	Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.
    c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de la otra tabla, por la Id.
7-	Realizar un cambio de caracteres a una variable y a todas las variables.
8-	Realizar un cambio de elementos en una variable y en todo el Data Frame

'''

%reset -f

dir ='C:/Users/ALUMNO/Downloads/Curso-Bilbao-C2B/3-ETL_y_Enriquecimiento/'
file = 'SalePrice.csv'

import pandas as pd

df = pd.read_csv( dir + file )

#%% 1-	Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables diferentes en cada caso.

df1 = df.iloc[0:50,0:20]
df2 = df.iloc[40:90,21:50]
df3 = df.iloc[20:100,51:80]

#%% 2-	Dividir el Dataset en tres grupos con usuarios comunes y diferentes y variables comunes y diferentes en cada caso.

dfa = df.iloc[0:50,0:30]
dfb = df.iloc[40:90,25:55]
dfc = df.iloc[20:100,51:80]

#%% 3-	Realizar uniones de los tres primeros grupos:



    #%% a.	Incluyendo todas las variables y todas las observaciones, por el índice.

    df_union_3a = pd.concat([df1,df2,df3], \
                            sort = False )

    #%% b.	Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.

    df_union_3b = pd.concat([df1,df2,df3], \
                            axis = 1, \
                            join = 'inner', \
                            #join_axes = , \
                            sort = False )

    #%% c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.

    df_union_3c = pd.concat([df2,df1,df3], \
                            axis = 1, \
                            #join = 'inner', \
                            join_axes = [df2.index], \
                            sort = False )\
                    .loc[:,~df2.columns.duplicated()]

#%% 4-	Realizar uniones de los tres grupos creados en el punto 2:



    #%% a.	Incluyendo todas las variables y todas las observaciones, por el índice.

    df_union_4a = pd.concat([dfa,dfb,dfc], \
                            sort = False )

    #%% b.	Incluyendo las observaciones comunes de las tres tablas y todas las variables, por el índice.

    df_union_4b = pd.concat([dfa,dfb,dfc], \
                            axis = 1, \
                            join = 'inner', \
                            sort = False )

    #%% c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de las otras dos tablas, por el índice.

    df_union_4c = pd.concat([dfb,dfa,dfc], \
                            axis = 1, \
                            #join = 'inner', \
                            join_axes = [dfb.index], \
                            sort = False )\
                    .loc[:,~dfb.columns.duplicated()]

#%% 5-	Realizar dos grupos con observaciones comunes y variables únicas, incluyendo la Id en las dos tablas:

df51 = df.iloc[0:50,0:20]
df52 = df.iloc[30:80,21:40]
df52['Id'] = df.iloc[30:38,0]

    #%% a.	Incluyendo todas las variables y todas las observaciones, por la Id.

    df5a = pd.merge(df51, \
                    df52, \
                    how = 'outer', \
                    on = 'Id')

    #%% b.	Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.

    df5b = pd.merge(df51, \
                    df52, \
                    how = 'inner', \
                    on = 'Id')

    #%% c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de la otra tabla, por la Id.

    df5c = pd.merge(df51, \
                    df52, \
                    how = 'right', \
                    on = 'Id')

#%% 6-	Realizar dos grupos con observaciones y variables comunes, incluyendo la Id en las dos tablas:

df61 = df.iloc[0:50,0:30]
df62 = df.iloc[30:80,21:50]
df62['Id'] = df.iloc[30:38,0]

    #%% a.	Incluyendo todas las variables y todas las observaciones, por la Id.

    df6a = pd.merge(df61, \
                    df62, \
                    how = 'outer', \
                    on = 'Id')

    #%% b.	Incluyendo las observaciones comunes de las dos tablas y todas las variables, por la Id.

    df6b = pd.merge(df61, \
                    df62, \
                    how = 'inner', \
                    on = 'Id')

    #%% c.	Incluyendo las observaciones de la tabla dos y enriqueciendo esa información con la información de la otra tabla, por la Id.

    df6c = pd.merge(df61, \
                    df62, \
                    how = 'right', \
                    on = 'Id')

#%% 7-	Realizar un cambio de caracteres a una variable y a todas las variables.

df7 = dfa.copy()
df7['MSZoning'] = df7['MSZoning'].map(lambda x: x.replace('R','r'))

#%% 8-	Realizar un cambio de elementos en una variable y en todo el Data Frame
    
df8 = dfa.copy()
df8 = df8.replace({'RL':'rl', \
                   'NAmes':'Names', \
                   'TA':'ta'})
    
