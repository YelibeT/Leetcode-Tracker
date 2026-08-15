from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
)

from config import BOT_TOKEN
from bot.handlers.start import start
from bot.handlers.register import (
    register,
    save_username,
    cancel,
    USERNAME
)
from bot.handlers.profile import profile
from bot.handlers.setup import choose_mode, choose_roadmap


app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("profile", profile))


register_handler = ConversationHandler(
    entry_points=[
        CommandHandler("register", register),
        CallbackQueryHandler(choose_mode, pattern="^mode_"),
        CallbackQueryHandler(choose_roadmap, pattern="^roadmap_")
    ],

    states={
        USERNAME: [
            MessageHandler(
                filters.TEXT & ~filters.COMMAND,
                save_username
            )
        ]
    },

    fallbacks=[
        CommandHandler("cancel", cancel)
    ]
)


app.add_handler(register_handler)


print("Bot is running...")

app.run_polling()