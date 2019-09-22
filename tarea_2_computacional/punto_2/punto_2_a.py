import numpy as np #importar módulo númpy

theta_0=np.pi/16 #amplitud
g=9.8 #aceleración de la gravedad
l=1 #logitud del péndulo

n=int(input("ingrese el valor de subintervalos: ")) #se pide por pantalla el dato n

theta=np.linspace(0,theta_0,n+1) #intervalo de integración
theta=[i for i in theta] #transformación del arreglo de numpy a lista
theta.pop(len(theta)-1) #eliminación del último punto theta (divergencia)
theta=np.array(theta) #transformación de lista a arreglo de numpy

h=theta[1]-theta[0] #diferencia de valores en theta

alpha=h/2 #factor alpha

beta=4*pow(l/(2*g),1/2) #factor beta

#definición de la función
f=beta/(pow(np.cos(theta)-np.cos(theta_0),1/2))

Int=0 #inicialización de la integral en 0

#integral generada por medio de búcle for
for i in range(len(f)): #desde 0 hasta len(f)-1
    if i==len(f)-1: #en el último elemento de f
        pass #el último elemento de f no ejecutará el método del trapecio
    else:
        Int+=alpha*(f[i]+f[i+1]) #método del trapecio

print("Resultado de la integral (método del trapecio): %f"%Int)
#se mostrará por pantalla el resultado
error=abs(1-Int/2.01194)#cálculo del error
print("El error es:", end=" ")
print(error) #se muestra por pantalla el error
