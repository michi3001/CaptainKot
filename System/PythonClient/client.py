import argparse
import asyncio
import capnp
import calculator_capnp  # Die generierte Datei

def main():
    # Verbindung zum Server herstellen
    import socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Erstellen und Senden einer Anfrage
    request = calculator_capnp.Calculator.AddRequest.new_message(num1=10.0, num2=20.0)
    client_socket.sendall(request.to_bytes())

    # Empfangen und Verarbeiten der Antwort
    response_bytes = client_socket.recv(1024)
    response = calculator_capnp.Calculator.AddResponse.from_bytes(response_bytes)
    print(f"Ergebnis der Addition: {response.result}")

    client_socket.close()

if __name__ == "__main__":
    main()
