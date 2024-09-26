# Kotlin Compiler

This project contains a simple C++-based compiler that reads Cap'n Proto schema files and generates Kotlin interfaces from them. The compiler supports several data types and converts them into the corresponding Kotlin data types.

## 1. Building the Compiler

To build the compiler, make sure you have the necessary build tools and a C++17-compatible compiler (e.g., `g++`) installed on your system. Additionally, `CMake` is used to generate the build system.

### Steps to Build the Compiler

1. **Clone the repository (if not already done):**
    ```bash
    git clone https://github.com/michi3001/CaptainKot.git
    cd KotlinCompiler
    ```

2. **Create a build directory:**
    ```bash
    mkdir build
    cd build
    ```

3. **Run CMake to configure the build system:**
    ```bash
    cmake ..
    ```

4. **Compile the compiler:**
     ```bash
    cmake --build .
    ```
    After successful compilation, an executable file (KotlinCompiler.exe) will be created in the `build` directory under the Debug folder.

## 2. Running the Compiler

Once the compiler has been successfully built, it can be used to translate Cap'n Proto schema files into Kotlin code.

### Steps to compile Cap'n Proto files:
    ```bash
    ./KotlinCompiler <path_to_schema_file>
    ```

    Example:
    ```bash
    ./KotlinCompiler ../schemas/calculator.capnp
    ```
