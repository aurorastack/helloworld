from aurorastack.core.pygrpc.server import GRPCServer

from myproject.interface.grpc.helloworld import HelloWorld

_all_ = ["app"]

app = GRPCServer()
app.add_service(HelloWorld)
