from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from schemas.user import UserCreate, User
from services.users import create_user, get_user_by_email
from auth.dependencies import get_current_user
from auth.dependencies import has_role, has_area, has_role_or_area
from core.database import get_db
from core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=User)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return create_user(db=db, user=user)

@router.post("/token")
def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password
    print(email, password)
    user = get_user_by_email(db, email=form_data.username)
    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={
        "sub": user.email,
        "id_area": user.id_area,
        "id_rol": user.id_rol
    })
    return {"access_token": access_token, 
            "token_type": "bearer",
            "id_area": user.id_area,
            "id_rol": user.id_rol
            }

@router.get("/users/me", response_model=User)
def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user


@router.post("/register-user", dependencies=[Depends(has_role(["root", "administrador"]))])
def register_user(db: Session = Depends(get_db)):
    # Lógica para registrar usuario
    return {"message": "User registered successfully"}

@router.get("/protected-rol", dependencies=[Depends(has_role(["infraestructura", "administrador"]))])
def register_user(db: Session = Depends(get_db)):
    # Lógica para registrar usuario
    return {"message": "User registered successfully"}


@router.get("/protected-area", dependencies=[Depends(has_area(["HR", "IT"]))])
def protected_area(db: Session = Depends(get_db)):
    # Lógica para acceder a áreas protegidas
    return {"message": "Access granted"}

@router.get("/protected-role-area", dependencies=[Depends(has_role_or_area(["admin"], ["IT"]))])
def protected_role_area(db: Session = Depends(get_db)):
    # Lógica para roles y áreas protegidas
    return {"message": "Access granted for admin in IT"}