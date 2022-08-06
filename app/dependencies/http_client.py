import httpx

BASE_URL = "https://fantasy.premierleague.com/api"


async def http_client():
    async with httpx.AsyncClient(base_url=BASE_URL) as client:
        yield client
