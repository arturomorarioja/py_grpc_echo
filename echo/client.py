import grpc
import echo_pb2 as pb
import echo_pb2_grpc as rpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = rpc.EchoStub(channel)

    message = input("Enter a message: ")
    request = pb.Message(text=message)
    response = stub.Say(request)

    print("Server replied:", response.text)
    channel.close()

if __name__ == "__main__":
    run()