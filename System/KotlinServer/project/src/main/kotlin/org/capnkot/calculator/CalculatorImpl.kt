package org.capnkot.calculator

import org.capnkot.calculator.interfaces.CalculatorInterface

import java.io.DataInputStream
import java.io.DataOutputStream
import java.net.ServerSocket
import java.net.Socket

// Interface für den Calculator
interface CalculatorInterface {
    fun add(num1: Double, num2: Double): Double
    fun subtract(num1: Double, num2: Double): Double
    fun multiply(num1: Double, num2: Double): Double
    fun divide(num1: Double, num2: Double): Double
}

// Implement the generated CalculatorInterface here
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
        if (num2 == 0.0) throw ArithmeticException("Division by zero")
        return num1 / num2
    }
}

fun handleClient(clientSocket: Socket) {
    val inputStream = DataInputStream(clientSocket.getInputStream())
    val outputStream = DataOutputStream(clientSocket.getOutputStream())

    try {
        val operation = inputStream.readUTF()
        val num1 = inputStream.readDouble()
        val num2 = inputStream.readDouble()

        println("Operation: $operation, num1: $num1, num2: $num2")  // Debug-Ausgabe

        val calculator: CalculatorInterface = CalculatorImpl()
        val result = when (operation) {
            "add" -> calculator.add(num1, num2)
            "subtract" -> calculator.subtract(num1, num2)
            "multiply" -> calculator.multiply(num1, num2)
            "divide" -> calculator.divide(num1, num2)
            else -> throw IllegalArgumentException("Unknown operation: $operation")
        }

        outputStream.writeDouble(result)
        outputStream.flush()
    } finally {
        clientSocket.close()
    }
}

fun main() {
    val serverSocket = ServerSocket(8080)
    println("Server started under localhost:8080")

    while (true) {
        val clientSocket = serverSocket.accept()
        println("Client verbunden")
        Thread { handleClient(clientSocket) }.start()
    }
}
