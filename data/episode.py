import datetime
from typing import List, Optional
import sqlalchemy as sa

from data.modelbase import SqlAlchemyBase


class Episode(SqlAlchemyBase):

    __tablename__ = "episodes"

    id: int = sa.Column(sa.Integer, primary_key=True, autoincrement=True)

    season: int = sa.Column(sa.Integer)
    episode_number: int = sa.Column(sa.Integer, index=True)
    episode_title: str = sa.Column(sa.String, index=True)
    youtube_url: str = sa.Column(sa.String, nullable=True)
    record_date: datetime.date = sa.Column(sa.String, index=True)
    record_date_converted: datetime.date = sa.Column(sa.String, index=True)
    publish_date: datetime.date = sa.Column(sa.String, index=True)
    publish_date_converted: datetime.date = sa.Column(sa.String, index=True)
    published: int = sa.Column(sa.Integer)
    episode_length: int = sa.Column(sa.Integer)
    episode_length_string: str = sa.Column(sa.String)
    host_url: str = sa.Column(sa.String, nullable=True)
