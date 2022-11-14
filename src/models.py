import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique= True, primary_key=True)
    username = Column(String(250), unique= True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email= Column(String(100), unique =True, nullable=False)
    publicacion= relationship('Publicacion')
    seguidores = relationship('Seguidores')
    comentarios = relationship('Comentarios')

class Media(Base):
    __tablename__ = 'Media'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, unique=True, primary_key=True)
    type = Column(Enum("video","image"))
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, nullable=False, ForeignKey=(publicacion.id))

class Publicacion(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, unique=True, primary_key=True)
    user_id = Column(Integer, nullable=False, ForeignKey=(user.id))
   

class Comentarios(Base):
    __tablename__ = 'comentarios'
    id = Column(Integer, unique=True, primary_key=True)
    comentario_texto = Column(String(250), nullable=False)
    autor_id = Column(Integer, nullable=False, ForeignKey=(user.id))
    post_id = Column(Integer, nullable=False, ForeignKey=(post.id) )
   

class Seguidor(Base):
    __tablename__ = 'publicacion'
    id = Column(Integer, unique=True, primary_key=True)
    user_from_id = Column(Integer, nullable=False, ForeignKey=(user.id))
    user_to_id = Column(Integer, nullable=False, ForeignKey=(user.id))
   


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
 
