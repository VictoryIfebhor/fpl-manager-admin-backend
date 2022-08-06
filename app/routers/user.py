import httpx
from fastapi import APIRouter, Depends

from app.dependencies.http_client import http_client

router = APIRouter(prefix="/users")


@router.get("/{manager_id}")
async def get_manager_info(
    manager_id: int,
    client: httpx.AsyncClient = Depends(http_client)
):
    url = f"/entry/{manager_id}/"
    res = await client.get(url)
    return res.json()
