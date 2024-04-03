from sqlalchemy.orm import Session
from ..models.models import Route
from ..services.logic import RouteService


class RouteRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_route(self, route_data: dict):
        route = Route(**route_data)
        self.db.add(route)
        self.db.commit()
        self.db.refresh(route)
        return route

    def get_all_routes(self):
        return self.db.query(Route).all()

    def add_routes_to_db_from_csv(self, file_path: str):
        return RouteService(route_repository=self).add_routes_to_db_from_csv(file_path)

    def get_routes_by_id(self, route_id: int):
        return RouteService(route_repository=self).get_optimal_route(route_id)
