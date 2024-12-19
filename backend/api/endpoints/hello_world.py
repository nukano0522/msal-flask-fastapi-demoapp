from typing import Dict, Union

from fastapi import APIRouter, Security, Request
from fastapi_azure_auth.user import User

from backend.api.dependencies import azure_scheme

router = APIRouter()


@router.get(
    "/hello",
    # response_model=HelloWorldResponse,
    summary="Say hello",
    name="hello_world",
    operation_id="helloWorld",
    dependencies=[Security(azure_scheme)],
)
async def world(request: Request):
    """
    Wonder who we say hello to?
    """
    user: User = request.state.user
    # return {'hello': 'world', 'user': user}
    return {"message": "Hello World!!!", "user": user}


# async def world(request: Request) -> Dict[str, Union[str, User]]:
#     """
#     Wonder who we say hello to?
#     """
#     user: User = request.state.user
#     return {'hello': 'world', 'user': user}
