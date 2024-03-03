import logging

from aurorastack.core.error import *
from aurorastack.core.service import *
from aurorastack.core.service.utils import *

from myproject.model.helloworld.response import HelloReply

_LOGGER = logging.getLogger(__name__)


@authentication_handler
@authorization_handler
@mutation_handler
@event_handler
class HelloWorldService(BaseService):
    resource = "HelloWorld"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @transaction(
        permission="helloworld:HelloWorld.read",
        role_types=["TENANT_ADMIN", "WORKSPACE_OWNER", "WORKSPACE_MEMBER"],
    )
    @convert_model
    # def say_hello(self, params: HelloRequest) -> HelloReply:
    def say_hello(self, params):
        """Search resources
        Args:
            params (ResourceSearchRequest): {
                'name': 'str',     # required
            }
        Returns:
            HelloReply:
        """
        msg = {"message": f"hello {params.get('name','No name')}"}
        return HelloReply(**msg)
