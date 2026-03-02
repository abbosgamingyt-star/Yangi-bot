import logging
import time
from telegram.ext import ApplicationBuilder, MessageHandler, filters, CommandHandler
from config import Config
from database import init_db
from handlers import handle_message, start_command

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

_last_msg_time = {}

async def rate_limited_handler(update, context):
    user_id = update.effective_user.id
    now = time.time()

    if user_id in _last_msg_time:
        if now - _last_msg_time[user_id] < Config.RATE_LIMIT_SECONDS:
            await update.message.reply_text("⏳ Too many messages. Please slow down.")
            return

    _last_msg_time[user_id] = now
    await handle_message(update, context)

def main():
    init_db()
    app = ApplicationBuilder().token(Config.BOT_TOKEN).build()
    
    # Add handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, rate_limited_handler)
    )
    
    logger.info("Bot started polling")
    app.run_polling()

if __name__ == "__main__":
    main()
