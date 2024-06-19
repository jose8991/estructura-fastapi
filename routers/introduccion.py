from fastapi import APIRouter

router = APIRouter()


@router.get(
        "/",
        tags=["Introduccion"],
        summary="Saludo de bienvenida",
        description="Saludo de bienvenida a la aplicacion",
        response_description="Saludo de bienvenida",
)
def get_hola_mundi():
    return {"Hello": "World"}
