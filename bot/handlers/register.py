from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler

from bot.services.api_client import create_user
from bot.services.roadmap import get_next_problem


USERNAME = 1


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.callback_query:
        await update.callback_query.answer()

        await update.callback_query.edit_message_text(
            "Great choice!\n\n"
            "What's your LeetCode username?"
        )

    return USERNAME


async def save_username(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    username = update.message.text.strip()
    telegram_id = update.effective_user.id

    mode = context.user_data.get("mode")
    roadmap = context.user_data.get("roadmap")

    try:
        result = await create_user(
            telegram_id=telegram_id,
            leetcode_username=username,
            mode=mode,
            roadmap=roadmap
        )

        if result is None:
            await update.message.reply_text(
                "You're already registered."
            )
            return ConversationHandler.END

        await update.message.reply_text(
            "You're all set! 🎉\n\n"
            f"LeetCode: {username}\n"
            f"Mode: {mode}"
        )

        if mode == "roadmap" and roadmap:

            problem = get_next_problem(
                roadmap,
                1
            )

            if problem:

                keyboard = [
                    [
                        InlineKeyboardButton(
                            "✅ I solved it",
                            callback_data="solved"
                        )
                    ]
                ]

                await update.message.reply_text(
                    "🧠 Your first problem:\n\n"
                    f"🧩 {problem.title}\n"
                    f"🟢 {problem.difficulty}\n"
                    f"📚 {problem.category}\n\n"
                    f"🔗 https://leetcode.com/problems/{problem.slug}/",
                    reply_markup=InlineKeyboardMarkup(keyboard)
                )

        return ConversationHandler.END

    except Exception as e:
        print(f"Registration error: {e}")

        await update.message.reply_text(
            "Something went wrong while registering. "
            "Please try again."
        )

        return USERNAME


async def cancel(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Registration cancelled. Use /register to start again."
    )

    return ConversationHandler.END

