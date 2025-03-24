import _dsp_cpp  # SWIG-generated module

def apply_fir_filter(samples):
    real = [s.real for s in samples]
    imag = [s.imag for s in samples]
    filtered_real, filtered_imag = _dsp_cpp.fir_filter(real, imag)
    return [complex(r, i) for r, i in zip(filtered_real, filtered_imag)]
