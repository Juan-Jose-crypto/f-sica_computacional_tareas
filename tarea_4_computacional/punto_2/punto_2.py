import numpy as np #Importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib;

print("INSTRUCCIONES")
A="El siguiente programa permite hallar los extremos de la función propuesta"
adorno_1="="*len(A)
print(adorno_1)
print(A)
print("en el taller. Solo necesita dos datos de entrada para poder solucionar")
print("el problema mediante el método de la Bisección. Es necesario saber cual")
print("es el intervalo I=[a,b] en el que se quiere saber si existe o no extremos.")
B="Dependiendo del intervalo el programa dirá cuantos extremos hay y sus res-"
print(B)
print("pectivos valores, además de si es un mínimo o un máximo en forma de una")
print("Tupla. Por ejemplo: (x,máximo) dice que en x hay un máximo.")
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

ext=[] #contenedor vacío para los extremos de la función;
for i in range(len(x)): #explorar cada indice en x;
    dx=h #dx igual a h;
    if i==len(x)-1: #si i es el último índice;
        pass #ignorar;
    else:
        x_0=x[i] #dato inicial;
        x_1=x[i+1] #dato siguiente;
        if f_prim[i]*f_prim[i+1]<=0: #revisar la condición en el intervalo [x[i],x[i+1]];
                while dx>tol:
                    x_2=x_1-((x_1-x_0)/(g(x_1)-g(x_0)))*g(x_1) #Secante
                    dx=x_2-x_1 #cambio de valor de dx;
                    x_0=x_1 #cambio de x_0 como x_1
                    x_1=x_2 #cambio de x_1 como x_2
                    if dx<tol:
                        if g(x_1)-g(x_1+h)<0: #condición de guardado;
                            #esto es verdad porque la función es suave;
                            ext.append((x_1,"mínimo")) #tupla con dato y la etiqueta mínimo;
                        else:
                            ext.append((x_1,"máximo")) #tupla con dato y la etiqueta máximo;
                
extreme_number=len(ext) #número de raíces;
print("La función tiene %i extremos en el intervalo [%i,%i]."%(extreme_number,a,b))
print("Los extremos son los siguientes:")
for i in range(len(ext)):
    print("El extremo %d es: "%(i+1), ext[i]) #imprimir en pantalla las raíces;

#graficar la función y la primera derivada;
plt.plot(x,f,color="red",label="$f(x)$") #función;
plt.plot(x,f_prim,color="orange",label="$f'(x)$") #primera derivada;
plt.xlabel("$x$") #dar nombre al eje x;
plt.ylabel("$f(x)$,$f'(x)$") #dar nombre al eje y;
plt.legend() #que haya una leyenda que me diga de qué curva es la función o la derivada;
plt.title("$f(x)$ y $f'(x)$ en función $x$") #título;
plt.grid(True) #agregar grillas;
plt.show() #mostrar resultado en conjunto.
