import sys
import json
import capnp
capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')

def main():
    # Alle Ausgaben zu Debugging-Zwecken auf stderr
    try:
        # Lies die Binärdaten von der Standardeingabe
        request_data = sys.stdin.buffer.read()

        # Verwende einen Kontextmanager, um die Nachricht korrekt zu deserialisieren
        with capnpCalculatorSchema.Request.from_bytes(request_data) as request:
            operation = request.operation
            num1 = request.num1
            num2 = request.num2

            # Erstelle die Antwort als Dictionary
            response = {
                "operation": operation,
                "num1": num1,
                "num2": num2
            }

            # Serialisiere die Antwort als JSON
            response_json = json.dumps(response)
            response_bytes = response_json.encode('utf-8')  # Konvertiere zu Bytes

            # Sende die Antwort an stdout zurück
            sys.stdout.buffer.write(response_bytes)
            sys.stdout.buffer.flush()  # Sicherstellen, dass die Ausgabe sofort gesendet wird

    except Exception as e:
        # Im Fehlerfall eine JSON-Antwort mit dem Fehler zurückgeben
        error_response = {
            "error": str(e)
        }
        sys.stdout.buffer.write(json.dumps(error_response).encode('utf-8'))

if __name__ == "__main__":
    main()
