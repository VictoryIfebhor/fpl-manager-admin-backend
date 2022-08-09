from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from app.routers import league, user

app = FastAPI()


@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse("/docs")

app.include_router(user.router)
app.include_router(league.router)
