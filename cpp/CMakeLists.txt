cmake_minimum_required(VERSION 3.14)
project(yagi_sdr_dsp)

find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_package(SWIG REQUIRED)
include(UseSWIG)

set(CMAKE_CXX_STANDARD 17)

include_directories(${PROJECT_SOURCE_DIR}/include)

add_library(dsp SHARED src/dsp.cpp)
target_include_directories(dsp PUBLIC include)

# SWIG binding
set_source_files_properties(swig/dsp.i PROPERTIES CPLUSPLUS ON)
swig_add_library(dsp_cpp
  TYPE MODULE
  LANGUAGE python
  SOURCES swig/dsp.i src/dsp.cpp
)
swig_link_libraries(dsp_cpp ${Python3_LIBRARIES})
