from fastapi import APIRouter  # type: ignore

route = APIRouter()


@route.get("/main", status_code=200)
async def main_route():
    return {
        "Ceci est la route principale"
    }