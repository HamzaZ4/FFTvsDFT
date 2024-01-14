import wave
import math
import numpy as np
import scipy.io.wavfile  as wav
import matplotlib.pyplot as plt
import time


# il faut premierement que j'ai des sample points de mon wav file



Fs, data = wav.read('../../TestingSounds/FFT/tuba-55(0.2).wav') # On veut lire les données du son


start = time.time() # commencer un chronometre
# on fait le fft
fft = np.fft.fft(data)

end = time.time() # terminer le chronometre quand le fft fini

# Creer le domaine de frequence

print(data.shape[0])
print(Fs)

freq = np.fft.fftfreq(data.shape[0],1/Fs)

print(freq)
freq_axis = np.linspace(0, 44100, len(freq))



plt.figure()

plt.stem(freq , np.abs(fft)/90, 'b', markerfmt = " ", basefmt="-b")

plt.xlim([0, 1000])
plt.xlabel("Frequence Hz")
plt.ylabel("Amplitude")
temps = end - start
print("Le programme a pris " + str(temps) + " secondes")
plt.show()


