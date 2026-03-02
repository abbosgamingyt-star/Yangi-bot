import logging
from telegram import Update
from telegram.ext import ContextTypes
from config import Config
from database import save_message

logger = logging.getLogger(__name__)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    if not message or not message.text:
        return

    user = message.from_user
    user_id = user.id
    username = user.username or ""
    full_name = user.full_name or ""

    try:
        save_message(user_id, username, full_name, message.text)
    except Exception as e:
        logger.error(f"Failed to save message to DB: {e}")

    try:
        forward_text = (
            f"📨 New message from {full_name}\n"
            f"🆔 User ID: {user_id}\n"
            f"📛 Username: @{username}\n"
            f"💬 Message:\n{message.text}"
        )
        await context.bot.send_message(
            chat_id=Config.ADMIN_CHAT_ID,
            text=forward_text
        )
        logger.info(f"Message from {user_id} forwarded to admin")
    except Exception as e:
        logger.error(f"Failed to forward message to admin: {e}")

    await message.reply_text(
        "✅ Thank you! Your message has been received. "
        "Our team will contact you if necessary."
    )
