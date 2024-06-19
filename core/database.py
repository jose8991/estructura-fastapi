from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settingsbd

DATABASE_URL = settingsbd.DATABASE_URL_MYSQL

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Función para probar la conexión a la base de datos
def test_db_connection():
    try:    
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("Conexión a la base de datos exitosa.")
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")

# Llama a la función para probar la conexión al iniciar el módulo
#test_db_connection()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()
