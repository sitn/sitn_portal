from sqlalchemy import (
    Column,
    Integer,
)

import sqlahelper
DBSession = sqlahelper.get_session()
Base = sqlahelper.get_base()

# class User(Base):
    #  __tablename__ = 'users'
    # __table_args__ = {'schema': 'user_administration', 'autoload': True}
    # id = Column(Integer, primary_key=True)
