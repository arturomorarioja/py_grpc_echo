from concurrent.futures import ThreadPoolExecutor
import grpc
import echo_pb2 as pb
import echo_pb2_grpc as rpc

class EchoService(rpc.EchoServicer):
    def Say(self, request, context):
        print(f"Received: {request.text!r}")
        reply_text = f"You said: {request.text}"
        return pb.Message(text=reply_text)
    
def serve():
    server = grpc.server(ThreadPoolExecutor(max_workers=4))
    rpc.add_EchoServicer_to_server(EchoService(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    print("gRPC Echo server running on port 50051")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()