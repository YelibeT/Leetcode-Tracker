from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.services.api_client import (
    get_user,
    update_user_position
)

from bot.services.leetcode import (
    get_recent_submissions
)

from bot.services.roadmap import (
    get_next_problem
)


async def check_solved(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer(
        "Checking LeetCode..."
    )

    telegram_id = update.effective_user.id

    try:

        user = await get_user(
            telegram_id
        )

        if not user:

            await query.edit_message_text(
                "You're not registered yet."
            )

            return

        roadmap = user.get("roadmap")

        position = user.get(
            "current_position",
            1
        )

        username = user.get(
            "leetcode_username"
        )

        if not roadmap:

            await query.edit_message_text(
                "You don't have a roadmap selected."
            )

            return

        submissions = await get_recent_submissions(
            username
        )

        recent_submissions = submissions.get(
            "data",
            {}
        ).get(
            "recentAcSubmissionList",
            []
        )

        solved_slugs = {
            submission["titleSlug"]
            for submission in recent_submissions
        }

        problem = get_next_problem(
            roadmap,
            position
        )

        if not problem:

            await query.edit_message_text(
                "🎉 You've completed your roadmap!"
            )

            return

        if problem.slug not in solved_slugs:

            await query.edit_message_text(
                "Not solved yet 👀\n\n"
                f"🧩 {problem.title}\n\n"
                "Solve it on LeetCode, then "
                "tap the button again."
            )

            keyboard = InlineKeyboardMarkup([
                [
                    InlineKeyboardButton(
                        "🔄 Check again",
                        callback_data="check_solved"
                    )
                ]
            ])

            await query.edit_message_reply_markup(
                reply_markup=keyboard
            )

            return

        position += 1

        await update_user_position(
            telegram_id,
            position
        )

        next_problem = get_next_problem(
            roadmap,
            position
        )

        if not next_problem:

            await query.edit_message_text(
                "🎉 You completed the roadmap!"
            )

            return

        keyboard = InlineKeyboardMarkup([
            [
                InlineKeyboardButton(
                    "🔄 Check if I solved it",
                    callback_data="check_solved"
                )
            ]
        ])

        await query.edit_message_text(
            "✅ Solved!\n\n"
            "🔥 Next problem:\n\n"
            f"🧩 {next_problem.title}\n"
            f"🟢 {next_problem.difficulty}\n"
            f"📚 {next_problem.category}\n\n"
            f"🔗 https://leetcode.com/problems/"
            f"{next_problem.slug}/",
            reply_markup=keyboard
        )

    except Exception as e:

        print(
            f"Check solved error: {e}"
        )

        await query.edit_message_text(
            "Something went wrong while checking "
            "your LeetCode submission."
        )
