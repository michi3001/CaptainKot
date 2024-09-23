cmake_minimum_required(VERSION 3.10)
project(KotlinCompiler)

# Setze den C++-Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Füge alle Quellcodedateien hinzu
add_executable(KotlinCompiler
    src/main.cpp
    src/parser.cpp
    src/generator.cpp
)