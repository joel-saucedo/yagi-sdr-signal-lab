from rtlsdr import RtlSdr

def get_samples(n=256*1024, center_freq=428e6, rate=2.4e6):
    sdr = RtlSdr()
    sdr.sample_rate = rate
    sdr.center_freq = center_freq
    sdr.gain = 'auto'
    data = sdr.read_samples(n)
    sdr.close()
    return data
