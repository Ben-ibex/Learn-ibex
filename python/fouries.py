import numpy as np
import matplotlib.pyplot as plt

# Generate a time-domain signal: a combination of two sine waves
sampling_rate = 1000  # Sampling rate in Hz
t = np.linspace(0, 1, sampling_rate, endpoint=False)  # Time vector (1 second)

# Sine waves with different frequencies
freq1 = 50  # Frequency of 50 Hz
freq2 = 120  # Frequency of 120 Hz
signal = np.sin(2 * np.pi * freq1 * t) + 0.5 * np.sin(2 * np.pi * freq2 * t)

# Perform Fast Fourier Transform (FFT)
fft_result = np.fft.fft(signal)
fft_freq = np.fft.fftfreq(len(t), d=1/sampling_rate)  # Frequency axis

# Take the magnitude of the FFT result
magnitude = np.abs(fft_result)

# Plot the original signal and its frequency spectrum
plt.figure(figsize=(12, 6))

# Plot the time-domain signal
plt.subplot(2, 1, 1)
plt.plot(t, signal)
plt.title("Time-Domain Signal")
plt.xlabel("Time(s)")
plt.ylabel("Amplitude")

# Plot the frequency spectrum (positive frequencies only)
plt.subplot(2, 1, 2)
plt.plot(fft_freq[:sampling_rate // 2], magnitude[:sampling_rate // 2])
plt.title("Frequency Spectrum")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.tight_layout()

plt.show()
