from telegram import Update
from telegram.ext import ContextTypes

from bot.services.api_client import get_user
from bot.services.leetcode import get_user_stats


async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    telegram_id = update.effective_user.id

    user = await get_user(telegram_id)

    if not user:
        await update.message.reply_text(
            "❌ You haven't registered yet.\n"
            "Use /register first."
        )
        return

    username = user["leetcode_username"]

    stats = await get_user_stats(username)

    if not stats:
        await update.message.reply_text(
            "❌ Could not find that LeetCode user."
        )
        return

    await update.message.reply_text(
        f"👤 {stats['username']}\n\n"
        f"🏆 Ranking: {stats['ranking']}\n\n"
        f"✅ Total Solved: {stats['total']}\n"
        f"🟢 Easy: {stats['easy']}\n"
        f"🟡 Medium: {stats['medium']}\n"
        f"🔴 Hard: {stats['hard']}"
    )