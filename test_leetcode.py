import asyncio

from bot.services.leetcode import get_user_stats


async def main():
    data = await get_user_stats("Yelibe_Tsedeke")
    print(data)


asyncio.run(main())