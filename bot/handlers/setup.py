from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def choose_mode(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "mode_roadmap":

        context.user_data["mode"] = "roadmap"

        keyboard = [
            [
                InlineKeyboardButton(
                    "🟢 NeetCode 75",
                    callback_data="roadmap_75"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔵 NeetCode 150",
                    callback_data="roadmap_150"
                )
            ]
        ]

        await query.edit_message_text(
            "Great! 🧠\n\n"
            "Which roadmap do you want to follow?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "mode_reminder":

        context.user_data["mode"] = "reminder"

        await query.edit_message_text(
            "🔔 Reminder mode selected!\n\n"
            "What's your LeetCode username?"
        )


async def choose_roadmap(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "roadmap_75":
        context.user_data["roadmap"] = "neetcode75"

    elif query.data == "roadmap_150":
        context.user_data["roadmap"] = "neetcode150"

    await query.edit_message_text(
        "Excellent choice! 🧠\n\n"
        "What's your LeetCode username?"
    )