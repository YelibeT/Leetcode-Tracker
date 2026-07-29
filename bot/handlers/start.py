from telegram import Update
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to LeetTracker 🚀\n\n"
        "Track your LeetCode journey with me.\n"
        "Use /register to connect your account."
    )