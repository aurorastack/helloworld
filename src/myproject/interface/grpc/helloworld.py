from aurorastack.api.sample.v1 import helloworld_pb2, helloworld_pb2_grpc
from aurorastack.core.pygrpc import BaseAPI

from myproject.service.helloworld import HelloWorldService


class HelloWorld(BaseAPI, helloworld_pb2_grpc.HelloWorldServicer):
    pb2 = helloworld_pb2
    pb2_grpc = helloworld_pb2_grpc

    def say_hello(self, request, context):
        params, metadata = self.parse_request(request, context)
        helloworld_svc = HelloWorldService(metadata)
        response: dict = helloworld_svc.say_hello(params)
        return self.dict_to_message(response)
