import signal
from asyncio import BaseEventLoop

import grpc
from grpc.aio._server import Server

from hello_pb2 import HelloReply, HelloRequest
from hello_pb2_grpc import GreeterServicer, add_GreeterServicer_to_server


class Greeter(GreeterServicer):
    async def SayHello(self, request: HelloRequest, context):
        return HelloReply(message=f"hello, {request.name}")


def _raise_sigterm():
    raise SystemExit(1)


async def _serve(server: Server, address: str):
    port = server.add_insecure_port(address)
    await server.start()
    print("Server started on", port)
    await server.wait_for_termination()


def serve(server: Server, address: str, grace: float = 5):
    loop: BaseEventLoop = server._loop
    loop.add_signal_handler(signal.SIGTERM, _raise_sigterm)
    try:
        loop.run_until_complete(_serve(server, address))
    except (SystemExit, KeyboardInterrupt):
        pass
    finally:
        loop.run_until_complete(server.stop(grace))
        loop.remove_signal_handler(signal.SIGTERM)
        loop.close()


server = grpc.aio.server()
add_GreeterServicer_to_server(Greeter(), server)

if __name__ == "__main__":
    serve(server, "[::]:5001")
