import socket
import capnp

from fastapi import FastAPI, HTTPException

capnp.remove_import_hook()
capnpCalculatorSchema = capnp.load('calculator.capnp')

app = FastAPI()

# Definition of the routes for the different operations 
@app.get("/add")
def add(num1: float, num2: float):
    return sendRequest("add", num1, num2)

@app.get("/subtract")
def subtract(num1: float, num2: float):
    return sendRequest("subtract", num1, num2)

@app.get("/multiply")
def multiply(num1: float, num2: float):
    return sendRequest("multiply", num1, num2)

@app.get("/divide")
def divide(num1: float, num2: float):
    if num2 == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return sendRequest("divide", num1, num2)



def recv_all(sock, length):     # function to receive all bytes from the socket correctly
    data = bytearray()
    while len(data) < length:
        part = sock.recv(length - len(data))
        if not part:
            raise HTTPException(status_code=500, detail="Socket closed prematurely")
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
        # socketObject.connect(('localhost', 5000))    localhost for local use
        socketObject.connect(('server', 5000))        # server for docker use

        # Send the request to the server
        socketObject.sendall(len(requestBytes).to_bytes(4, byteorder='big'))
        socketObject.sendall(requestBytes)

        try:        # get the answer from the server
            responseLengthBytes = recv_all(socketObject, 4)
        except socket.timeout:
            raise HTTPException(status_code=500, detail="Did not receive response length within timeout")

        if len(responseLengthBytes) < 4:
            raise HTTPException(status_code=500, detail="Did not receive complete response length")
        responseLength = int.from_bytes(responseLengthBytes, byteorder='big')

        if responseLength <= 0:
            raise HTTPException(status_code=500, detail="Received invalid response length")
            
        try:
            responseBytes = recv_all(socketObject, responseLength)
        except socket.timeout:
            raise HTTPException(status_code=500, detail=f"Timeout while receiving response (expected {responseLength} bytes)")

        if len(responseBytes) != responseLength:
            raise HTTPException(status_code=500, detail=f"Expected {responseLength} bytes but received {len(responseBytes)} bytes")

        try:
            with capnpCalculatorSchema.Response.from_bytes(responseBytes) as response:      # decode the response of the server with capnp
                return {"result": response.result}

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error decoding server response: {e}")

