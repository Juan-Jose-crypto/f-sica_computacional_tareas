import numpy as np #Importar módulo numpy;
import matplotlib.pyplot as plt #Importar módulo matplotlib

#datos de entrada;

#preámbulo (inicio);
print("INSTRUCCIONES")
A="El siguiente programa permite hallar las raíces de la función propuesta"
adorno_1="="*len(A)
print(adorno_1)
print(A)
print("en el taller. Solo necesita dos datos de entrada para poder solucionar")
print("el problema mediante el método de la Bisección. Es necesario saber cual")
print("es el intervalo I=[a,b] en el que se quiere saber si existe o no ceros.")
B="Dependiendo del intervalo el programa dirá cuantos ceros hay y sus res-"
print(B)
print("pectivos valores.")
print(" ")
print("Finalmente, el  programa hará un plot f(x), f'(x) vs t con el cual se")
print("puede verificar si se quiere el resultado obtenido en el programa.")
adorno_2="="*len(B)
print(adorno_2)
#preámbulo (Final);


tol=pow(10,-15) #tolerancia;
a=float(input("Introduzca el límite inferior a del intervalo de inspección: "))
b=float(input("Introduzca el límite superior b del intervalo de inspección: "))
N=10**3 #número de puntos;
x=np.linspace(a,b,N) #generación del intervalo [a,b];
h=x[1]-x[0] #distancia entre los puntos del intervalo [a,b];
shift=tol+1 #variable "corrimiento";

f=np.exp(-x**2)*(2*x+1)*np.cos(5*x) #función como arreglo de numpy;

#derivada analítica de la función;
f_prim=2*np.exp(-x**2)*np.cos(5*x)-2*np.exp(-x**2)*x*(1+2*x)*np.cos(5*x)-5*np.exp(-x**2)*(1+2*x)*np.sin(5*x)

roots=[] #contenedor vacío para las raíces de la función;
for i in range(len(x)): #explorar cada indice en x;
    dx=h #dx igual a la distancia entre puntos en x;
    if i==len(x)-1: #si i es el último índice;
        pass #ignorar;
    else:
        if f[i]*f[i+1]<=0: #revisar la condición en el intervalo[x[i],x[i+1]];
                x_0=x[i] #primera variable;
                x_1=x[i+1] #segunda variable;
                #cambio de paradigma a funcional;
                def g_int(x):
                    f=np.exp(-x**2)*(2*x+1)*np.cos(5*x) #función matemática;
                    return(f) #retornar a f;
                #bucle while con algoritmo de bisección;
                while dx>tol:
                    if g_int(x_0)*g_int(x_1)<=0: #condición de existencia de raíz;
                        x_m=(x_0+x_1)/2 #hallar punto medio;
                        if g_int(x_0)*g_int(x_m)<=0: #condición de existencia de raíz;
                            x_1=x_m #x_1 guarda el dato x_m
                            dx=abs(x_1-x_0) #distancia entre x_1 y x_0
                            if dx<tol: 
                                roots.append(x_m) #guardar la raíz en roots;
                        else:
                            x_0=x_m #x_0 guarda el dato x_m
                            dx=abs(x_1-x_0) #distancia entre x_1 y x_0
                            if dx<tol:
                                roots.append(x_m) #guardar la raíz en roots;
                    else:
                        x_0=x_1 #x_0 guarda el dato x_1
                        x_1=x_1+shift #usar corrimiento;
root_number=len(roots) #número de raíces;
print("La función tiene %i raíces en el intervalo [%i,%i]."%(root_number,a,b))
print("Las raíces son las siguientes:")
for i in range(len(roots)):
    print("La raíz %d es: "%(i+1), roots[i]) #imprimir en pantalla las raíces;


#graficar la función y la primera derivada;
plt.plot(x,f,color="red",label="$f(x)$") #función;
plt.plot(x,f_prim,color="orange",label="$f'(x)$") #primera derivada;
plt.xlabel("$x$") #dar nombre al eje x;
plt.ylabel("$f(x)$,$f'(x)$") #dar nombre al eje y;
plt.legend() #que haya una leyenda que me diga de qué curva es la función o la derivada;
plt.title("$f(x)$ y $f'(x)$ en función $x$") #título;
plt.grid(True) #agregar grillas;
plt.show() #mostrar resultado en conjunto.
