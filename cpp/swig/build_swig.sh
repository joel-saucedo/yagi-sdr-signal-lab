%module _dsp_cpp
%{
#include "../include/dsp.hpp"
%}

%include "std_vector.i"
%template(FloatVector) std::vector<float>;

%include "../include/dsp.hpp"
