import socket
import struct

def send_request(operation, num1, num2):
    """Sendet eine Anfrage an den Server und gibt das Ergebnis zurück."""
    # Verbindung zum Server herstellen
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8080))

    # Operation als UTF-String senden (Länge voranstellen)
    operation_bytes = operation.encode('utf-8')
    client_socket.sendall(struct.pack('!H', len(operation_bytes)))  # 2-Byte Länge
    client_socket.sendall(operation_bytes)  # Operation als UTF-8 senden

    # Anfrage senden: num1 und num2
    client_socket.sendall(struct.pack('!d', num1))  # Packe als Big-Endian Double
    client_socket.sendall(struct.pack('!d', num2))  # Packe als Big-Endian Double

    # Antwort empfangen
    result = client_socket.recv(8)
    if len(result) != 8:
        raise ValueError("Erwartete 8 Bytes für das Ergebnis, aber erhalten: " + str(len(result)))

    result = struct.unpack('!d', result)[0]  # Entpacke als Big-Endian Double

    client_socket.close()
    return result


def main():
    # Teste die Operationen
    operations = ['add', 'subtract', 'multiply', 'divide']
    num1 = 10.0
    num2 = 20.0

    for operation in operations:
        try:
            result = send_request(operation, num1, num2)
            print(f"Ergebnis der Operation '{operation}' mit {num1} und {num2}: {result}")
        except Exception as e:
            print(f"Fehler bei Operation '{operation}': {e}")

if __name__ == "__main__":
    main()
