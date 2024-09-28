package org.capnkot.calculator

import java.net.ServerSocket

fun main() {
    val serverSocket = ServerSocket(5000)
    println("Server started under port 5000")
    println("If trying to access within docker compose the url is server:5000")
    println("If trying to access from outside the docker compose the url is localhost:5000")

    while (true) {
        val clientSocket = serverSocket.accept()
        println("Client connected")
        Thread { handleClient(clientSocket) }.start()
    }
}