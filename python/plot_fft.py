import numpy as np
import matplotlib.pyplot as plt

def plot_spectrum(samples):
    power = 20*np.log10(np.abs(np.fft.fftshift(np.fft.fft(samples))))
    plt.plot(power)
    plt.title("Spectrum")
    plt.xlabel("Frequency Bin")
    plt.ylabel("Power (dB)")
    plt.grid()
    plt.show()
