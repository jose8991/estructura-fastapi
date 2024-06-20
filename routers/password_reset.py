from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from core.database import get_db
from models.users import Usuario
from core.security import get_password_hash
from core.email import send_email
from datetime import datetime, timedelta
import uuid

router = APIRouter()

@router.post("/forgot-password")
def forgot_password(email: str, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.email == email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email not found")

    token = str(uuid.uuid4())
    expiry = datetime.utcnow() + timedelta(hours=1)

    user.reset_password_token = token
    user.reset_password_expiry = expiry
    db.commit()

    reset_link = f"http://your-app-url/reset-password?token={token}"
    email_body = f"Click the following link to reset your password: {reset_link}"
    send_email(user.email, "Password Reset Request", email_body)

    return {"msg": "Password reset email sent"}

@router.post("/reset-password")
def reset_password(token: str, new_password: str, db: Session = Depends(get_db)):
    user = db.query(Usuario).filter(Usuario.reset_password_token == token).first()
    if user is None or user.reset_password_expiry < datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid or expired token")

    user.password = get_password_hash(new_password)
    user.reset_password_token = None
    user.reset_password_expiry = None
    db.commit()

    return {"msg": "Password reset successfully"}
q
