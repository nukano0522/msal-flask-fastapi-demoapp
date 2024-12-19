from backend.api.endpoints import hello_world, get_members, get_organization
from fastapi import APIRouter

api_router_hello = APIRouter(tags=["hello"])
api_router_hello.include_router(hello_world.router)

api_router_get_organization = APIRouter(tags=["organization"])
api_router_get_organization.include_router(get_organization.router)

api_router_get_members = APIRouter(tags=["organization"])
api_router_get_members.include_router(get_members.router)
