import pandas as pd

from turtle import distance
from typing import List

from models.models import Route
from repositories.repo import RouteRepository


class RouteService:
    def __init__(self, route_repository: RouteRepository) -> None:
        self.route_repository = route_repository

    def add_routes_to_db_from_csv(self, file_path: str):
        data = pd.read_csv(file_path)
        data = data.to_dict(orient='records')

        for route in data:
            self.route_repository.create_route(route)

    def get_optimal_route(self, route_id: int) -> List[Route]:
        all_points = self.route_repository.get_all_routes()
        start_point = self.route_repository.get_routes_by_id(route_id)

        remaining_points = all_points.copy()
        remaining_points.remove(start_point)

        path = [start_point]
        current_point = start_point

        while remaining_points:
            nearest_point = min(remaining_points, key=lambda x: distance(x, current_point))
            path.append(nearest_point)
            current_point = nearest_point
            remaining_points.remove(nearest_point)

        return path
