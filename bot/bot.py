from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters
)

from config import BOT_TOKEN
from bot.handlers.start import start
from bot.handlers.register import (
    register,
    save_username,
    USERNAME
)


app = Application.builder().token(BOT_TOKEN).build()


app.add_handler(CommandHandler("start", start))


register_handler = ConversationHandler(
    entry_points=[
        CommandHandler("register", register)
    ],
    states={
        USERNAME: [
            MessageHandler(filters.TEXT & ~filters.COMMAND, save_username)
        ]
    },
    fallbacks=[]
)

app.add_handler(register_handler)


print("Bot is running...")

app.run_polling()