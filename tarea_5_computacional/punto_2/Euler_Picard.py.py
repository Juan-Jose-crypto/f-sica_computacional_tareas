import numpy as np #importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib;

#constantes;
A=0.93 #medido en m^2;
rho= 1.2 #medido en kg/m^3;
m=250 #medido en kg;
g=9.8 #medido en m/s^2
N=10**3 #número de puntos de la gráfica;
t=np.linspace(0,7.9,N) #intervalo de tiempo;
tau=t[1]-t[0] #intervalo de tiempo tau; medido en s;

#variables;
x=[] #contenedor vacío de posición;
v=[] #contenedor vacío de velocidad;
a=[] #contenedor vacío de aceleración;

#condiciones iniciales;
v_0=67 #módulo de la velocidad inicial; medido en m/s;
v_i=v_0 #guardar dato v_0 en v_i;
theta_0=(42.5*np.pi)/180 #ángulo de la velocidad respecto a la horizontal;
x_0=0 #posición inicial en x;
y_0=0 #posición inicial en y;
r_0=np.array([x_0,y_0]) #vector posición inicial;<--------- posición;
v_0_x=v_0*np.cos(theta_0) #velocidad inicial en x;
v_0_y=v_0*np.sin(theta_0) #velocidad inicial en y;
v_0=np.array([v_0_x,v_0_y]) #vector velocidad inicial;<--------- velocidad;
a_0_x=-(A*rho*np.linalg.norm(v_0)/(2*m))*v_0_x #aceleración inicial en x;
a_0_y=-(g+(A*rho*np.linalg.norm(v_0)/(2*m))*v_0_y) #aceleración inicial en y;
a_0=np.array([a_0_x,a_0_y]) #vector aceleración inicial;<---------aceleración;

#inicializar (0);
x.append(r_0) #guardar posición inicial;
v.append(v_0) #guardar velocidad inincial;
a.append(a_0) #guardar aceleración inicial;

#base cartesiana;
x_hat=np.array([1,0]) #base usual x en 2D;
y_hat=np.array([0,1]) #base usual y en 2D;

#siguiente punto (1);
x.append(x[0]+v[0]*tau) #Método de Euler;
v.append(v[0]+a[0]*tau)
v_1=v[1]
v_1_norm=np.linalg.norm(v_1)
a_1_x=-(A*rho*v_1_norm/(2*m))*(v_1@x_hat)
a_1_y=-(g+(A*rho*v_1_norm/(2*m))*(v_1@y_hat))
a_1=np.array([a_1_x,a_1_y])
a.append(a_1)

for i in range(len(t)):
    x_2=x[i+1]+v[i+1]*tau #predecir siguiente posición;
    v_2=v[i+1]+a[i+1]*tau #predecir siguiente velocidad;
    v_plus=v_2
    v_plus_norm=np.linalg.norm(v_plus)
    a_plus_x=-(A*rho*v_plus_norm/(2*m))*(v_plus@x_hat)
    a_plus_y=-(g+(A*rho*v_plus_norm/(2*m))*(v_plus@y_hat))
    a_plus=np.array([a_plus_x,a_plus_y])
    a.append(a_plus)
    x.append(x[i]+(tau/3)*(v_2+4*v[i+1]+v[i])) #corregir posición (Picard);
    v.append(v[i]+(tau/3)*(a[i+2]+4*a[i+1]+a[i])) #corregir velocidad (Picard);
        
           
x_1=[] #creación de contenedor vacío para la posición en x;
x_2=[] #creación de contenedor vacío para la posición en y;

for i in range(len(x)): #bucle for para guardado;
    x_1.append(x[i][0])
    x_2.append(x[i][1])

#gráficar y contra x;
plt.plot(x_1,x_2,'--',color='red')
plt.xlabel('$x(m)$')
plt.title('Trayectoria de motociclista con velocidad inicial %d m/s'%(v_i))
plt.ylabel('$y(m)$')
plt.grid(True)
plt.show() #mostrar resultado de la gráfica;
