import numpy as np #Importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib

#preámbulo (inicio);
print("INSTRUCCIONES")
A="El siguiente programa permite hallar las raíces de la función propuesta"
adorno_1="="*len(A)
print(adorno_1)
print(A)
print("en el taller. Solo necesita dos datos de entrada para poder solucionar")
print("el problema mediante el método de Newton-raphson. Es necesario saber cual")
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

#datos de entrada;
tol=pow(10,-10) #tolerancia;
a=float(input("Introduzca el límite inferior a del intervalo de inspección: "))
b=float(input("Introduzca el límite superior b del intervalo de inspección: "))
N=10**3 #número de puntos;
x=np.linspace(a,b,N) #generación del intervalo [a,b];
h=x[1]-x[0] #distancia entre los puntos del intervalo [a,b];

f=np.exp(-x**2)*(2*x+1)*np.cos(5*x) #función como arreglo de numpy;

#derivada analítica de la función como arreglo de numpy;
f_prim=2*np.exp(-x**2)*np.cos(5*x)-2*np.exp(-x**2)*x*(1+2*x)*np.cos(5*x)-5*np.exp(-x**2)*(1+2*x)*np.sin(5*x)

#cambio de paradigma de estructural a funcional;
def g(x):
    f=np.exp(-x**2)*(2*x+1)*np.cos(5*x) #función f(x);
    return(f)

def g_prim(x):
    #función primera derivada de f(x);
    f_prim=2*np.exp(-x**2)*np.cos(5*x)-2*np.exp(-x**2)*x*(1+2*x)*np.cos(5*x)-5*np.exp(-x**2)*(1+2*x)*np.sin(5*x)
    return(f_prim)

roots=[] #contenedor vacío para las raíces de la función;
for i in range(len(x)): #explorar cada indice en x;
    dx=h #dx igual a h;
    x_0=x[i] #dato inicial;
    if i==len(x)-1: #si i es el último índice;
        pass #ignorar;
    else:
        if f[i]*f[i+1]<=0: #revisar la condición en el intervalo [x[i],x[i+1]];
            while dx>tol:
                x_1=x_0-(g(x_0)/g_prim(x_0)) #Newton-Raphson;
                dx=x_1-x_0 #cambio de valor de dx;
                x_0=x_1 #cambio de x_0 como x_1
                if dx<tol: #condición de guardado;
                    roots.append(x_0) #guardar la raíz en roots;
            

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
