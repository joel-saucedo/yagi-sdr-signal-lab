#include "dsp.hpp"
#include <cmath>

std::pair<std::vector<float>, std::vector<float>> fir_filter(
    const std::vector<float>& real,
    const std::vector<float>& imag
) {
    // Simple low-pass FIR example
    const int N = 5;
    float coeffs[N] = {0.1, 0.15, 0.5, 0.15, 0.1};
    std::vector<float> r_out(real.size(), 0), i_out(imag.size(), 0);

    for (size_t i = N; i < real.size(); ++i) {
        for (int j = 0; j < N; ++j) {
            r_out[i] += coeffs[j] * real[i - j];
            i_out[i] += coeffs[j] * imag[i - j];
        }
    }
    return {r_out, i_out};
}
