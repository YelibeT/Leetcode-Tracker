from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from bot.handlers.register import USERNAME

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
            ],
            [
                InlineKeyboardButton(
                    "⬅️ Back",
                    callback_data="back_to_mode"
                ),
                InlineKeyboardButton(
                    "❌ Cancel",
                    callback_data="cancel_setup"
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

        return USERNAME

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

    return USERNAME

async def go_back(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    current_step = context.user_data.get("step")

    if current_step == "username":

        # If they came from roadmap, go back to roadmap selection
        if context.user_data.get("mode") == "roadmap":

            context.user_data["step"] = "roadmap"

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
                ],
                [
                    InlineKeyboardButton(
                        "⬅️ Back",
                        callback_data="back"
                    ),
                    InlineKeyboardButton(
                        "❌ Cancel",
                        callback_data="cancel_setup"
                    )
                ]
            ]

            await query.edit_message_text(
                "Which roadmap do you want to follow?",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

            return

        # If they came from reminder, go back to mode
        elif context.user_data.get("mode") == "reminder":

            context.user_data["step"] = "mode"

            keyboard = [
                [
                    InlineKeyboardButton(
                        "🧠 Roadmap",
                        callback_data="mode_roadmap"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔔 Reminder",
                        callback_data="mode_reminder"
                    )
                ]
            ]

            await query.edit_message_text(
                "How do you want to use LeetTracker?",
                reply_markup=InlineKeyboardMarkup(keyboard)
            )

            return

    elif current_step == "roadmap":

        context.user_data["step"] = "mode"

        keyboard = [
            [
                InlineKeyboardButton(
                    "🧠 Roadmap",
                    callback_data="mode_roadmap"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔔 Reminder",
                    callback_data="mode_reminder"
                )
            ]
        ]

        await query.edit_message_text(
            "How do you want to use LeetTracker?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

async def cancel_setup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    context.user_data.clear()

    await query.edit_message_text(
        "❌ Setup cancelled.\n\n"
        "Use /start whenever you're ready."
    )