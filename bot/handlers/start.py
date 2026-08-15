from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🆕 Start from scratch",
                callback_data="mode_roadmap"
            )
        ],
        [
            InlineKeyboardButton(
                "🔔 Just remind me",
                callback_data="mode_reminder"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🧠 How do you want to use LeetTracker?",
        reply_markup=reply_markup
    )
