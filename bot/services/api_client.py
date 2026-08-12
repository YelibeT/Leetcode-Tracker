import httpx

API_URL="http://127.0.0.1:8000"

async def create_user(telegram_id: int, leetcode_username:str):
    async with httpx.AsyncClient() as client:
        response=await client.post(
            f"{API_URL}/users",
            json={
                "telegram_id":telegram_id,
                "leetcode_username":leetcode_username
            }
        )

        response.raise_for_status()

        return response.json()