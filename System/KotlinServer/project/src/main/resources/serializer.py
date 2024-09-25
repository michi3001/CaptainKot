# serializer.py
import capnp
import sys
capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')

def serialize_response(result):
    response = capnpCalculatorSchema.Response.new_message()
    response.result = result

    response_bytes = response.to_bytes()

    # Ausgabe in den Fehlerstrom
    sys.stdout.buffer.write(response_bytes)
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        # Lese das Ergebnis von stdin
        result = float(sys.stdin.read().strip())
        serialize_response(result)
    except Exception as e:
        print(f"Error in serializer: {e}", file=sys.stderr)
        sys.exit(1)  # Beende das Skript mit einem Fehlercode
