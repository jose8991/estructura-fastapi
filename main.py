from fastapi import FastAPI
from routers import introduccion

app = FastAPI(
    title="herramientas fastapi",
    description="herramientas para el desarrollo de aplicaciones",
    version="0.1.0",
    contact={
        "name": "Jose Luis",
        "email": "joseluisgm98@proton.me"
    }
)


app.include_router(introduccion.router, tags=["Introduccion"], prefix="/introduccion")
