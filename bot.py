from telegram.ext import Application
from config import BOT_TOKEN


app = Application.builder().token(BOT_TOKEN).build()

print("Bot is running.aliza.")

app.run_polling()