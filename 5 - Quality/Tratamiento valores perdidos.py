#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Cargamos los datos
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[2]:


# Lo primero que debemos hacer es visualizar los datos
print(data)


# In[3]:


# Tambien podemos visualizar un numero determinado para mayor comodidad
data.head(n=10)


# In[4]:


#Tambien tenemos la opcion de realizar un "resumen estadistico" de cada una de las variables.
data.describe()


# In[5]:


# Una vez conocidos nuestros datos procedemos a analizar su completitud.
# Tenemos que saber cuantos valores perdidos tenemos de cada variable antes de tomar una decision sobre como proceder.
data.isnull().sum()


# In[6]:


# Otra opcion es calcular el porcentaje que siempre es mas representativo.
data.isnull().sum()/len(data.index)


# In[7]:


# La primera opcion es borrar todas las filas que contengan algun dato perdido.
# Esta es la opcion mneos adeccuada ya que supone una importante perdida de infomacion
# Una vez eliminados los visualizamos los datos
datoscomp=data.dropna()
print(datoscomp)


# In[8]:


# Con esta funcion nos vemos si existen (TRUE) o no (FALSE) datos perdidos
datoscomp.isnull().any().any()


# In[9]:


# Una opcion es eliminar los datos pero esto nos lleva a perder informacion y puede ser informacion relevante.
# Existen varias opciones para imputar los datos.
# Volvemos a cargar los datos originales.
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[10]:


# Me aseguro de que haya valores perdidos
data.isnull().any().any()


# In[11]:


# El metodo de imputacion mas sencillo es la media 
data=data.fillna(data.mean())


# In[12]:


# Pocedemos a comprobar que no existen valores perdidos
data.isnull().any().any()


# In[13]:


# Volvemos a cargar los datos
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[14]:


# Comprobamos que hay valores perdidos nuevamente
data.isnull().any().any()


# In[15]:


# Otra forma de imputar la media es la siguiente

import pandas as pd
import numpy as np
import sklearn.preprocessing as sk

# Seleccionamos los datos numericos.

datoNum=data.iloc[:,1:8]
fecha=data.iloc[:,0]


imp=sk.Imputer(missing_values="NaN", strategy="mean", axis=0, verbose=0, copy=False)
imp=imp.fit(datoNum)
imputed_data=imp.transform(datoNum.values)

datos_completos= pd.concat([fecha, datoNum], axis=1)





# In[16]:


datos_completos


# In[17]:


# Nos aseguramos de que no haya valores perdidos.
datos_completos.isnull().any().any()


# In[18]:


# Volvemos a cargar los datos
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[19]:


# Otra opcion es imputar la mediana

import pandas as pd
import numpy as np
import sklearn.preprocessing as sk

# Seleccionamos los datos numericos.

datoNum=data.iloc[:,1:8]
fecha=data.iloc[:,0]

from sklearn.preprocessing import Imputer
imp=sk.Imputer(missing_values="NaN", strategy="median", axis=0, verbose=0, copy=False)
imp=imp.fit(datoNum)
imputed_data=imp.transform(datoNum.values)

datos_completos= pd.concat([fecha, datoNum], axis=1)


# In[20]:


# Nos aseguramos de que no haya valores perdidos.
datos_completos.isnull().any().any()


# In[21]:


# Volvemos a cargar los datos
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[22]:


# La ultima opcion dentro de la imputacion por valores fijos es la moda o valor mas frecuente.
# Esto se usa especialmete para variables categoricas.

import pandas as pd
import numpy as np
import sklearn.preprocessing as sk

# Seleccionamos los datos numericos.

datoNum=data.iloc[:,1:8]
fecha=data.iloc[:,0]

from sklearn.preprocessing import Imputer
imp=sk.Imputer(missing_values="NaN", strategy="most_frequent", axis=0, verbose=0, copy=False)
imp=imp.fit(datoNum)
imputed_data=imp.transform(datoNum.values)

datos_completos= pd.concat([fecha, datoNum], axis=1)


# In[23]:


# Nos aseguramos de que no haya valores perdidos.
datos_completos.isnull().any().any()


# In[24]:


# Estos son las formas que existen para estimar los valores perdidos basandonos en valores estadisticos.
# En ocasiones es mas acertado utilizar otros metodos, especialmente si las variables estan relacionadas entre si.
# Volvemos a cargar los datos.
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[25]:


# Al tratarse de una serie temporal se puede sustituir por el valor anterior de dicha serie

data1=data.fillna(method='bfill')


# In[26]:


datos_completos.isnull().any().any()


# In[27]:


# Tal y como hemos hecho en cada ejemplo volvemos a cargar los datos originales
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_1.csv")


# In[28]:


# Para este caso necesitamos saber el tipo de dato que hay en cada columna.
data.dtypes


# In[29]:


# Otre opcion es realizar una imputacion multiple.
# Este procedimiento es adecuado cuando las variables explicativas estan relacionadas entre si.
# Previamente realizaremos una matriz de correlacion.
data.corr()


# In[ ]:


# Se puede observar que existe cierta correlacion entre las variables dependientes.
# Esto es un indicador de que puede ser adecuado utilizar metodos de imputacion multiple.
# Hasta ahora hemos seàparado las columnas manualmente ya que estamos trabajando con pocos datos.
# Con grandes bases de datos en los que se entremezclen datos numericos con otro tipo de datos puede generar problemas.
# Por ello podemos separarlos en funcion de su tipologia.

# En caso de que genere problemas ir a anaconda Promt y escribir
# 1- conda install ecos  
# 2- conda install CVXcanon  
# 3- pip install fancyimpute  

# En caso de que siga generando problemas analizar las dependencias adicionales exigidas, en mi caso fue ipykernel
# pip install ipukernel
# y despues: pip install fancyinpute

import pandas as pd
import numpy as np


datoNum=data.select_dtypes(include=[np.float]).as_matrix()
fecha=data.select_dtypes(include=[np.object]).as_matrix()

datoNum=pd.DataFrame(datoNum)
fecha=pd.DataFrame(fecha)

import fancyimpute 
datoNumcomp=pd.DataFrame(fancyimpute.MICE().complete(datoNum))

datos_completos= pd.concat([fecha, datoNumcomp], axis=1)

datos_completos.columns=data.columns
datos_completos.index=data.index

datos_completos


# In[ ]:


datos_completos.isnull().any().any()


# In[ ]:




