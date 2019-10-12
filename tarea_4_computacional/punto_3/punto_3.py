import numpy as np #Importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib

with open("datos.dat","r") as f: #abrir archivo;
    file=f.read() #leer archivo;

archivo=[i for i in file if i is not '\n'] #transformar información en elementos de la lista;
archivo=archivo[17:] #hacer un slice desde el elemento 17 hasta el final;
files=" " #variable string vacío;

for i in archivo: #recorrer todos los elementos de archivo;
    files+=i#concatenar;

archivo=files.split(" ") #crear lista archivo con elementos de files;

file=[float(i) for i in archivo if i is not ''] #quitar espacios y transformar los elementos de archivo a flotantes;

t=[] #contenedor o lista vacía t;
x=[] #contenedor o lista vacía x;

for i in range(len(file)): #recorrer todos los índices de file;
    if i%2==0:
        t.append(file[i]) #los elementos con posición par se guardan en t;
    else:
        x.append(file[i]) #los elementos con posición impar se guardan en x;


N=len(t) #número de puntos de la función;
n=N-1 #número de subintervalos;
h=t[1]-t[0] #distancia entre los valores de t;
tol=pow(10,-20) #valor de la tolerancia;
x_prim=[] #contenedor vacío de la función derivada;


#Derivada de 5 puntos;
for i in range(len(x)):
    if i==len(x)-1:
        x_prim.append((x[i]-x[i-1])/h) #derivada para el último punto;
        
    elif i==0:
        x_prim.append((x[i+1]-x[i])/h) #derivada para el primer punto;
        
    elif i==1 or i==len(x)-2:
        x_prim.append((x[i+1]-x[i-1])/(2*h)) #derivada para el segundo y penúltimo punto;
        
    else:
        x_prim.append((1/(12*h))*(x[i-2]-8*x[i-1]+8*x[i+1]-x[i+2])) #derivada para el resto de puntos;

#encontrar los ceros de la función;
roots=[] #contenedor vacío para las raíces del gráfico;
for i in range(len(t)): #recorrer todos los índices en t;
    dt=h #dt como h;
    if i==len(t)-1: #si i es el último índice;
        pass #ignorar;
    else:
        if x[i]*x[i+1]<=0: #condición de existencia de una raíz;
            if i==0:
                roots.append("Inferior") #control de raíces;
            elif i==len(t)-2:
                roots.append("Superior") #control de raíces;
                #el control de raíces avisa si hay raíz en los extremos;
            else:
                t_0=t[i-1] #primer dato en t;
                t_1=t[i] #segundo dato en t;
                t_2=t[i+1] #tercer dato en t;
                t_3=t[i+2] #cuarto dato en t;
                f_0=x[i-1] #valor de la función en t_0;
                f_1=x[i] #valor de la función en t_1;
                f_2=x[i+1] #valor de la función en t_2;
                f_3=x[i+2] #valor de la función en t_3;
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


root_number=len(roots) #número de raíces;
print("La función tiene %i raíces."%root_number)
print("Las raíces son las siguientes:")
for i in range(len(roots)):
    print("La raíz %d es: "%(i+1), roots[i]) #imprimir resultados de las raices;

#calcular los extremos de la función;
ext=[] #contenedor vacío para los extremos del gráfico;
for i in range(len(t)):
    dt=h #dt como h;
    if i==len(t)-1: #si i es el último índice;
        pass #ignorar;
    else:
        if x_prim[i]*x_prim[i+1]<=0: #condición de existencia de una raíz;
            if i==0:
                roots.append("Inferior") #control de extremos;
            elif i==len(t)-2:
                roots.append("Superior") #control de extremos;
                #el control de extremos avisa si hay extremos en los puntos inicial t[0] o t[final];
            else:
                t_0=t[i-1] #primer dato en t;
                t_1=t[i] #segundo dato en t;
                t_2=t[i+1] #tercer dato en t;
                t_3=t[i+2] #cuarto dato en t;
                f_0=x[i-1] #valor de la función en t_0;
                f_1=x[i] #valor de la función en t_1;
                f_2=x[i+1] #valor de la función en t_2;
                f_3=x[i+2] #valor de la función en t_3;
                f_prim_0=x_prim[i-1] #valor de la derivada en t_0;
                f_prim_1=x_prim[i] #valor de la derivada en t_1;
                f_prim_2=x_prim[i+1] #valor de la derivada en t_2;
                f_prim_3=x_prim[i+2] #valor de la derivada en t_3;
                z_0=t_1 #guardar dato t_1 en variable z_0;
                z_1=t_2 #guardar dato t_1 en variable z_0;
                def f(a):
                    #interpolación de Lagrange de orden 3 para datos en x;
                    function=((a-t_1)/(t_0-t_1))*((a-t_2)/(t_0-t_2))*((a-t_3)/(t_0-t_3))*f_0+((a-t_0)/(t_1-t_0))*((a-t_2)/(t_1-t_2))*((a-t_3)/(t_1-t_3))*f_1+((a-t_0)/(t_2-t_0))*((a-t_1)/(t_2-t_1))*((a-t_3)/(t_2-t_3))*f_2+((a-t_0)/(t_3-t_0))*((a-t_1)/(t_3-t_1))*((a-t_2)/(t_3-t_2))*f_3
                    return(function)
                def f_prim(a):
                    #interpolación de Lagrange de orden 3 para datos en x_prim;
                    function_prim=((a-t_1)/(t_0-t_1))*((a-t_2)/(t_0-t_2))*((a-t_3)/(t_0-t_3))*f_prim_0+((a-t_0)/(t_1-t_0))*((a-t_2)/(t_1-t_2))*((a-t_3)/(t_1-t_3))*f_prim_1+((a-t_0)/(t_2-t_0))*((a-t_1)/(t_2-t_1))*((a-t_3)/(t_2-t_3))*f_prim_2+((a-t_0)/(t_3-t_0))*((a-t_1)/(t_3-t_1))*((a-t_2)/(t_3-t_2))*f_prim_3
                    return(function_prim)
                while dt>tol: #método de la Secante (primer punto del taller);
                    z_2=z_1-((z_1-z_0)/(f_prim(z_1)-f_prim(z_0)))*f_prim(z_1)
                    dt=z_2-z_1
                    z_0=z_1
                    z_1=z_2
                    if dt<tol:
                        if f(z_1)-f(z_1+h)<0: #condición del mínimo
                            ext.append((z_1,"mínimo")) #guardar tupla en ext;
                        else:
                            ext.append((z_1,"máximo")) #guardar tupla en ext;


extreme_number=len(ext) #número de extremos;
print("La función tiene %i extremos."%extreme_number)
print("Los extremos son los siguientes:")
for i in range(len(ext)):
    print("El extremo %d es: "%(i+1), ext[i]) #imprimir resultado;


#gráficar x vs t y x_prim vs t;
plt.plot(t,x,color="red",label="$x(t)$") #función gráficada;
plt.plot(t,x_prim,color="orange",label="$x'(t)$") #primera derivada gráficada;
plt.xlabel("$t$") #nombrar eje x como t;
plt.ylabel("$x(t)$, $x'(t)$") #nombrar eje y como x(t), x'(t);
plt.legend() #diferenciar curvas;
plt.title("$x(t)$ y $x'(t)$ en función de $t$") #título; 
plt.grid(True)# poner rejillas;
plt.show() #mostrar resultado en conjunto;
