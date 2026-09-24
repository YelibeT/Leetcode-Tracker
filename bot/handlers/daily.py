from telegram.ext import ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from bot.services.api_client import (
    get_users,
    update_user_position
)

from bot.services.leetcode import (
    get_recent_submissions
)

from bot.services.roadmap import (
    get_next_problem
)


def problem_keyboard():

    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "🔄 Check if I solved it",
                callback_data="check_solved"
            )
        ]
    ])


async def send_daily_problem(
    context: ContextTypes.DEFAULT_TYPE
):

    try:
        users = await get_users()

        for user in users:

            if user.get("mode") != "roadmap":
                continue

            roadmap = user.get("roadmap")
            position = user.get(
                "current_position",
                1
            )

            telegram_id = user["telegram_id"]
            username = user["leetcode_username"]

            if not roadmap:
                continue

            submissions = await get_recent_submissions(
                username
            )

            submission_data = submissions.get(
                "data",
                {}
            )

            recent_submissions = submission_data.get(
                "recentAcSubmissionList",
                []
            )

            solved_slugs = {
                submission["titleSlug"]
                for submission in recent_submissions
            }

            while True:

                problem = get_next_problem(
                    roadmap,
                    position
                )

                if not problem:
                    await context.bot.send_message(
                        chat_id=telegram_id,
                        text=(
                            "🎉 Congratulations!\n\n"
                            "You've completed your roadmap!"
                        )
                    )

                    break

                if problem.slug in solved_slugs:

                    position += 1

                    await update_user_position(
                        telegram_id,
                        position
                    )

                    continue

                await context.bot.send_message(
                    chat_id=telegram_id,
                    text=(
                        "🧠 Your daily LeetCode problem:\n\n"
                        f"🧩 {problem.title}\n"
                        f"🟢 {problem.difficulty}\n"
                        f"📚 {problem.category}\n\n"
                        f"🔗 https://leetcode.com/problems/"
                        f"{problem.slug}/"
                    ),
                    reply_markup=problem_keyboard()
                )

                break

    except Exception as e:

        print(
            f"Daily problem error: {e}"
        )
