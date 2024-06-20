from fastapi import FastAPI
from core.database import engine, Base, test_db_connection
from routers import users, password_reset

# Crear las tablas en la base de datos
def create_tables():
    Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="herramientas fastapi",
    description="herramientas para el desarrollo de aplicaciones",
    version="0.1.0",
    contact={
        "name": "Jose Luis",
        "email": "joseluisgm98@proton.me"
    }
)

# Probar la conexión a la base de datos al iniciar la aplicación
test_db_connection()

# Crear las tablas al iniciar la aplicación
create_tables()

# Incluir el router para las rutas de autenticación
app.include_router(users.router, prefix="/users", tags=["auth"])
app.include_router(password_reset.router, tags=["Password Reset"], prefix="/auth")

# Aquí puedes incluir otras rutas como la de introducción
# app.include_router(introduccion.router, tags=["Introducción"], prefix="/introduccion")
