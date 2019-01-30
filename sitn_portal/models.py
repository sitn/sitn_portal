from sqlalchemy import (
    Column,
    Sequence,
    Integer,
    Text,
    String,
    Unicode,
    Boolean,
    ForeignKey,
    Float)

from sqlalchemy.orm import relationship, backref, deferred

import sqlahelper
DBSession = sqlahelper.get_session()
Base = sqlahelper.get_base()

# class User(Base):
    #  __tablename__ = 'users'
    # __table_args__ = {'schema': 'user_administration', 'autoload': True}
    # id = Column(Integer, primary_key=True)

class Documents(Base):
    __tablename__ = 'documents'
    __table_args__ = {'schema': 'crdppf', 'autoload': True}
    docid = Column(String, primary_key=True)
    legalstate = Column(Integer, ForeignKey('crdppf.vl_legalstate.id'), nullable=False)
    legalstates = relationship("Legalstates", lazy="joined")
    doctype = Column(Integer, ForeignKey('crdppf.vl_doctype.id'), nullable=False)
    doctypes = relationship("DocumentType", lazy="joined")

class Legalstates(Base):
    __tablename__ = 'vl_legalstate'
    __table_args__ = {'schema': 'crdppf'}
    id = Column(String, primary_key=True)
    value = Column(Unicode)

class DocumentType(Base):
    __tablename__ = 'vl_doctype'
    __table_args__ = {'schema': 'crdppf'}
    id = Column(String, primary_key=True)
    value = Column(Unicode)

class Municipalities(Base):
    __tablename__ = 'la3_limites_communales'
    __table_args__ = {'schema': 'general'}
    idobj = Column(String, primary_key=True)
    comnom = Column(Unicode)
    numcom = Column(Integer, nullable=False)
    nufeco = Column(Integer, nullable=False)
    image2 = Column(String)
