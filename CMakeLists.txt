cmake_minimum_required(VERSION 3.24)
project(Code_learning)

set(CMAKE_CXX_STANDARD 14)

include_directories(C)

add_executable(Code_learning
        C/first.cpp
        C/first.h C/fist.c)
