import asyncio

import grpc

from hello_pb2 import HelloReply, HelloRequest
from hello_pb2_grpc import GreeterStub


async def run():
    async with grpc.aio.insecure_channel("localhost:5001") as channel:
        stub = GreeterStub(channel)
        res: HelloReply = await stub.SayHello(HelloRequest(name="x"))
    print(res.message)


asyncio.run(run())
