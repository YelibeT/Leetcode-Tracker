from telegram import Update
from telegram.ext import ContextTypes

from bot.services.api_client import get_user

async def profile(update:Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id=update.effective_user.id
    user=await get_user(telegram_id)

    if not user:
        await update.message.reply_text(
            "You havent registered yet."
            "User /register first"
        )
        return 
    await update.message.reply_text(
        f"Your profile\n\n"
        f"Leetcode Username: {user['leetcode_username']}"
    )
