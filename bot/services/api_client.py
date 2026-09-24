import httpx


API_URL = "http://127.0.0.1:8000"


async def create_user(
    telegram_id: int,
    leetcode_username: str,
    mode: str | None = None,
    roadmap: str | None = None
):
    async with httpx.AsyncClient() as client:

        response = await client.post(
            f"{API_URL}/users",
            json={
                "telegram_id": telegram_id,
                "leetcode_username": leetcode_username,
                "mode": mode,
                "roadmap": roadmap
            }
        )

        if response.status_code == 400:
            return None

        response.raise_for_status()

        return response.json()


async def get_user(
    telegram_id: int
):
    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{API_URL}/users/{telegram_id}"
        )

        if response.status_code == 404:
            return None

        response.raise_for_status()

        return response.json()


async def get_users():
    async with httpx.AsyncClient() as client:

        response = await client.get(
            f"{API_URL}/users"
        )

        response.raise_for_status()

        return response.json()


async def update_user_position(
    telegram_id: int,
    position: int
):
    async with httpx.AsyncClient() as client:

        response = await client.put(
            f"{API_URL}/users/{telegram_id}/position",
            params={
                "position": position
            }
        )

        response.raise_for_status()

        return response.json()

