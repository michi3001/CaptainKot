cmake_minimum_required(VERSION 3.10)
project(Kotlin_Compiler)

# Setze den C++-Standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Füge alle Quellcodedateien hinzu
add_executable(Kotlin_Compiler
    src/main.cpp
    src/parser.cpp
    src/generator.cpp
)