from concurrent.futures import ThreadPoolExecutor

import grpc
from grpc._server import _Server

from hello_pb2 import HelloReply, HelloRequest
from hello_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class Greeter(GreeterServicer):
    def SayHello(self, request: HelloRequest, context):
        return HelloReply(message=f"hello, {request.name}")


def serve(server: _Server, address: str):
    port = server.add_insecure_port(address)
    server.start()
    print("Server started on", port)
    server.wait_for_termination()


server = grpc.server(ThreadPoolExecutor(10))
add_GreeterServicer_to_server(Greeter(), server)

if __name__ == "__main__":
    serve(server, "[::]:5001")
