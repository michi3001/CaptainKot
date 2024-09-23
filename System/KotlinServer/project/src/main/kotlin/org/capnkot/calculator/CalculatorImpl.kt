package org.capnkot.calculator

import java.io.DataInputStream
import java.io.DataOutputStream
import java.net.ServerSocket
import java.net.Socket

// Einfache Implementierung des Calculator
// Diese Funktionen sollen später den Glue Code der von CapnProto erzeugt wird überschreiben
// Capn Proto ist dann für das Kommunikationsprotokoll zwischen Python Client und Kotlin Server zuständig

// Python Client nutzt die Funktionen vom CapnProto Schema in dem in den Request den dieser sendet der
// Capn Proto Glue Code miteingebunden wird
// Der Kotlin Server antwortet dann darauf indem er das Ergebnis der überschriebenen Methode richtig zurückgibt
class CalculatorImpl {

    fun add(num1: Double, num2: Double): Double {
        return num1 + num2
    }

    fun subtract(num1: Double, num2: Double): Double {
        return num1 - num2
    }

    fun multiply(num1: Double, num2: Double): Double {
        return num1 * num2
    }

    fun divide(num1: Double, num2: Double): Double {
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

        val calculator = CalculatorImpl()
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
    println("Server gestartet auf Port 8080")

    while (true) {
        val clientSocket = serverSocket.accept()
        println("Client verbunden")
        Thread { handleClient(clientSocket) }.start()
    }
}
