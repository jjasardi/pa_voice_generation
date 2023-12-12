import wave
import numpy as np
import matplotlib.pyplot as plt


filepath = "../audio_assets/bae_pangram1.wav"
#filepath = "../audio_assets/bae_pangram2.wav"
#filepath = "../audio_assets/bae_phoneme_pangram1.wav"


signal_wave = wave.open(filepath, 'r')
sample_rate = 16000
sig = np.frombuffer(signal_wave.readframes(sample_rate), dtype=np.int16)

sig = sig[:]

plt.figure(1)

plot_a = plt.subplot(211)
plot_a.plot(sig)
plot_a.set_xlabel('Sample rate * time')
plot_a.set_ylabel('Energy')

plot_b = plt.subplot(212)
plot_b.specgram(sig, NFFT=1024, Fs=sample_rate, noverlap=900)
plot_b.set_xlabel('Time')
plot_b.set_ylabel('Frequency')

plt.show()