from telegram.ext import Application, CommandHandler
from bot.config import BOT_TOKEN


from bot.handlers.start import start
from bot.handlers.register import register


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
    
)
app.add_handler(
    CommandHandler("register", register)
    
)


print("Bot is running...")

app.run_polling()