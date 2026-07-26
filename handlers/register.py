from telegram import Update
from telegram.ext import ContextTypes


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me your LeetCode username."
    )