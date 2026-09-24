from datetime import time
from zoneinfo import ZoneInfo

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
    CallbackQueryHandler,
    Defaults,
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

from bot.handlers.setup import (
    choose_mode,
    choose_roadmap,
    go_back,
    cancel_setup
)

from bot.handlers.checkSolved import check_solved
from bot.handlers.daily import send_daily_problem


TIMEZONE = ZoneInfo(
    "Africa/Addis_Ababa"
)


app = (
    Application.builder()
    .token(BOT_TOKEN)
    .defaults(
        Defaults(
            tzinfo=TIMEZONE
        )
    )
    .build()
)


app.add_handler(
    CommandHandler(
        "start",
        start
    )
)

app.add_handler(
    CommandHandler(
        "profile",
        profile
    )
)


register_handler = ConversationHandler(

    entry_points=[
        CommandHandler(
            "register",
            register
        ),

        CallbackQueryHandler(
            choose_mode,
            pattern="^mode_"
        ),

        CallbackQueryHandler(
            choose_roadmap,
            pattern="^roadmap_"
        ),

        CallbackQueryHandler(
            go_back,
            pattern="^back$"
        ),

        CallbackQueryHandler(
            cancel_setup,
            pattern="^cancel_setup$"
        )
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
        CommandHandler(
            "cancel",
            cancel
        )
    ]
)


app.add_handler(
    register_handler
)


app.add_handler(
    CallbackQueryHandler(
        check_solved,
        pattern="^check_solved$"
    )
)


app.job_queue.run_daily(
    send_daily_problem,
    time=time(
        hour=9,
        minute=0
    ),
    name="daily_leetcode_problem"
)


print(
    "Bot is running..."
)

print(
    "Daily problems scheduled for 09:00 "
    "Africa/Addis_Ababa"
)


app.run_polling()
