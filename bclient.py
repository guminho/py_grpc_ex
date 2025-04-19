import logging

import grpc

from rpc import helloworld_pb2_grpc
from rpc.helloworld_pb2 import HelloReply, HelloRequest


def run():
    with grpc.insecure_channel("localhost:7000") as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)

        rep: HelloReply = stub.SayHello(HelloRequest(name="you"))
        print(rep.message)

        for rep in stub.SayHelloStreamReply(HelloRequest(name="you")):
            print(rep.message)

        def _gen():
            for name in ("harry", "ron"):
                yield HelloRequest(name=name)

        for rep in stub.SayHelloBiStream(_gen()):
            print(rep.message)


if __name__ == "__main__":
    logging.basicConfig()
    run()
