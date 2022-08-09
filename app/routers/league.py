import asyncio

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

    result: list

    result = await asyncio.gather(*tasks)
    final_result = []
    for lst in result:
        final_result.extend(lst)

    return {
        "count": len(final_result),
        "managers": final_result
    }
