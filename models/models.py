from sqlalchemy import Column, Integer, Float, String, Boolean

from ..common.database import Base
from typing import List, Dict


class Route(Base):
    __tablename__ = 'route'

    id = Column(Integer, primary_key=True, index=True, nullable=False, unique=True)
    zip = Column(Integer, nullable=False, unique=True)
    lat = Column(Float, nullable=False)
    lng = Column(Float, nullable=False)
    city = Column(String)
    state_id = Column(String)
    state_name = Column(String)
    zcta = Column(Boolean, default='TRUE')
    parent_zcta = Column(String)
    population = Column(Integer)
    density = Column(Float)
    county_fips = Column(String)
    county_name = Column(String)
    county_weights = Dict[str, float]
    county_names_all = List[String]
    county_fips_all = List[String]
    imprecise = Column(Boolean, default='FALSE')
    military = Column(Boolean, default='FALSE')
    timezone = Column(String)
