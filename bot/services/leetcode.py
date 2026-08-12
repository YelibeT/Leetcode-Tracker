import httpx


LEETCODE_API = "https://leetcode.com/graphql"


async def get_user_stats(username: str):

    query = """
    query userProfile($username: String!) {
        matchedUser(username: $username) {
            username
            profile {
                realName
                ranking
            }
            submitStats {
                acSubmissionNum {
                    difficulty
                    count
                }
            }
        }
    }
    """

    variables = {
        "username": username
    }

    async with httpx.AsyncClient() as client:
        response = await client.post(
            LEETCODE_API,
            json={
                "query": query,
                "variables": variables
            }
        )

        response.raise_for_status()

        data = response.json()

    user = data["data"]["matchedUser"]

    if not user:
        return None

    stats = user["submitStats"]["acSubmissionNum"]

    return {
        "username": user["username"],
        "real_name": user["profile"]["realName"],
        "ranking": user["profile"]["ranking"],
        "easy": next(
            item["count"] for item in stats
            if item["difficulty"] == "Easy"
        ),
        "medium": next(
            item["count"] for item in stats
            if item["difficulty"] == "Medium"
        ),
        "hard": next(
            item["count"] for item in stats
            if item["difficulty"] == "Hard"
        ),
        "total": next(
            item["count"] for item in stats
            if item["difficulty"] == "All"
        )
    }