# Stage 1: Build Kotlin Compiler
FROM alpine:latest AS compilerBuild

# Install necessary tools for building the Kotlin compiler (g++, cmake, git)
RUN apk add --no-cache g++ cmake make build-base

COPY ./KotlinCompiler/schemas/ /KotlinCompiler/schemas
COPY ./KotlinCompiler/src/ /KotlinCompiler/src
COPY ./KotlinCompiler/CMakeLists.txt /KotlinCompiler

WORKDIR /KotlinCompiler

# Build the Cap'n Proto compiler
RUN mkdir build && cd build && cmake ..
RUN cd build && cmake --build . --verbose

RUN cd build && find . -type f -exec ls -l {} \;


# DEBUG: List the contents of the build directory
# RUN cd build && ls -l && sleep 99999


RUN /KotlinCompiler/build/KotlinCompiler ./schemas/calculator.capnp

# DEBUG: List the contents of the build directory
# RUN cd output && ls -l && sleep 99999


# Stage 2: Build the Kotlin Server
FROM openjdk:17-alpine

RUN apk add --no-cache maven

WORKDIR /app

COPY ./KotlinServer/project/src ./src

# Copy the generated Kotlin interface file from the compiler build stage
COPY --from=compilerBuild /KotlinCompiler/output/CalculatorInterface.kt ./src/main/kotlin/org/capnkot/calculator/interfaces/

# Add package declaration to the interface file
RUN sed -i '1s|^|package org.capnkot.calculator.interfaces\n|' ./src/main/kotlin/org/capnkot/calculator/interfaces/CalculatorInterface.kt

COPY ./KotlinServer/project/pom.xml /app/

RUN mvn dependency:go-offline

RUN mvn package

EXPOSE 8080

CMD ["java", "-jar", "target/kotlinServer.jar"]
