import numpy as np #Importar módulo numpy;
import matplotlib.pyplot as plt #importar módulo matplotlib;

class Fourier_Transform:
    function=0 #función a transformar;
    N=0 #número de puntos;
    omega=0 #frecuencia angular;
    lim_min=0 #límite inferior;
    lim_max=0 #límite superior;
    def __init__(self,function,N,omega,lim_min,lim_max):
        self.function=function #función;
        self.N=N #número de puntos;
        self.omega=omega #frecuencia angular;
        self.lim_min=lim_min #limite inferior;
        self.lim_max=lim_max #limite superior;
        
    #métodos de la clase;
    #métodos set;
    def set_function(self,function):
        self.function=function #elegir función;
    def set_omega(self,omega):
        self.omega=omega #elegir frecuencia angular;
    def set_points_number(self,N):
        self.N=N #elegir número de puntos;
    def set_lim_min(self,lim_min):
        self.lim_min=lim_min #elegir límite inferior;
    def set_lim_max(self,lim_max):
        self.lim_max=lim_max #elegir límite máximo;

    #métodos get;
    def get_function(self):
        return(self.function) #obtener función;
    def get_omega(self):
        return(self.omega) #obtener omega;
    def get_points_number(self):
        return(self.N) #obtener número de puntos;
    def get_n(self):
        return(self.get_points_number()-1) #obtener número de subintervalos;
    def get_h(self):
        return(self.get_time()[1]-self.get_time()[0]) #obtener diferencia entre el segundo punto y el primero;
    def get_lim_max(self):
        return(self.lim_max) #obtener limite superior;
    def get_lim_min(self):
        return(self.lim_min) #obtener limite inferior;
    def get_time(self):
        #obtener arreglo de posibles tiempos t;
        return(np.linspace(self.get_lim_min(),self.get_lim_max(),self.get_points_number())) #obtener intervalo de tiempo;
    def get_transform(self):
        #obtener transformada de Fourier para un valor de omega;
        Int=0 #inicialización de la integral;
        for i in range(self.get_n()-1):
            #método del trapecio;
            Int+=(self.get_h()/2)*(self.get_function()[i]+self.get_function()[i+1])
        return(Int) #obtener valor de la transformada de Fourier;


#Fourier_Transform(función,número puntos,frecuencia angular,mínimo,máximo);

object_1=Fourier_Transform(0,0,0,0,0) #creación de objeto;
object_1.set_points_number(10**3) #elección del número de puntos (mil puntos);
object_1.set_lim_min(-2.5) #elección del límite inferior;
object_1.set_lim_max(2.5) #elección del límite superior;
t=object_1.get_time() #variable t guarda el arreglo time;

omega=np.linspace(-5,5,100) #arreglo con posibles valores de omega;
omega_list=[i for i in omega] #transformación de omega en lista;
g_analitic=(np.exp((-1/4)*(1+omega)**2)*(1+np.exp(omega)))/(2*np.sqrt(2)) #TFI analítica;
g=[] #se almacena valor de la TFI númerica en esta lista vacía;
for i in omega:
    object_1.set_omega(i) #elegir omega igual a i;
    omega=object_1.get_omega() #almacenar .get_omega en omega;
    alpha=1/np.sqrt(2*np.pi) #factor que acompaña la función
    f=np.exp(-t**2)*np.cos(t) #función definida
    f_F=alpha*np.exp(1j*omega*t)*f #función de Fourier;
    object_1.set_function(f_F) #elegir función
    g.append(object_1.get_transform()) #añadir a la lista g;

g_real=[i.real for i in g] #parte real de g;
g_imag=[i.imag for i in g] #parte imaginaria de g;

Error=0 #inicialización del error en 0;
for i in range(len(g_real)):
    Error+=(1/len(g_analitic))*abs(1-(g_real[i]/g_analitic[i])) #error relativo promedio;

print("El error relativo promedio de la Transformada de Fourier númerica es:",end=" ")
print(Error)

plt.plot(omega_list,g_real,"--",label="$g_{DFT}^{real}$",color="red") #parte real
plt.plot(omega_list,g_imag,":",label="$g_{DFT}^{Imag}$",color="orange") #parte imaginaria
plt.plot(omega_list,g_analitic,label="$g_{analitic}$",color="blue") #transformada inversa analítica
plt.title("Gráfico $g(\omega)$ en función de la frecuencia angular $\omega$") #añadir título
plt.legend() #añadir leyendas;
plt.xlabel("Frecuencia $\omega$")#etiquetar eje x;
plt.ylabel("$g(\omega)$")#etiquetar eje y;
plt.show() #mostrar todo en un gráfico.
