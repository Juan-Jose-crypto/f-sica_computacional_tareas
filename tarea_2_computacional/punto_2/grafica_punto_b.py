import matplotlib.pyplot as plt
import numpy as np

n=np.array([4,8,16,32,64,128,256,512,1024])
S_1=np.array([1.102132,1.376447,1.565192,1.696939,1.789513,
            1.854770,1.900842,1.933394,1.956404])
S_2=np.array([1.091079,1.368084,1.559114,1.692590,1.786420,1.852577,
              1.899289, 1.932296,1.955627])

plt.plot(n,S_1, "x" ,label="Trapecio", color="red")
plt.plot(n,S_2, "*" ,label="Simpson", color="blue")
plt.title("Integral númerica $S$ en función del número de subintervalos $n$")
plt.ylabel("Integral númerica $S$")
plt.legend()
plt.xlabel("Número de subintervalos $n$")
plt.show()
