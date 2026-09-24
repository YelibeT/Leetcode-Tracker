import asyncio

from bot.services.leetcode import get_recent_submissions


async def main():

    data = await get_recent_submissions(
        "Yelibe_Tsedeke"
    )

    print(data)


asyncio.run(main())