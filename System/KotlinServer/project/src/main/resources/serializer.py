# serializer.py
import capnp
import sys
capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')

def serializeResponse(result):
    # Create the serialized response
    response = capnpCalculatorSchema.Response.new_message()
    response.result = result

    response_bytes = response.to_bytes()

    # Write the serialized response
    sys.stdout.buffer.write(response_bytes)
    sys.stdout.flush()

if __name__ == "__main__":
    try:
        # Read the result which comes from the kotlin server
        result = float(sys.stdin.read().strip())
        serializeResponse(result)
    except Exception as e:
        print(f"Error in serializer: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with error code 1
