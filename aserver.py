import asyncio
import logging
from typing import AsyncIterator as AIter

import grpc

from rpc import helloworld_pb2_grpc
from rpc.helloworld_pb2 import HelloReply, HelloRequest


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    async def SayHello(self, request: HelloRequest, context):
        await asyncio.sleep(0.01)
        return HelloReply(message=f"Hello, {request.name}")

    async def SayHelloStreamReply(self, request: HelloRequest, context):
        await asyncio.sleep(0.01)
        yield HelloReply(message=f"one, {request.name}")
        yield HelloReply(message=f"two, {request.name}")

    async def SayHelloBiStream(self, request_iterator: AIter[HelloRequest], context):
        async for request in request_iterator:
            await asyncio.sleep(0.01)
            yield HelloReply(message=f"Hello, {request.name}")


async def serve():
    server = grpc.aio.server()
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    port = server.add_insecure_port("[::]:7000")
    await server.start()
    print("Server started, listening on", port)
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(serve())
