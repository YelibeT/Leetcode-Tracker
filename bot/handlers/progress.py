from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

from bot.services.api_client import get_user, update_user_position
from bot.services.roadmap import get_next_problem


async def mark_solved(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query
    await query.answer()

    telegram_id = update.effective_user.id

    try:
        user = await get_user(telegram_id)

        if not user:
            await query.edit_message_text(
                "You're not registered yet.\n\n"
                "Use /register to get started."
            )
            return

        roadmap = user.get("roadmap")
        current_position = user.get("current_position", 1)

        if not roadmap:
            await query.edit_message_text(
                "You don't have a roadmap selected."
            )
            return

        next_position = current_position + 1

        updated_user = await update_user_position(
            telegram_id,
            next_position
        )

        problem = get_next_problem(
            roadmap,
            next_position
        )

        if not problem:
            await query.edit_message_text(
                "🎉 You've completed this roadmap!\n\n"
                "Great work."
            )
            return

        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ I solved it",
                    callback_data="solved"
                )
            ]
        ]

        await query.edit_message_text(
            "🔥 Problem completed!\n\n"
            f"🧠 Next problem:\n\n"
            f"🧩 {problem.title}\n"
            f"🟢 {problem.difficulty}\n"
            f"📚 {problem.category}\n\n"
            f"🔗 https://leetcode.com/problems/{problem.slug}/",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    except Exception as e:
        print(f"Progress error: {e}")

        await query.edit_message_text(
            "Something went wrong while updating your progress."
        )
