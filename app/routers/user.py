from fastapi import APIRouter, Depends
from httpx import AsyncClient

from app.dependencies.http_client import http_client

router = APIRouter(prefix="/users")


@router.get("/{manager_id}")
async def get_manager_info(
    manager_id: int,
    client: AsyncClient = Depends(http_client)
):
    res = await client.get(f"/entry/{manager_id}/")
    return res.json()
