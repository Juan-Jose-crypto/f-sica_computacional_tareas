import numpy as np #importación del módulo numpy y asignación del nickname np;
import pandas as pd #importación del módulo pandas y asignación del nickname pd;

#se pide por pantalla el número de intervalos y se almacena en la variable N;
N=int(input("Inserte el número de intervalos de división a trabajar: "))

x=np.linspace(-np.pi,np.pi,N+1) #creación del intervalo con N+1 puntos;
h=(2*np.pi)/N #definición de h;

#función f(x);
f=np.exp(x)*np.cos(4*x)
#explicación: arreglo de numpy cuyos elementos son la función f(x) evaluada en cada elemento de x;

#derivada de f(x) analítica;
f_prim=np.exp(x)*np.cos(4*x)-4*np.exp(x)*np.sin(4*x)
#Explicación: arreglo de numpy cuyo elementos son la derivada de f(x) evaluada en cada elemento de x;

f=[i for i in f] #transformación de arreglo de numpy f a lista;
f_prim=[i for i in f_prim] #transformación de arreglo de numpy f_prim a lista;

#creación de listas vacías;
f_1_2=[] #almacén de primera derivada usando dos puntos;
f_1_3=[] #almacén de primera derivada usando tres puntos;
f_1_5=[] #almacén de primera derivada usando cinco puntos;

#derivada númerica de primer orden usando 2 puntos (los índices de las listas o arreglos inician desde cero);
for i in range(len(f)):
    if i==len(f)-1:
        f_1_2.append((f[i]-f[i-1])/h) #derivada para el último punto;
    else:
        f_1_2.append((f[i+1]-f[i])/h) #derivada para el resto de puntos;

#derivada númerica de primer orden usando 3 puntos;
for i in range(len(f)):
    if i==len(f)-1:
        f_1_3.append((f[i]-f[i-1])/h) #derivada para el último punto;
        
    elif i==0:
        f_1_3.append((f[i+1]-f[i])/h) #derivada para el primer punto;
    else:
        f_1_3.append((f[i+1]-f[i-1])/(2*h)) #derivada para el resto de puntos;

#derivada númerica de primer orden usando 5 puntos;
for i in range(len(f)):
    if i==len(f)-1:
        f_1_5.append((f[i]-f[i-1])/h) #derivada para el último punto;
        
    elif i==0:
        f_1_5.append((f[i+1]-f[i])/h) #derivada para el primer punto;
        
    elif i==1 or i==len(f)-2:
        f_1_5.append((f[i+1]-f[i-1])/(2*h)) #derivada para el segundo y penúltimo punto;
        
    else:
        f_1_5.append((1/(12*h))*(f[i-2]-8*f[i-1]+8*f[i+1]-f[i+2])) #derivada para el resto de puntos;


#importación de datos a archivo csv;        
datos={"x":x, "df(2)":f_1_2, "df(3)":f_1_3, "df(5)":f_1_5 ,"df(analitic)":f_prim } #creación de diccionario datos.

df=pd.DataFrame(datos) #creación de un dataframe para almacenar datos;

df.to_csv("datos_derivada_numerica.csv") #conversión de dataframe a archivo csv con nombre entre comillas;
#el archivo de texto se guardará dentro de la carpeta actual del archivo .py;

#lectura de datos en arcivo csv;
df=pd.read_csv("datos_derivada_numerica.csv", header=None, skiprows=1, names=["Número", "x", "df(2)",
                                                                              "df(3)", "df(5)", "df(analitic)"])
#número indica el número de datos y la posición del dato dentro del archivo;
#x indica el dato de posición;
#df(2) indica el dato de la derivada númerica con dos puntos;
#df(3) indica el dato de la derivada númerica con tres puntos;
#df(5) indica el dato de la derivada númerica con cinco puntos;
#df(analitic) indica el dato de la derivada analítica;


print(df) #visualización de los datos.
