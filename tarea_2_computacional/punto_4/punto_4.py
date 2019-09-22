#apertura de datos.dat;
with open("datos.dat","r") as file:
    archivo=file.read() #lectura del archivo datos.dat;
   
files=[i for i in archivo if i is not "\n"] #guardar datos en files omitiendo los espacios;
new_files=" " #creación de new_files (variable);

for i in files:
    new_files+=i #concatenación del contenido de files dentro de new_files;

file=new_files.split(" ") #transformación del string new_files a la lista file;
file=[i for i in file if i is not ''] #eliminación de los espacios en blanco;

file=[float(i) for i in file] #transformación de datos string a tipo flotante;

x=[] #creación de contenedor vacío para datos de x;
f=[] #creación de contenedor vacío para datos de f;

for i in range(len(file)):
    if i%2==0: #si la posición es par se guardará en x;
        x.append(file[i])
    else:
        f.append(file[i]) #si la posición es impar se guardará en f;
#extrapolación lineal
x.append(1.816890) #dato posterior al último para extrapolar (dato muy cercano);
f.append(f[len(f)-2]+((x[len(x)-1]-x[len(x)-3])/(x[len(x)-2]-x[len(x)-3]))*(f[len(f)-1]-f[len(f)-2])) #dato extrapolado;

#integración
h=[] #contenedor vacío que posee las diferencias entre puntos adyacentes;
for i in range(len(x)):
    if i==len(x)-1: #omitir la diferencia en el último punto de x;
        pass
    else:
        h.append(x[i+1]-x[i]) #diferencia entre puntos adyacentes;


a1=[]#contenedor de datos de la constante a1;
for j in range(int(len(x)/3)):
    a1.append((1/12)*(h[3*j]+h[3*j+1]+h[3*j+2])*((3*h[3*j]**2-h[3*j+1]**2+2*h[3*j]*(h[3*j+1]-h[3*j+2])+h[3*j+2]**2)/(h[3*j]*(h[3*j]+h[3*j+1]))))


a2=[]#contenedor de datos de la constante a2;
for j in range(int(len(x)/3)):

    a2.append((1/12)*(h[3*j]+h[3*j+1]+h[3*j+2])*(((h[3*j]+h[3*j+1]-h[3*j+2])*(h[3*j]+h[3*j+1]+h[3*j+2])**2)/(h[3*j]*h[3*j+1]*(h[3*j+1]+h[3*j+2]))))

a3=[]#contenedor de datos de la constante a3;
for j in range(int(len(x)/3)):

    a3.append((1/12)*(h[3*j]+h[3*j+1]+h[3*j+2])*(((-h[3*j]+h[3*j+1]+h[3*j+2])*(h[3*j]+h[3*j+1]+h[3*j+2])**2)/(h[3*j+1]*(h[3*j]+h[3*j+1])*h[3*j+2])))

a4=[]#contenedor de datos de la constante a4;
for j in range(int(len(x)/3)):

    a4.append((1/12)*(h[3*j]+h[3*j+1]+h[3*j+2])*((h[3*j]**2-h[3*j+1]**2+2*(-h[3*j]+h[3*j+1])*h[3*j+2]+3*h[3*j+2]**2)/(h[3*j+2]*(h[3*j+1]+h[3*j+2]))))


Int=0 #inicialización de la integral en 0;
for j in range(int(len(x)/3)):
    Int+=a1[j]*f[3*j]+a2[j]*f[3*j+1]+a3[j]*f[3*j+2]+a4[j]*f[3*j+3] #integral con extrapolación de orden 3;

#método trapecio con paso adaptativo
Int_1=0 #inicialización de la integral en 0;
for i in range(len(f)):
    if i==len(f)-1: #no aplicar en el último punto la fórmula;
        pass
    else:
        Int_1+=(1/2)*h[i]*(f[i]+f[i+1]) #regla del trapecio;



print("Integral de la interpolación grado 3: %f "%Int) #resultado del método de interpolación grado 3;
print("Integral de la interpolación grado 1: %f"%Int_1) #resultado del método de interpolación grado 1;
error=abs(1-(Int/1.3852229032511942)) #error relativo interpolación grado 3;
error_1=abs(1-(Int_1/1.3852229032511942)) #error relativo interpolación grado 1;
print("Error interpolación grado 3: %f"%error) #mostrar por pantalla el error;
print("Error interpolación grado 1: %f"%error_1) #mostrar por pantalla el error;
