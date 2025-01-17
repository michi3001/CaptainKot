# CaptainKot

CaptainKot is a Kotlin-based server application that uses the Cap’n Proto serialization framework to define and compile data interfaces. The project allows developers to easily create and manage Kotlin data models and services, providing a robust foundation for building applications that require efficient data serialization and communication.

## Features

- **Kotlin Compiler**: Compiles Cap’n Proto schemas into Kotlin interface files.
- **Kotlin Server**: A lightweight server that can handle requests using the generated interfaces.
- **Maven Integration**: Uses Maven for dependency management and packaging.

## Prerequisites

Before running the CaptainKot project, ensure you have the following installed on your machine:
- Docker: To build and run the application in containers.

## Getting Started

### Clone the Repository

```bash
git clone https://github.com/yourusername/CaptainKot.git
cd CaptainKot/System
```
 Ensure you have your Capnproto schema in the folder: [System/KotlinCompiler/schemas](System/KotlinCompiler/schemas/)

### Run the application
```bash
docker-compose up --build
```

## Launch the System local without using docker

For trying out the application in Windows without using Docker. You need to:
* compile the Capnproto Schema Files to Kotlin Glue Code as described [here](/System/KotlinCompiler/README.md). The generated Glue has to copied into [System/KotlinServer/project/src/main/kotlin/org/capnkot/calculator/interfaces](System/KotlinServer/project/src/main/kotlin/org/capnkot/calculator/interfaces/)

* change the following code lines in [CalculatorImpl.kt](System/KotlinServer/project/src/main/kotlin/org/capnkot/calculator/CalculatorImpl.kt):
``` python
val deserializeProcess = ProcessBuilder("python3", "./src/main/resources/deserializer.py").start()
// use this for windows development: val serializeProcess = ProcessBuilder("python", "./src/main/resources/serializer.py").start()

val serializeProcess = ProcessBuilder("python3", "./src/main/resources/serializer.py").start()
// use this for windows development: val serializeProcess = ProcessBuilder("python", "./src/main/resources/serializer.py").start()
```
This has to be done because in the docker container the python code has to be started with 'python3' and under windows with 'python'

* change the following code lines in [client.py](System/PythonClient/client.py)
``` python
# socketObject.connect(('localhost', 5000))    localhost for local use
socketObject.connect(('server', 5000))        # server for docker use
```

## Access the Application
This application provides several mathematical operations (addition, subtraction, multiplication, and division) via an API. Below are instructions on how to access and use the API endpoints.
 
1. **Open the Swagger UI**:
   - Open your web browser and navigate to http://localhost/docs. This will open the Swagger UI, an interactive tool for exploring  and testing the API.
   - In Swagger UI, expand the available operations: add, subtract, multiply, and divide.
   - Enter your numbers (num1 and num2) and click Execute to see the results.


2. **Directly Access Routes in the Browser**:

   Alternatively, you can access the API routes directly via your browser by using the following URL structure:
   
   ### Addition:
   - http://localhost/add?num1=5&num2=3
   ### Subtraction:
   - http://localhost/subtract?num1=5&num2=3
   ### Multiplication:
   - http://localhost/multiply?num1=5&num2=3
   ### Division:
   - http://localhost/divide?num1=5&num2=3

Simply replace `num1` and `num2` with your desired numbers. These endpoints will perform the respective operations and return the result.