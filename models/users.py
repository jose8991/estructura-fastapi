from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from core.database import Base

class Area(Base):
    __tablename__ = "areas"
    id_area = Column(Integer, primary_key=True, index=True)
    nombre_area = Column(String(20), index=True)

class Rol(Base):
    __tablename__ = "roles"
    id_rol = Column(Integer, primary_key=True, index=True)
    nombre_rol = Column(String(20), index=True)

class Usuario(Base):
    __tablename__ = "usuarios"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(10), index=True)
    email = Column(String(20), unique=True, index=True)
    password = Column(String(100), unique=True, index=True)
    id_area = Column(Integer, ForeignKey("areas.id_area"))
    id_rol = Column(Integer, ForeignKey("roles.id_rol"))
    reset_password_token = Column(String(100), nullable=True)
    reset_password_expiry = Column(DateTime, nullable=True)
    area = relationship("Area")
    rol = relationship("Rol")
