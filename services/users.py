from sqlalchemy.orm import Session
from models.users import Usuario
from schemas.user import UserCreate
from core.security import get_password_hash


def create_user(db: Session, user: UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = Usuario(
        email=user.email,
        nombre=user.nombre,
        password=hashed_password,
        id_area=user.id_area,
        id_rol=user.id_rol
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()


def get_user_by_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()