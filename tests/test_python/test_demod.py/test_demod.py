from dsp_wrappers import apply_fir_filter

def test_fir_shape():
    data = [complex(x, 0) for x in range(100)]
    result = apply_fir_filter(data)
    assert len(result) == len(data)
