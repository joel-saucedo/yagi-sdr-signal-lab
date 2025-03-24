## Signal Pipeline

1. RF signal captured by antenna
2. IQ samples acquired using RTL-SDR
3. C++ processes samples: filtering, demod, decoding
4. Python visualizes spectrum, waterfall, bitstream

Mathematical models include:
- Fourier transform for spectral analysis
- FIR/IIR for bandpass filtering
- Arctangent demodulation for FM
