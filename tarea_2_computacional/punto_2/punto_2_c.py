import numpy as np #importar módulo numpy

theta_0=np.pi/2 #amplitud que puede variarse
g=9.8 #aceleración de la gravedad
l=1 #logitud del péndulo
T_lim=2*np.pi*np.sqrt(l/g)#<----límite de pequeños ángulos

n=1024 #se fija el número de subintervalos

theta=np.linspace(0,theta_0,n+1) #intervalo de integración
theta=[i for i in theta] #transformación del arreglo de numpy a lista
theta.pop(len(theta)-1) #eliminación del último punto theta (divergencia)
theta=np.array(theta) #transformación de lista a arreglo de numpy
h=theta[1]-theta[0] #diferencia de valores en theta

alpha=h/3 #factor alpha

beta=4*pow(l/(2*g),1/2) #factor beta

#definición de la función
f=beta/(pow(np.cos(theta)-np.cos(theta_0),1/2))

Int=0 #inicialización de la integral en 0


#integral generada por medio de búcle for
for j in range(int(n/2)): #desde 0 hasta (n/2)-1
    if j==int((n/2))-1: # último slice 
        Int+=(h/12)*(-f[n-3]+8*f[n-2]+5*f[n-1]) #contribución de último slice
    else:
        Int+=alpha*(f[2*j]+4*f[2*j+1]+f[2*j+2]) #regla de Simpson

error=abs(1-Int/T_lim)#<--- error relativo

print("Resultado de la integral (regla de Simpson): %f"%Int)
print("Periodo de oscilación en el límite de ángulos pequeños: %f"%T_lim)
print("Error relativo al límite de ángulos pequeños: %f"%error)
#se mostrará por pantalla el resultado
