import matplotlib.pyplot as plt #Importación del módulo matplotlib y asignación del nickname plt;
import pandas as pd #importación del módulo pandas y asignación del nickname pd;

#apertura de un archivo .dat usando una variable temporal file;
with open("datos.dat", "r") as file:
    archivo=file.read()

#creación de lista files con el contenido del archivo .dat;
files=[i for i in archivo if i is not "\n" ] #eliminación de los saltos de líneas;
files=files[18:] #eliminación de 17 bits de información en la lista files para dejar el contenido númerico;

new_files=" " #creación de string vacío new_files;

#concatenación de los elementos de files en new_files;
for i in files:
    new_files+=i
    
files=new_files.split(" ") #conversión de files de ser un string a una lista;

files=[i for i in files if i is not ''] #eliminación de elementos que son un espacio en blanco;

files=[float(i) for i in files] #transformación de los elementos de files de ser strings a ser de tipo real;

#creación de listas vacías;
t=[] #almacén de los datos de tiempo;
x=[] #almacén de los datos de posición;
h=[] #almacén de los datos de intervalos temporales;
f_1_3=[] #almacén de los datos de la primera derivada de x con paso adaptativo;
f_2_3=[] #almacén de los datos de la segunda derivada de x con paso adaptativo;

#la lista files tiene como elementos en las posiciones pares los datos del tiempo,
#en las posiciones impares están los datos de la posición;

#para posición x y tiempo t;
for i in range(len(files)):
    if i%2==0:
        t.append(files[i]) #agregar solo las posiciones pares de files;
    else:
        x.append(files[i]) #agregar solo las posiciones impares de files;

#para h;
for i in range(len(t)):
    if i==len(t)-1:
        pass #eliminar el último punto porque no existe un punto información posterior;
    else:
        h.append(t[i+1]-t[i]) #definición de intervalos temporales;

#para las derivadas;
for i in range(len(x)):
    if i==0 or i==len(x)-1:
        pass
    else:
        f_1_3.append((h[i-1]**2*x[i+1]+(h[i]**2-h[i-1]**2)*x[i]-h[i]**2*x[i-1])/(h[i]*h[i-1]**2+h[i-1]*h[i]**2))
        f_2_3.append((2*(h[i-1]*x[i+1]+h[i]*x[i-1]-x[i]*(h[i-1]+h[i])))/(h[i]*h[i-1]**2+h[i-1]*h[i]**2))

x.pop(0) #eliminación del primer elemento en x;
x.pop(len(x)-1) #eliminación del último elemento en x;
t.pop(0) #eliminación del primer elemento en t;
t.pop(len(t)-1) #eliminación del último elemento en t;

datos={"t":t, "x":x, "dx(3)":f_1_3, "ddx(3)":f_2_3} #diccionario con los datos del archivo .dat almacenados;
df=pd.DataFrame(datos) #creación de un dataframe con la información del diccionario datos;
df.to_csv("datos.csv") #transformación del dataframe df a un archivo csv;
df=pd.read_csv("datos.csv", header=None, skiprows=1, names=["Número", "t", "x",
                                                                              "dx(3)", "ddx(3)"]) #lectura de datos
while True:
    Q=input("¿Desea ver la tabla de datos del archivo datos.dat? y/n: ")
    if Q=="y":
        print(df) #visualización de los datos.
        break
    else:
        break
        
msm_2="¿Desea usar el graficador de datos? y/n: "
print("="*(len(msm_2)+2))
Q_1=input(msm_2) 
print("="*(len(msm_2)+2))
while True:
    if Q_1=="y":
        print("Elija alguna de estas optiones introduciendo el número de la opción: ")
        print("1. Gráfico de posición en función del tiempo")
        print("2. Gráfico de velocidad en función del tiempo")
        print("3. Gráfico de aceleración en función del tiempo")
        print("4. Gráfico combinado de posición, velocidad y aceleración vs tiempo")
        print("5. salir")
        print(" ")
        ch=input("Por favor introduzca el número de la opción que desea usar: ")
        print(" ")
        if ch=="1" or ch=="2" or ch=="3" or ch=="4" or ch=="5":
            if ch=="1":
                plt.plot(t,x,"-.",color="blue",label="$x(t)$")
                plt.title("Posición $x$ en función del tiempo $t$")
                plt.xlabel("Tiempo $t$")
                plt.ylabel("Posición $x(t)$")
                plt.grid(True)
                plt.legend()
                plt.show()
                break #salida del búcle infinito
            elif ch=="2":
                plt.plot(t,f_1_3,"--",color="green",label="$\dot{x}(t)$")
                plt.title("Velocidad $\dot{x}$ en función del tiempo $t$")
                plt.xlabel("Tiempo $t$")
                plt.ylabel("Velocidad $\dot{x}(t)$")
                plt.grid(True)
                plt.legend()
                plt.show()
                break #salida del búcle infinito    
            elif ch=="3":
                plt.plot(t,f_2_3,"-",color="red",label="$\ddot{x}(t)$")
                plt.title("Aceleración $\ddot{x}$ en función del tiempo $t$")
                plt.xlabel("Tiempo $t$")
                plt.ylabel("Aceleración $\ddot{x}$")
                plt.grid(True)
                plt.legend()
                plt.show()
                break #salida del búcle infinito
            elif ch=="4":
                plt.plot(t,x,"-.",color="blue",label="$x(t)$")
                plt.plot(t,f_1_3,"--",color="green",label="$\dot{x}(t)$")
                plt.plot(t,f_2_3,"-",color="red",label="$\ddot{x}(t)$")
                plt.title("Posición, velocidad y aceleración en función del tiempo $t$")
                plt.xlabel("Tiempo $t$")
                plt.grid(True)
                plt.legend()
                plt.show()
                break #salida del búcle infinito
            elif ch=="5":
                break #salida del búcle infinito
        else:
            msm_2="Intente con alguna de las siguientes opciones: 1, 2, 3, 4 o 5."
            print("="*len(msm_2)) #construcción de dercorador
            print("¡Entrada mala!")
            print(msm_2) #mensaje de aclaración
            print("="*len(msm)) #decorador
