from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from core.database import get_db
from models.users import Usuario
from core.security import  decode_access_token

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        user = db.query(Usuario).filter(Usuario.email == email).first()
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return user
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
def has_role(required_roles: list[str]):
    def role_checker(current_user: Usuario = Depends(get_current_user)):
        print(current_user.rol.nombre_rol)
        if current_user.rol.nombre_rol not in required_roles:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
        return current_user
    return role_checker

def has_area(required_areas: list[str]):
    def area_checker(current_user: Usuario = Depends(get_current_user)):
        if current_user.area.nombre_area not in required_areas:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
        return current_user
    return area_checker

def has_role_or_area(required_roles: list[str], required_areas: list[str]):
    def role_or_area_checker(current_user: Usuario = Depends(get_current_user)):
        if current_user.rol.nombre_rol not in required_roles and current_user.area.nombre_area not in required_areas:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Operation not permitted")
        return current_user
    return role_or_area_checker