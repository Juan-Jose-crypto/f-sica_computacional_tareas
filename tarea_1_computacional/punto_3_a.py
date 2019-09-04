import numpy as np #Importación del módulo numpy y asignación del nickname np;
import pandas as pd #importación del módulo pandas y asignación del nickname pd;

#se pide por pantalla el número de intervalos y se almacena en la variable N;
N=int(input("Inserte el número de intervalos de división a trabajar: "))

x=np.linspace(-np.pi,np.pi,N+1) #creación del intervalo con N+1 puntos;
h=(2*np.pi)/N #definición de h;

#función f(x);
f=np.exp(x)*np.cos(4*x)
#explicación: arreglo de numpy cuyos elementos son la función f(x) evaluada en cada elemento de x;

#segunda derivada de f(x) analítica;
f_prim_2=-15*np.exp(x)*np.cos(4*x)-8*np.exp(x)*np.sin(4*x)
#Explicación: arreglo de numpy cuyo elementos son la segunda derivada de f(x) evaluada en cada elemento de x;

f=[i for i in f] #transformación de arreglo de numpy f a lista;
f_prim_2=[i for i in f_prim_2] #transformación de arreglo de numpy f_prim_2 a lista;
x=[i for i in x] #transformación de arreglo de numpy x a lista;

f_prim_2.pop(0) #eliminación del primer punto de la segunda derivada analítica;
f_prim_2.pop(len(f_prim_2)-1) #eliminación del último punto de la segunda derivada analítica;

#creación de listas vacías;
f_2_3=[] #almacén de la segunda derivada usando tres puntos;
f_2_5=[] #almacén de la segunda derivada usando cinco puntos;

#derivada númerica de segundo orden usando 3 puntos;
for i in range(len(f)):
    if i==0 or i==len(f)-1:
        #se pasa automáticamente al siguiente índice (se omiten estos pasos);
        pass 
    else:
        #derivada númerica de segundo orden con 3 puntos;
        f_2_3.append((f[i+1]-2*f[i]+f[i-1])/h**2) 

#derivada númerica de segundo orden usando 5 puntos;
for i in range(len(f)):
    if i==0 or i==len(f)-1:
        pass 
    elif i==1 or i==len(f)-2:
        #derivada númerica de segundo orden con 3 puntos;
        f_2_5.append((f[i+1]-2*f[i]+f[i-1])/h**2)
    else:
        #derivada númerica de segundo orden con 5 puntos;
        f_2_5.append(((-f[i-2]+16*f[i-1]-30*f[i]+16*f[i+1]-f[i+2])/(12*h**2)))
        
x.pop(0) #eliminación del primer elemento de x;
x.pop(len(x)-1) #eliminación del último elemento de x;

#importación de datos a archivo csv;        
datos={"x":x, "ddf(3)":f_2_3, "ddf(5)":f_2_5, "ddf(analitic)":f_prim_2 } #creación de diccionario datos.

df=pd.DataFrame(datos) #creación de un dataframe para almacenar datos;

df.to_csv("datos_derivada_2_numerica.csv") #conversión de dataframe a archivo csv con nombre entre comillas;
#el archivo de texto se guardará dentro de la carpeta actual del archivo .py;

#lectura de datos en arcivo csv;
df=pd.read_csv("datos_derivada_2_numerica.csv", header=None, skiprows=1, names=["Número", "x", "ddf(3)",
                                                                              "ddf(5)", "ddf(analitic)"])
#número indica el número de datos y la posición del dato dentro del archivo;
#x indica el dato de posición;
#ddf(3) indica el dato de la segunda derivada númerica con tres puntos;
#ddf(5) indica el dato de la segunda derivada númerica con cinco puntos;
#ddf(analitic) indica el dato de la segunda derivada analítica; 

print(df) #visualización de los datos.
