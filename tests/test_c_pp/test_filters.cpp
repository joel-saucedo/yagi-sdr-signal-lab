#include "dsp.hpp"
#include <cassert>

int main() {
    std::vector<float> r = {1, 2, 3, 4, 5};
    std::vector<float> i = {0, 0, 0, 0, 0};
    auto [out_r, out_i] = fir_filter(r, i);
    assert(out_r.size() == r.size());
    return 0;
}
