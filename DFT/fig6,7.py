import numpy as np
import matplotlib.pyplot as plt
import wave
# Prendre valeurs de fct sinus et les mettre dans un vecteur x[n]

x=[]*40

sr = 1000

ts = 1.0/1000

f = 12.

t = np.arange(0,1,ts)

x = 1*np.sin(2*np.pi*f*t) # le t c'est notre variable independante NP.Sin prend des array sinon sa marche pas

f = 9

x+= 3*np.sin(2*np.pi*f*t)

f = 2

x+= 4*np.sin(2*np.pi*f*t)

plt.xlabel("Temps(s)")
plt.ylabel("Amplitude")
plt.plot(t,x,"r")
plt.show()