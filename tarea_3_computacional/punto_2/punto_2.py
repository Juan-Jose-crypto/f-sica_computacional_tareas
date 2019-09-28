import matplotlib.pyplot as plt #Importar módulo matplotlib;
import numpy as np #importar módulo numpy;
import time #importar módulo time;

#extracción de información en datos.dat;
with open("datos.dat","r") as f:
    files=f.read() #lectura de información;

list_file=[i for i in files if i is not "\n"] #eliminación de saltos de línea;

document=" " #creación de string document vacío;

for i in list_file:
    document+=i #concatenación de strings;

document=document.split(" ")#creación de lista document;

new_file=[float(i) for i in document if i is not ''] #eliminación de espacios;

t=[] #creación de contenedor vacío para datos de tiempo;
f=[] #creación de contenedor vacío para datos de la función;

for i in range(len(new_file)):
    if i%2==0:
        t.append(new_file[i]) #almacenar en t si la posición es par;
    else:
        f.append(new_file[i]) #almacenar en f si la posición es impar;

#print(t[0]) <---- se halla el primer valor de la lista t que es t=-5.0


'''
Este código es usado para preguntar si todos los datos
están igualmente espaciados:

dt=t[1]-t[0] #distancia entre el primer elemento de la lista t y el siguiente;

boolean=True #Booleano cuyo valor es verdadero;

for i in range(len(t)):
    if i==len(t)-1:
        pass #ignorar el último punto;
    else:
        boolean=boolean and (t[i+1]-t[i]==dt) #se compara cada slice en tamaño;

print(boolean) #resultado final: boolean=True;
'''

#valores de tiempo (t);
N=len(t) #número de puntos;
n=len(t)-1 #número de slices;
T=t[len(t)-1]-t[0] #periodo de la señal de la gráfica f(t) vs t;
dt_prim=T/n #valor del intervalo dt (infinitésimo) de tiempo;
t_prim=np.linspace(0,n,N)*dt_prim #valores de t usados para gráficar f(t) vs t;

'''
El efecto es el de correr la gráfica de tal manera que el primer extremo
esté en 0 y el segundo extremo se encuentre en T. Lo anterior es equivalente
a realizar la siguiente transformación:

t'=t+5.00;
'''

#valores de la frecuencia angular omega (w);
nu=1/T #valor de la frecuencia;
omega=2*np.pi*nu #valor de omega o frecuencia angular;
dw=omega/n #valor del intervalo dw (infinitésimo) de frecuencia angular;
'''
se quiere que el arreglo de numpy w tenga el mismo número de
slices que t;
'''
w=np.linspace(0,n,N)*dw #valores de w usados para gráficar g(w) vs w;

g_total=[] #creación de contenedor (lista vacía) para la IDFT;

initial_time=time.time() #cronometro que arranca en tiempo t=0s;
for n in range(N):
    Int=0 #contador de la integral en 0;
    for m in range(N):
        Int+=(1/np.sqrt(N))*f[m]*np.exp(-1j*(2*np.pi*m*n/N)) #DFT
    g_total.append(Int) #agregar la lista g_total;
    
final_time=time.time() #el cronometro se para en el tiempo final;
total_time=final_time-initial_time #medición del tiempo total gastado;
print("El tiempo total gastado en hacer DFT fue de:",end=" ")
print(total_time,end=' ') #<---- tiempo que tarda
print("segundos")

g_real=[i.real for i in g_total] #parte real;
g_img=[i.imag for i in g_total] #parte imaginaria;

fig, axs=plt.subplots(2,2) #objeto subplots;

axs[0,0].plot(t,f,color="yellow") #gráfica de f vs t;
axs[0,0].set_xlabel("Tiempo $t$")
axs[0,0].set_ylabel("$f(t)$")

axs[0,1].plot(t_prim,f,color="green") #gráfica de f vs t';
axs[0,1].set_xlabel("Tiempo $t'$")
axs[0,1].set_ylabel("$f(t')$")

axs[1,0].plot(w,g_real,color="red") #gráfica de g_real vs w;
axs[1,0].set_xlabel("Frecuencia angular $\omega$")
axs[1,0].set_ylabel("Re$[g(\omega)]$")

axs[1,1].plot(w,g_img,color="orange") #gráfica de g_img vs w;
axs[1,1].set_ylabel("Im$[g(\omega)]$")
axs[1,1].set_xlabel("Frecuencia angular $\omega$")

plt.show() #mostrar gráficos del entorno fig.
