from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.services.api_client import create_user


USERNAME = 1


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            "Great choice! 🧠\n\n"
            "What's your LeetCode username?"
        )

    return USERNAME

async def save_username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    username = update.message.text.strip()
    telegram_id = update.effective_user.id

    user = await create_user(
        telegram_id,
        username
    )
    if not user:
        await update.message.reply_text(
            "You're already registered. User /profile to view your account.")
        return ConversationHandler.END
    await update.message.reply_text(
        f"Account registered!\n\n"
        f"LeetCode username: {user['leetcode_username']}"
    )
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Registration cancelled. Use /register to start again."
    )
    return ConversationHandler.END
