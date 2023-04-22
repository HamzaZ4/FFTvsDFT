import numpy as np
import matplotlib.pyplot as plt

dx =.001 # Discretization
L=np.pi # Period/2
x=L*np.arange(-1+dx,1+dx,dx)
n=len(x)
nquart = int(np.floor(n/6))






#Les lignes suivantes( 16 a 21 ) sont simplement la formation de la fonction que je vise a approximer avec la serie de FOURIER
f = np.zeros_like(x)
f[nquart:2*nquart] = (6/n)*np.arange(1,nquart+1)
f[2*nquart:3*nquart] = np.ones_like(nquart)
f[3*nquart:4*nquart] = np.ones_like(nquart) - (3/n)*np.arange(0,nquart)
f[4*nquart:5*nquart] = [0.5]*nquart - (6/n)*np.arange(0,nquart)
f[5*nquart:6*nquart] = [-0.5]*nquart + (6/n)*np.arange(0,nquart)


fig, ax = plt.subplots() # Fig = figure( canvas we're drawing on ), ax = defining an axis
ax.plot(x,f,color ='k')

name ="Accent"
cmap = plt.colormaps['tab10'] # juste des truc pour faire varier les couleurs
colors = cmap.colors
ax.set_prop_cycle(color=colors)

A0 = np.sum(f*np.ones_like(x))*dx  #
fFS=A0/2
A = np.zeros(50)
B= np.zeros(50)

# La serie de Fourier
for k in range(50): #On va calculer les coefficients en calculant les produits scalaires de fonctions
    A[k] = np.sum(f*np.cos(np.pi*(k+1)*x/L)) *dx #On fait les vecteurs des coefficients
    B[k] = np.sum(f*np.cos(np.pi*k+1)*x/L)*dx
    fFS =fFS + A[k]*np.cos((k+1)*np.pi*x/L) + B[k]*np.sin((k+1)*np.pi*x/L)


    #On va de K=1 à 20 fonctions pour voir comment l'approximation s'ajuste et
    # ressemble de plus en plus à ce qu'on cherche

ax.plot(x, fFS, '-')
plt.show()