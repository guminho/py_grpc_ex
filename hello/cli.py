import grpc

from hello_pb2 import HelloReply, HelloRequest
from hello_pb2_grpc import GreeterStub


def run():
    with grpc.insecure_channel("localhost:5001") as channel:
        stub = GreeterStub(channel)
        res: HelloReply = stub.SayHello(HelloRequest(name="x"))
    print(res.message)


run()
