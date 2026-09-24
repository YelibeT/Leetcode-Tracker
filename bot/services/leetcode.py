import httpx


LEETCODE_URL = "https://leetcode.com/graphql/"


HEADERS = {
    "Content-Type": "application/json",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    ),
    "Referer": "https://leetcode.com/",
    "Origin": "https://leetcode.com"
}


async def get_user_stats(
    username: str
):

    query = """
    query getUserProfile($username: String!) {
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
            LEETCODE_URL,
            headers=HEADERS,
            json={
                "query": query,
                "variables": variables
            }
        )

        response.raise_for_status()

        return response.json()


async def get_recent_submissions(
    username: str
):

    query = """
    query recentAcSubmissions($username: String!, $limit: Int!) {
        recentAcSubmissionList(
            username: $username
            limit: $limit
        ) {
            id
            title
            titleSlug
            timestamp
        }
    }
    """

    variables = {
        "username": username,
        "limit": 20
    }

    async with httpx.AsyncClient() as client:

        response = await client.post(
            LEETCODE_URL,
            headers=HEADERS,
            json={
                "operationName": "recentAcSubmissions",
                "query": query,
                "variables": variables
            }
        )

        response.raise_for_status()

        return response.json()
