#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[2]:


# Igual que en anteriores ocasiones tenemos que comprender nuestors datos.
print(data)


# In[3]:


data.head(n=10)


# In[4]:


data.describe()


# In[5]:


# Comprobamos que no hay valores perdidos.
data.isnull().sum()


# In[6]:


# El primer paso es realizar un "box-plot" para visualizar si existen outliers y como se distribuyen.

# Una de las opciones es analizar cada variable individualmente
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data=pd.DataFrame(data)

data1=data.iloc[:,0]

plt.boxplot(data1);



# In[7]:


# Tambien podemos realizar un grafico de todas las variables a la vez.
data.plot(kind='box');


# In[8]:


# El analisis grafico nos permite ver que existen outliers en todas las variables incluidas en el modelo.
# Una vez que hemos contatado que existen outliers.
# La primera opcion es eliminar las filas que contienen outliers en alguna de las variables.
import numpy as np
from scipy import stats
dataSinOut=data[(np.abs(stats.zscore(data)) <3).all(axis=1)]


# In[9]:


print(dataSinOut)


# In[10]:


dataSinOut.plot(kind='box');


# In[11]:


# Volvemos a cargar el dataset
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[12]:


# Otra forma de eliminar los datos en funcion del quantil es la siguiente.
# En este caso habria que hacerlo para cada una de las variables.
# Este procedimiento puede ser interesante si estamos interesados en descartar algun tipo de evento concreto
# Que se haya focalizado en alguna de las variables.
qB = data["G1"].quantile(0.15)
qA = data["G1"].quantile(0.85)
dataSinOut=data[(data["G1"] > qB) & (data["G1"] < qA)]

dataSinOut


# In[13]:


# Volvemos a realizar el grafico.
# Solo se han eliminado los outliers de la primera variable.
# SIn embargo observamos que han desaparecido los outliers para la mayoria de las observaciones.
dataSinOut.plot(kind='box');


# In[14]:


# Esto nos lleva a plantearnos que en los outliers se agrupan en las mismas observaciones.
# A continuacion mostramos aquellas observaciones en las que se encuentran los outliers.
# Para ello modificamos ligeramente el codigo anterior.


qB = data["G1"].quantile(0.15)
qA = data["G1"].quantile(0.85)
dataOut=data[(data["G1"] < qB) | (data["G1"] > qA)]
dataOut


# In[15]:


# En este caso observamos que tenemos muchos outliers.
# Realmente estamos mas interesado en saber que ocurre con los valores verdaderamente extremos.
# Por ello ajustamos mas los porcentajes para seleccionar aquellos valores en los que estamos interesados.

qB = data["G1"].quantile(0.01)
qA = data["G1"].quantile(0.99)
dataOut=data[(data["G1"] < qB) | (data["G1"] > qA)]
dataOut


# In[16]:


# Podemos observar que la observacion 38 agrupa valores muy extremos y que realmente resultan muy anomalos.
# Una observacion asi puede distorisionar un modelo.
# Por ello seria adecuado estudiar dicha variable por separado y excluirla del modelo.
# Sin embargo en el grafico anterior observamos que en la variable "G6" sigue existiendo un outlier que no hemos recogido.
# De cara a entender bien nuestros datos es conveniente saber que ocurre con esa observacion.
# Por ello repetimos el proceso.

qB6 = data["G6"].quantile(0.01)
qA6 = data["G6"].quantile(0.99)
dataOut6=data[(data["G6"] < qB6) | (data["G6"] > qA6)]
dataOut6


# In[17]:


# En este analisis vemos que en la observacion que nos acontece el resto de las variables toman valore que podemos calificar como normales


# In[18]:


# Volvemos a cargar los datos
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[19]:


# Tambien podemos utilizar la primera metodologia columna por columna.
from scipy import stats
data[(np.abs(stats.zscore(data["G1"])) < 3)]


# In[20]:


# En estos tres procedimientos hemos visto diferentes formas de eliminar los valores extremos.
# Existen otras muchas ocasiones en las que estos valores juegan un papel clave para el modelo.
# De hecho en algunos casos son mas importantes los valores extremos que los valores "normales".
# En estas ocasiones nos interesa crear una nueva variable que nos marque si una determinada observacion es un outlier o no.
# Ademas en estos casos nos puede interesar diferenciar si se trata de un outlier "por arriba" o "por abajo".

# Volvemos a cargar los datos.

import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[21]:


# Lo primero que tenemos que hacer es calcular los estadisticos basicos para la deteccion de outliers (media o mediana y desviacion tipica)
data.describe()


# In[22]:


# De los pasos anteriores hemos descubierto que la fila 38 presenta unos valores muy anomalos.
# Por ello la vamos a eliminar.
# Una forma de eliminarla es hacerlo manualmente.

data1=data.drop(data.index[38])
data1.head(n=40)


# In[23]:


# Esto es una opcion viable en el caso de que debamos eliminar pocas observaciones.
# Otra opcion es seleccionar una de las variables, ver a partir de que valor queremos eliminar la observacion y hacerlo a mano.
# Vuelvo a cargar los datos.

import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[24]:


data2=data[(data["G1"] < 5)]
print(data2)
data1.head(n=40)
           


# In[25]:


