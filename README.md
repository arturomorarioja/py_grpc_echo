# Echo: gRPC Sample App
Example of a gRPC server and client using Python.

## Installation
1. Create a Python virtual environment: `python -m venv venv`
2. Activate the said environment:
    - Windows: `venv\Scripts\activate` or `.\venv\Scripts\Activate`
    - Linux/Mac: `source venv/bin/activate`
3. Install the dependencies: `pip install -r requirements.txt`

## Instructions
1. Generate `echo/echo_pb2.py` and `echo/echo_pb2_grpc.py` from `proto/echo.proto`:
```v
python -m grpc_tools.protoc -Iproto \
  --python_out=echo \
  --grpc_python_out=echo \
  proto/echo.proto
```
2. Run the server: `python echo/server.py`
3. In a different terminal, run the client: `python echo/client.py` 
4. Send a message from the client to the server. The server will acknowledge it
        
## Tools
Python

## Author
ChatGPT5, prompted by Arturo Mora-Rioja.