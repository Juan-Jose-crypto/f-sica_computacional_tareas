import matplotlib.pyplot as plt
import numpy as np

n=np.array([2,4,8,16,32,64,128,256,512,1024])
S=np.array([0.689549,1.102132,1.376447,1.565192,1.696939,1.789513,
            1.854770,1.900842,1.933394,1.956404])

plt.plot(n,S, "x" ,label="$S(n)$", color="red")
plt.title("Integral númerica $S$ en función del número de subintervalos $n$")
plt.ylabel("Integral númerica $S$")
plt.legend()
plt.xlabel("Número de subintervalos $n$")
plt.show()
