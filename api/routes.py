from fastapi import APIRouter

from models.models import Route
from ..repositories.repo import RouteRepository
from ..services.logic import RouteService
from ..common.database import get_db

route_router = APIRouter()
route_repository = RouteRepository(db=get_db())


@route_router.post("/routes", response_model=Route)
def create_route(route_data: Route):
    created_route = route_repository.create_route(route_data.dict())
    return created_route


@route_router.get("/routes/{route_id}", response_model=Route)
def get_route(route_id: int):
    route_path = RouteService(route_repository).get_optimal_route(route_id)
    return route_path
