import sys
import json
import capnp
capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')

def deserializeRequest(requestData):
    with capnpCalculatorSchema.Request.from_bytes(requestData) as request:
        operation = request.operation
        num1 = request.num1
        num2 = request.num2

        response = {
            "operation": operation,
            "num1": num1,
            "num2": num2
        }

        response_json = json.dumps(response)
        response_bytes = response_json.encode('utf-8')

        # Send the deserialized request back to the kotlin server in json format
        sys.stdout.buffer.write(response_bytes)
        sys.stdout.buffer.flush()

if __name__ == "__main__":
    try:
        requestData = sys.stdin.buffer.read()
        deserializeRequest(requestData)
    except Exception as e:
        error_response = {
            "error": str(e)
        }
        sys.stdout.buffer.write(json.dumps(error_response).encode('utf-8'))

