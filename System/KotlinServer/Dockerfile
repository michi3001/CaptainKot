# Stage 1: Build Kotlin Compiler
FROM python:3.11-slim AS compilerbuild

# Install the necessary build tools for the Cap'n Proto compiler, including cmake
RUN apt-get update && \
    apt-get install -y capnproto autoconf automake libtool curl make g++ unzip cmake && \
    apt-get clean

# Build the Cap'n Proto schemas
COPY ./KotlinCompiler/schemas/ /KotlinCompiler/schemas
COPY ./KotlinCompiler/src/ /KotlinCompiler/src
COPY ./KotlinCompiler/CMakeLists.txt /KotlinCompiler

WORKDIR /KotlinCompiler

RUN mkdir build && cd build && cmake .. && \
    cmake --build . --verbose

RUN /KotlinCompiler/build/KotlinCompiler ./schemas/calculator.capnp


# Stage 2: Build Kotlin Server
FROM openjdk:17-slim

# Install Maven and Python 3 along with required packages
RUN apt-get update && \
    apt-get install -y maven python3 python3-pip g++ && \
    apt-get clean

# Install pycapnp
RUN pip3 install pycapnp

WORKDIR /app

# Copy the Kotlin source files
COPY ./KotlinServer/project/src ./src

# Copy the generated Kotlin interface file from the first stage
COPY --from=compilerbuild /KotlinCompiler/output/CalculatorInterface.kt ./src/main/kotlin/org/capnkot/calculator/interfaces/

# Add package declaration to the interface file
RUN sed -i '1s|^|package org.capnkot.calculator.interfaces\n|' ./src/main/kotlin/org/capnkot/calculator/interfaces/CalculatorInterface.kt

# Copy the Maven project file
COPY ./KotlinServer/project/pom.xml /app/

# Pre-fetch Maven dependencies
RUN mvn clean install

# Package the Maven project
RUN mvn package

EXPOSE 8080

# Copy Python scripts for serialization/deserialization
COPY ./KotlinServer/project/src/main/resources/deserializer.py ./src/main/resources/deserializer.py
COPY ./KotlinServer/project/src/main/resources/serializer.py ./srcmain/resources/serializer.py
COPY ./KotlinCompiler/schemas/ ./


# Debug sleep
# CMD ["sleep", "infinity"]

# Start the Kotlin server
CMD ["java", "-jar", "target/kotlinServer.jar"]
