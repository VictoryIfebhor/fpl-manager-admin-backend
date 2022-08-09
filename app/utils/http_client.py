from httpx import AsyncClient

# async def finish_tasks(
#     client: AsyncClient,
#     league_id: int,
#     first_page: int
# ):
#     tasks = []
#     for i in range(first_page, first_page + 5):
#         url = (
#             f"/leagues-classic/{league_id}/standings"
#             f"/?page_standings={i}&phase=1"
#         )
#         tasks.append(get_managers_per_page(client, url))
#     result = await asyncio.gather(*tasks, return_exceptions=True)
#     return result


async def get_managers_per_page(client: AsyncClient, url: str):
    res = await client.get(url)
    return res.json()["standings"]["results"]
