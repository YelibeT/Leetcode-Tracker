from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.services.api_client import create_user


USERNAME = 1


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me your LeetCode username."
    )

    return USERNAME

async def save_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    telegram_id = update.effective_user.id

    try:
        user = await create_user(
            telegram_id,
            username
        )
        await update.message.reply_text(
            f"Account registered!\n\n"
            f"LeetCode username: {user['leetcode_username']}"
        )

    except Exception:
        await update.message.reply_text(
            "Something went wrong while registering."
        )

    return ConversationHandler.END