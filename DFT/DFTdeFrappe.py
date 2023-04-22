import numpy as np
import matplotlib.pyplot as plt
import wave
import time


plt.title("Son non periodique")

plt.xlabel("Temps (s)")
plt.ylabel("Amplitude")



bruit = wave.open("200.03hz-_1_.wav", "r") # Le son: On "l'ouvre" pour donner acces aux donnes du signal

fe=44100 # Frequence d'echantillonnage

signal = bruit.readframes(-1) # lire le fichier wav
signal = np.frombuffer(signal, "int16") # convertir la lecture du fichier wav en binaire a des entiers



def DFT(x):

    N = len(x) # Nombre d'echantillons dans x
    n = np.arange(N) # on cree un vecter [ 0,1,2,3...(N-1) ]
    k = n.reshape((N, 1)) # on cree un vecter [ 0,1,2,3...(N-1) ] mais on reshape, donc c'est un vecteur "vertical" pour ensuite pouvoir faire multiplication plus tard
    W = np.exp((-2j * np.pi * k * n) / N)
    X = np.dot(W, x) # Produit scalaire entre les 2

    return X

start = time.time()
time.sleep(0)
X = DFT(signal)
end = time.time()
times = end -start
print("Le temps d'execution est de " + str(times) +" secondes")




# CALCUL ET FORMATTAGE DES DONNEES QUI SERONT UTILISES POUR CONSTRUIRE LE GRAPHIQUE

N = len(signal) # Le nombre de points d'echantillonnage = nb d'elements dans le signal
n = np.arange(N) # on cree un vecter [ 0,1,2,3...(N-1) ]
T = N / fe # Ca represente la duree de notre echantillon en secondes  ( N points avec fs points /s, la division nous redonne des s ( temps de signal))
freq = n / T  # n = Le nieme harmonique, /T, pcq on divise par la période.


# FORMALITES POUR LE GRAPHIQUE A LA FIN

plt.stem(freq/2, abs(X), 'b', \
         markerfmt=" ", basefmt="-b")  # Stem = les lignes verticales qui apparaitront sur notre graphique final

plt.xlabel('Freq (Hz)')
plt.ylabel('Amplitude')
plt.xlim([0, 1000])
times = end -start
print("Le temps d'execution est de " + str(times) +" secondes")
plt.show()

