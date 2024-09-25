package org.capnkot.calculator

import java.net.ServerSocket

fun main() {
    val serverSocket = ServerSocket(8080)
    println("Server started under port 8080")
    println("If trying to access within docker compose the url is server:8080")
    println("If trying to access from outside the docker compose the url is localhost:8080")

    while (true) {
        val clientSocket = serverSocket.accept()
        println("Client connected")
        Thread { handleClient(clientSocket) }.start()
    }
}