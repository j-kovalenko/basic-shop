import sqlalchemy
from .db_session import SqlAlchemyBase


class Acc(SqlAlchemyBase):
    __tablename__ = 'accessories'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    composition = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name_id = sqlalchemy.Column(sqlalchemy.String, nullable=True, unique=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)