from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler

from bot.services.api_client import create_user


USERNAME = 1


async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.callback_query:
        await update.callback_query.answer()
        await update.callback_query.edit_message_text(
            "Great choice! \n\n"
            "What's your LeetCode username?"
        )

    return USERNAME

async def save_username(update: Update, context: ContextTypes.DEFAULT_TYPE):

    username = update.message.text
    telegram_id = update.effective_user.id

    mode = context.user_data.get("mode")
    roadmap = context.user_data.get("roadmap")

    data = {
        "telegram_id": telegram_id,
        "leetcode_username": username,
        "mode": mode,
        "roadmap": roadmap
    }

    try:
        await create_user(data)

        await update.message.reply_text(
            "You're all set!\n\n"
            f"LeetCode: {username}\n"
            f"Mode: {mode}"
        )

        return ConversationHandler.END

    except Exception as e:
        print(f"Registration error: {e}")

        await update.message.reply_text(
            "Something went wrong while registering. Please try again."
        )

        return USERNAME
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Registration cancelled. Use /register to start again."
    )
    return ConversationHandler.END
