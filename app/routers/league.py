import asyncio
import itertools

from fastapi import APIRouter, Depends
from httpx import AsyncClient

from app.dependencies.http_client import http_client
from app.utils.http_client import get_managers_per_page

router = APIRouter(prefix="/leagues")


@router.get("/{league_id}")
async def get_managers(
    league_id: int,
    client: AsyncClient = Depends(http_client)
):
    tasks = []
    for i in range(1, 21):
        url: str = (
            f"/leagues-classic/{league_id}/standings"
            f"/?page_standings={i}&phase=1"
        )
        tasks.append(get_managers_per_page(client, url))
    result = await asyncio.gather(*tasks)
    list(itertools.chain.from_iterable(result))

    return list(itertools.chain.from_iterable(result))
