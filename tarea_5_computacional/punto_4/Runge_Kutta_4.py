import numpy as np #importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib;

N=10**3 #número de puntos de la gráfica;
x=np.linspace(0,1,N) #intervalo espacial;
dx=x[1]-x[0] #distancia entre puntos adyacentes;
y_1_0=0 #u(0)=0 siendo y_1=u;
y_1_1=1 #u(1)=1;
a=0 #límite inferior de intervalo de inspección;
b=10 #límite superior de intervalo de inspección;
y_2_0=np.linspace(a,b,N) #posibles valores de y_2_0;
h=y_2_0[1]-y_2_0[0] #distancia entre puntos del intervalo de posibles y_2_0;
f_alpha=[] #contenedor vacío de valores de la función f_alpha;
tol=pow(10,-20) #valor de la tolerancia;

for j in y_2_0: #bucle for para cada valor de y_2_0;
    y_0=np.array([y_1_0,j]) #vector y_0 con valores iniciales;
    y=[] #contenedor vacío del vector y;
    y.append(y_0) #agregar valores iniciales;

    #método Runge-Kutta de orde 4;
    for i in range(len(x)):
        g_k1=np.array([y[i][1],-(np.pi**2/4)*(y[i][0]+1)])
        k_1=dx*g_k1
        y_k2=y[i]+(1/2)*k_1
        g_k2=np.array([y_k2[1],-(np.pi**2/4)*(y_k2[0]+1)])
        k_2=dx*g_k2
        y_k3=y[i]+(1/2)*k_2
        g_k3=np.array([y_k3[1],-(np.pi**2/4)*(y_k3[0]+1)])
        k_3=dx*g_k3
        y_k4=y[i]+k_3
        g_k4=np.array([y_k4[1],-(np.pi**2/4)*(y_k4[0]+1)])
        k_4=dx*g_k4
        y.append(y[i]+(1/6)*(k_1+2*k_2+2*k_3+k_4))

    y_1=[] #contenedor vacío para los valores de y_1;
    y_2=[] #contenedor vacío para los valores de y_2;

    for i in range(len(x)): #bucle for para guardar valores de y_1 y y_2;
        y_1.append(y[i][0]) #guardar en y_1;
        y_2.append(y[i][1]) #guardar en y_2;
    
    f_alpha.append(y_1[len(y_1)-1]-y_1_1) #guardar en la lista f_alpha;

#encontrar los ceros de la función f_alpha;
roots=[] #contenedor vacío para las raíces del gráfico;
for i in range(len(y_2_0)): #recorrer todos los índices en t;
    dt=h #dt como h;
    if i==len(y_2_0)-1: #si i es el último índice;
        pass #ignorar;
    else:
        if f_alpha[i]*f_alpha[i+1]<=0: #condición de existencia de una raíz;
            if i==0:
                roots.append("Inferior") #control de raíces;
            elif i==len(y_2_0)-2:
                roots.append("Superior") #control de raíces;
                #el control de raíces avisa si hay raíz en los extremos;
            else:
                t_0=y_2_0[i-1] #primer dato en t;
                t_1=y_2_0[i] #segundo dato en t;
                t_2=y_2_0[i+1] #tercer dato en t;
                t_3=y_2_0[i+2] #cuarto dato en t;
                f_0=f_alpha[i-1] #valor de la función en t_0;
                f_1=f_alpha[i] #valor de la función en t_1;
                f_2=f_alpha[i+1] #valor de la función en t_2;
                f_3=f_alpha[i+2] #valor de la función en t_3;
                z_0=t_1 #guardar dato t_1 en variable z_0;
                z_1=t_2 #guardar dato t_2 en variable z_1;
                def f(a):
                    #interpolación de Lagrange de orden 3 para datos en x;
                    function=((a-t_1)/(t_0-t_1))*((a-t_2)/(t_0-t_2))*((a-t_3)/(t_0-t_3))*f_0+((a-t_0)/(t_1-t_0))*((a-t_2)/(t_1-t_2))*((a-t_3)/(t_1-t_3))*f_1+((a-t_0)/(t_2-t_0))*((a-t_1)/(t_2-t_1))*((a-t_3)/(t_2-t_3))*f_2+((a-t_0)/(t_3-t_0))*((a-t_1)/(t_3-t_1))*((a-t_2)/(t_3-t_2))*f_3
                    return(function)
                while dt>tol: #método de la Secante (primer punto del taller);
                    z_2=z_1-((z_1-z_0)/(f(z_1)-f(z_0)))*f(z_1)
                    dt=z_2-z_1
                    z_0=z_1
                    z_1=z_2
                    if dt<tol:
                        roots.append(z_1)

y_2_0=roots[0] #y_2_0 se iguala al valor de la raíz hallada;
y_0=np.array([y_1_0,y_2_0]) #vector y_0 con valores iniciales;
y=[] #contenedor vacío del vector y;
y.append(y_0) #agregar valores iniciales;

sol=-1+np.cos((np.pi*x)/2)+2*np.sin((np.pi*x)/2) #solución analítica al problema;

#repetición del bucle for de método Runge-Kutta de orden 4;
for i in range(len(x)):
    g_k1=np.array([y[i][1],-(np.pi**2/4)*(y[i][0]+1)])
    k_1=dx*g_k1
    y_k2=y[i]+(1/2)*k_1
    g_k2=np.array([y_k2[1],-(np.pi**2/4)*(y_k2[0]+1)])
    k_2=dx*g_k2
    y_k3=y[i]+(1/2)*k_2
    g_k3=np.array([y_k3[1],-(np.pi**2/4)*(y_k3[0]+1)])
    k_3=dx*g_k3
    y_k4=y[i]+k_3
    g_k4=np.array([y_k4[1],-(np.pi**2/4)*(y_k4[0]+1)])
    k_4=dx*g_k4
    y.append(y[i]+(1/6)*(k_1+2*k_2+2*k_3+k_4))

y_1=[] #y_1 volverá a ser un contenedor vacío;
y_2=[] #y_2 volverá a ser un contenedor vacío;

for i in range(len(x)): #bucle for para guardar valores de y_1 y y_2;
    y_1.append(y[i][0])
    y_2.append(y[i][1])

Error=0 #inicialización del error en 0;
for i in range(len(y_1)):
    if i==0:
        pass
    else:
        Error+=(1/(len(sol)-1))*abs(1-(y_1[i]/sol[i])) #error relativo promedio;

print("El error relativo promedio del método Runge-Kutta de orden 4 es:",end=" ")
print(Error)

#gráficar resultado final;
plt.plot(x,y_1,'*',color='red',label='$u^{numeric}(x)$')
plt.plot(x,sol,color='blue',label='$u^{analitic}(x)$')
plt.legend()
plt.grid(True)
plt.xlabel('Distancia en $x$')
plt.ylabel('$u(x)$')
plt.show()
