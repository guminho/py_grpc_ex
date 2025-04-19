import logging
import time
from concurrent import futures
from typing import Iterator as Iter

import grpc

from rpc import helloworld_pb2_grpc
from rpc.helloworld_pb2 import HelloReply, HelloRequest


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(self, request: HelloRequest, context):
        time.sleep(0.01)
        return HelloReply(message=f"Hello, {request.name}")

    def SayHelloStreamReply(self, request: HelloRequest, context):
        time.sleep(0.01)
        yield HelloReply(message=f"one, {request.name}")
        yield HelloReply(message=f"two, {request.name}")

    def SayHelloBiStream(self, request_iterator: Iter[HelloRequest], context):
        for request in request_iterator:
            time.sleep(0.01)
            yield HelloReply(message=f"Hello, {request.name}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port("[::]:7000")
    server.start()
    print("Server started, listening on", port)
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
