package org.capnkot.calculator

import java.io.DataInputStream
import java.io.DataOutputStream
import java.net.ServerSocket
import java.net.Socket
import org.json.JSONObject

import org.capnkot.calculator.interfaces.CalculatorInterface

class CalculatorImpl : CalculatorInterface {
    override fun add(num1: Double, num2: Double): Double {
        return num1 + num2
    }

    override fun subtract(num1: Double, num2: Double): Double {
        return num1 - num2
    }

    override fun multiply(num1: Double, num2: Double): Double {
        return num1 * num2
    }

    override fun divide(num1: Double, num2: Double): Double {
        if (num2 == 0.0) return -1.0      // Return -1 if division by zero: Error case
        return num1 / num2
    }
}

fun performCalculation(operation: String, num1: Double, num2: Double): Double {
    val calculator = CalculatorImpl()
    return when (operation) {
        "add" -> calculator.add(num1, num2)
        "subtract" -> calculator.subtract(num1, num2)
        "multiply" -> calculator.multiply(num1, num2)
        "divide" -> calculator.divide(num1, num2)
        else -> throw IllegalArgumentException("Unknown operation: $operation")
    }
}

fun handleClient(clientSocket: Socket) {
    val inputStream = DataInputStream(clientSocket.getInputStream())
    val outputStream = DataOutputStream(clientSocket.getOutputStream())

    try {
        // Read the request from the client
        val messageLength = inputStream.readInt()
        val messageBytes = ByteArray(messageLength)
        inputStream.readFully(messageBytes)

        // Start the Python process for deserialization
        val deserializeProcess = ProcessBuilder("python3", "./src/main/resources/deserializer.py").start()
        // use this for windows development: val serializeProcess = ProcessBuilder("python", "./src/main/resources/serializer.py").start()


        // Write the Client request to the Python process which deserializes it to JSON
        deserializeProcess.outputStream.use { it.write(messageBytes) }
        deserializeProcess.outputStream.close()

        val deserializeErrorStream = deserializeProcess.errorStream.bufferedReader().readText()
        val deserializeExitCode = deserializeProcess.waitFor()

        if (deserializeExitCode == 0) {
            // If successful, read the response
            val responseBytes = deserializeProcess.inputStream.readBytes()
            val jsonResponse = JSONObject(String(responseBytes))
            println("jsonResponse: $jsonResponse")

            val operation = jsonResponse.getString("operation")
            val num1 = jsonResponse.getDouble("num1")
            val num2 = jsonResponse.getDouble("num2")

            val result = performCalculation(operation, num1, num2)

            // Start the Python process for serializing the result in order to send it to the client

            val serializeProcess = ProcessBuilder("python3", "./src/main/resources/serializer.py").start()
            // use this for windows development: val serializeProcess = ProcessBuilder("python", "./src/main/resources/serializer.py").start()


            // Write the result to the serializer
            serializeProcess.outputStream.use { it.write(result.toString().toByteArray()) }
            serializeProcess.outputStream.close()

            val serializeErrorStream = serializeProcess.errorStream.bufferedReader().readText()
            val serializeExitCode = serializeProcess.waitFor()

            if (serializeExitCode == 0) {
                    // Read and send the final response
                    val finalResponseBytes = serializeProcess.inputStream.readBytes()

                    // Send the serialized response to the client
                    outputStream.writeInt(finalResponseBytes.size)
                    outputStream.write(finalResponseBytes)
                    outputStream.flush()
            } else {
                println("Error while serializing the response with Python script: $serializeErrorStream")
            }
        } else {
            println("Error while deserializing the request with Python script: $deserializeErrorStream")
        }
    } catch (e: Exception) {
        println("Error handling client: ${e.message}")
    } finally {
        clientSocket.close()
    }
}

fun main() {
    val serverSocket = ServerSocket(5000)
    println("Server started under localhost:5000")

    while (true) {
        val clientSocket = serverSocket.accept()
        println("Client connected")
        Thread { handleClient(clientSocket) }.start()
    }
}
