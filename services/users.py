from sqlalchemy.orm import Session
from models.users import Usuario, Area, Rol
from schemas.user import UserCreate
from core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    # Buscar el área por nombre
    area = db.query(Area).filter(Area.nombre_area == user.nombre_area).first()
    if not area:
        raise ValueError(f"Área no encontrada: {user.nombre_area}")

    # Buscar el rol por nombre
    rol = db.query(Rol).filter(Rol.nombre_rol == user.nombre_rol).first()
    if not rol:
        raise ValueError(f"Rol no encontrado: {user.nombre_rol}")

    hashed_password = get_password_hash(user.password)
    db_user = Usuario(
        nombre=user.nombre,
        email=user.email,
        password=hashed_password,
        id_area=area.id_area,
        id_rol=rol.id_rol
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()


def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()