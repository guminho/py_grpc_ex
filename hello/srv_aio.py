from asyncio import BaseEventLoop

import grpc
from grpc.aio._server import Server

from hello_pb2 import HelloReply, HelloRequest
from hello_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class Greeter(GreeterServicer):
    async def SayHello(self, request: HelloRequest, context):
        return HelloReply(message=f"hello, {request.name}")


async def _serve(server: Server, address: str):
    port = server.add_insecure_port(address)
    await server.start()
    print("Server started on", port)
    await server.wait_for_termination()


def serve(server: Server, address: str):
    loop: BaseEventLoop = server._loop
    try:
        loop.run_until_complete(_serve(server, address))
    finally:
        loop.close()


server = grpc.aio.server()
add_GreeterServicer_to_server(Greeter(), server)

if __name__ == "__main__":
    serve(server, "[::]:5001")
