import socket
import capnp

capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')


def recv_all(sock, length):     # function to receive all bytes from the socket correctly
    data = bytearray()
    while len(data) < length:
        part = sock.recv(length - len(data))
        if not part:
            raise ConnectionError("Socket closed prematurely")
        data.extend(part)
    return data

def sendRequest(operation, num1, num2):                     # function to send the request to the server
    request = capnpCalculatorSchema.Request.new_message()
    request.operation = operation
    request.num1 = num1
    request.num2 = num2
    requestBytes = request.to_bytes()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socketObject:
        socketObject.settimeout(5)
        # socketObject.connect(('localhost', 8080))    localhost for local use
        socketObject.connect(('server', 8080))        # server for docker use

        # Send the request to the server
        socketObject.sendall(len(requestBytes).to_bytes(4, byteorder='big'))
        socketObject.sendall(requestBytes)

        try:        # get the answer from the server
            responseLengthBytes = recv_all(socketObject, 4)
        except socket.timeout:
            print("Error: Did not receive response length within timeout")
            return

        if len(responseLengthBytes) < 4:
            print("Error: Did not receive complete response length")
            return

        responseLength = int.from_bytes(responseLengthBytes, byteorder='big')

        if responseLength <= 0:
            print("Error: Received invalid response length")
            return

        try:
            responseBytes = recv_all(socketObject, responseLength)
        except socket.timeout:
            print(f"Error: Timeout while receiving response (expected {responseLength} bytes)")
            return

        if len(responseBytes) != responseLength:
            print(f"Error: Expected {responseLength} bytes but received {len(responseBytes)} bytes")
            return

        try:
            with capnpCalculatorSchema.Response.from_bytes(responseBytes) as response:      # decode the response of the server with capnp
                print("The Response of the calculation is:", response.result)

        except Exception as e:
            print(f"Error decoding response: {e}")

def main():
    operations = [
        ("add", 5.0, 7.0),
        ("subtract", 5.0, 7.0),
        ("multiply", 5.0, 7.0),
        ("divide", 5.0, 7.0)
    ]

    for operation, num1, num2 in operations:
        print(f"\nSending {operation} request with num1={num1}, num2={num2}")
        sendRequest(operation, num1, num2)

if __name__ == "__main__":
    main()
