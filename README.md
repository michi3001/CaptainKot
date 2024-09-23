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

### Run the application
```bash
docker-compose up --build
```