# Otra opcion es eliminar aquellas observaciones que sobrepasen una desviacion prefijada.
# Esto se puede aplicar sobre una de las variables o sobre todo el dataset.
# Aplicarlo sobre una determinada variable nos exige ser cuidadosos a la hora de fijar el limite para no eliminar demasiadas observaciones.
# Volvemos a cargar los datos.

import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[26]:


# Para ello utilizamos una formula que ya hemos visto con anterioridad modificada.
# Tras ello comprobamos que no hemos eliminado elementos que queriamos mantener y que hemos eliminado la fila 38.

from scipy import stats
data1=data[(np.abs(stats.zscore(data["G1"])) < 6)]

print(data1)
data1.head(n=40)


# In[27]:


# Otra opcion en vez de eliminar la observacion es transformarlos NAs
import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[28]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


# Una forma de ver en cada variable en que observacion se encuentran los outliers.
# Marca como outliers aquellas observaciones que difieran de la media mas de tres veces la desviacion tipica.

import numpy as np

def outliers_z_score(ys):
    threshold = 3

    mean_y = np.mean(ys)
    stdev_y = np.std(ys)
    z_scores = [(y - mean_y) / stdev_y for y in ys]
    return np.where(np.abs(z_scores) > threshold)

datos=data.apply(outliers_z_score)
datos


# In[30]:


# Otra forma de ver en cada variable en que observacion se encuentran los outliers.
#En este caso nos basamos en la desviacion desde la mediana.

import numpy as np

def outliers_modified_z_score(ys):
    threshold = 3.5

    median_y = np.median(ys)
    median_absolute_deviation_y = np.median([np.abs(y - median_y) for y in ys])
    modified_z_scores = [0.6745 * (y - median_y) / median_absolute_deviation_y
                         for y in ys]
    return np.where(np.abs(modified_z_scores) > threshold)

datos=data.apply(outliers_modified_z_score)
datos


# In[31]:


# Una forma de ver en cada variable en que observacion se encuentran los outliers.
# Se fundamenta en la diferencia para el percentil 25 y 75.

import numpy as np

def outliers_iqr(ys):
    quartile_1, quartile_3 = np.percentile(ys, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((ys > upper_bound) | (ys < lower_bound))

datos=data.apply(outliers_iqr)
datos


# In[32]:


# Para ello utilizamos una formula ya utilizada pero modificada, igual que antes.
# Realizamos la comprobacion de antes
# Mostramos la fila que nos interesa (un numero menos ya que se ha eliminado la fila 38)

from scipy import stats
import numpy as np
data1=data[(np.abs(stats.zscore(data)) <6).all(axis=1)]

print(data1)
print(data1.head(n=40))
print(data1.iloc[153,:])


# In[33]:


# Hasta ahora hamos visto como identificar los outliers de diferente maneras para eliminarlos, mediante diferentes metodos.
# A continuecion mostramos como identificar los outliear y como sustituirlos.

import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[34]:


# Mediante esta formula podemos sustituir los outliers por la media.

def replace(group):
    mean, std = group.mean(), group.std()
    outliers = (group - mean).abs() > 3*std
    group[outliers] = mean        
    return group


datos=data.apply(replace)

data.head(n=40)


# In[35]:


import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[36]:


# De esta manera podemos convertir los outliers en NAs y luego tratarlos como NAs.
# El trataiento de NAs lo hemos visto en el script anterior.

import numpy as np

def replace2(group):
    mean, std = group.mean(), group.std()
    outliers = (group - mean).abs() > 3*std
    group[outliers] = np.nan        
    return group


datos=data.apply(replace2)

data.head(n=40)


# In[37]:


# Volvemos a cargar los datos.
# En este caso vamos a crear una variable outlier alto y otra bajo para cada variable original.

import os
import pandas as pd
os.chdir(r"C:\Users\ALUMNO\Downloads\Curso-Bilbao-C2B\5-Quality")
data = pd.read_csv("Ejemplo_3.csv")


# In[38]:


# Calculamos el valor que nos interesa.
# Creamos las nuevas columnas.

q1B = data["G1"].quantile(0.15)
q1A = data["G1"].quantile(0.85)

data2.loc[:,"out1bajo"]=0
data2.loc[data1["G1"]<q1B,"out1bajo"]=1

data2.loc[:,"out1alto"]=0
data2.loc[data1["G1"]>q1A,"out1alto"]=1

data2


# In[39]:


# Repetimos esta misma operacion para la segunda variable.



q2B = data["G2"].quantile(0.15)
q2A = data["G2"].quantile(0.85)

data2.loc[:,"out2bajo"]=0
data2.loc[data1["G2"]<q1B,"out1bajo"]=1

data2.loc[:,"out2alto"]=0
data2.loc[data1["G2"]>q1A,"out2alto"]=1

data2


# In[40]:


# De esta forma vemos si debido a los valores extremos se produce un "salto" en el valor.
# Tambien puede ocurrir que en estos valores se produzca un cambio en la pendiente.
# Para incluir esto hay que incluir una variable multicativa.



data2["out1bajomulti"]=data2["G1"]*data2["out1bajo"]
data2["out1altomulti"]=data2["G1"]*data2["out1alto"]

data2["out2bajomulti"]=data2["G2"]*data2["out2bajo"]
data2["out2altomulti"]=data2["G2"]*data2["out2alto"]

data2

