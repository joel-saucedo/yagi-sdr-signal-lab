# yagi-sdr-signal-lab

A modular software-defined radio (SDR) signal processing pipeline built around a custom 10-element 428 MHz Yagi-Uda antenna and RTL-SDR hardware. The system uses C++ for high-performance signal processing (DSP) and Python for interfacing, data capture, visualization, and decoding.

## Project Objectives

- Design and build a tuned 428 MHz Yagi-Uda antenna
- Capture RF signals using RTL-SDR hardware
- Process IQ data using optimized C++ code
- Interface with Python via SWIG
- Visualize spectrum, demodulate FM/digital, and decode bitstreams
- Enable future support for packet detection, digital telemetry, and machine learning signal classification

---

## Directory Structure

```text
    




---

## Components to Develop

### 1. Hardware

- [x] Design 10-element Yagi-Uda antenna (complete)
- [x] Design and print 3D standoffs for elements
- [x] Assemble antenna on PVC boom
- [ ] Tune folded dipole impedance (optional optimization)

### 2. C++ Backend (`cpp/`)

- [x] `dsp.cpp` with FIR filtering
- [ ] `demod.cpp` for FM and BPSK demodulation
- [ ] `utils.cpp` for FFT, moving average, and error correction
- [x] `dsp.hpp` + header files for SWIG exposure
- [x] `dsp.i` SWIG interface file
- [ ] Expand SWIG bindings to include demodulation
- [x] CMake and Makefile for build automation

### 3. Python Interface (`python/`)

- [x] `capture_samples.py` using `pyrtlsdr`
- [x] `dsp_wrappers.py` to call C++ from Python
- [x] `plot_fft.py` for basic FFT visualization
- [ ] `demod_fm.py` with SWIG interface to C++ demodulator
- [ ] `decode_packets.py` to parse bitstreams
- [ ] `waterfall.py` and `constellation.py` for advanced visualization

### 4. Testing

- [x] `test_filters.cpp` for FIR verification
- [ ] Unit tests for FM demod and symbol mapping
- [ ] Python tests for packet decoding

---

### 5. Planned Extensions

- Add direction-finding support via phase-difference between antennas

- Implement adaptive filtering and error correction

- Use ML to classify signals (CNN on spectrograms)

- Add GUI with PyQt for real-time interaction

