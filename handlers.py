import logging
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler
from config import Config
from database import save_message

logger = logging.getLogger(__name__)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle the /start command"""
    user = update.effective_user
    welcome_message = (
        f"Assalomu alaykum, {user.first_name}! 👋\n\n"
        "Murojatingiz bo'lsa, marhamat, batafsil yozib qoldiring. "
        "Biz murojatingizni o'rganib chiqib, siz bilan bog'lanamiz.\n\n"
        "📞 Siz bilan bog'lanishimiz uchun bizga telefon raqam yoki "
        "Telegram manzilingizni qoldiring."
    )
    await update.message.reply_text(welcome_message)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle any text message that is not a command."""
    message = update.message
    if not message or not message.text:
        return

    user = message.from_user
    user_id = user.id
    username = user.username or ""
    full_name = user.full_name or ""

    # Save to database
    try:
        save_message(user_id, username, full_name, message.text)
    except Exception as e:
        logger.error(f"Failed to save message to DB: {e}")

    # Forward to admin
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

    # Acknowledge user (you can keep this in Uzbek too if you want)
    await message.reply_text(
        "✅ Rahmat! Sizning murojatingiz qabul qilindi. "
        "Kerak bo'lsa, tez orada siz bilan bog'lanamiz."
    )

