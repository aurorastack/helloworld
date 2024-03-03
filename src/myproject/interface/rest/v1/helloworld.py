import logging

from aurorastack.core.error import *
from aurorastack.core.fastapi.api import BaseAPI, exception_handler
from fastapi import Request
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from myproject.service.helloworld import HelloWorldService

_LOGGER = logging.getLogger(__name__)

router = InferringRouter()


@cbv(router)
class HelloWorld(BaseAPI):
    service = "HelloWorld"

    @router.post("/sample/v1/say_hello")
    @exception_handler
    async def say_hello_post(self, request: Request):
        params, metadata = await self.parse_request(request)
        helloworld_svc: HelloWorldService = HelloWorldService(metadata)
        result = helloworld_svc.say_hello(params)
        return result
