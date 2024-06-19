from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class ConfiguracionBD(BaseSettings):
    DATABASE_URL_MYSQL: str = "/api/v1"

    class Config:
        env_file = ".env"


settingsbd = ConfiguracionBD()
