from fastapi import FastAPI

from api.routes import route_router
from common.database import Base, engine, SessionLocal
from common.settings import settings
from repositories.repo import RouteRepository
from services.logic import RouteService


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title="FastAPI Tech Task"
    )

    Base.metadata.create_all(bind=engine)

    route_repository = RouteRepository(SessionLocal)

    route_service = RouteService(route_repository)

    app.include_router(route_router)
    app.add_event_handler("startup", route_service.add_routes_to_db_from_csv)

    return app
