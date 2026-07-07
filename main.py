import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN not found in .env file")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start command"""
    await update.message.reply_text(
        "مرحبًا بك في بوت البحث عن المفقودين.\n"
        "أرسل صورة الشخص المفقود وسأستقبلها."
    )
    logger.info(f"User {update.effective_user.id} started the bot")

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle photo messages"""
    await update.message.reply_text("تم استلام الصورة بنجاح.")
    logger.info(f"Photo received from user {update.effective_user.id}")
    
    # TODO: Add photo processing logic here
    # - Save photo
    # - Store metadata
    # - Process image

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle errors"""
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main():
    """Start the bot"""
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.PHOTO, photo))
    
    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    logger.info("Bot started - polling for messages...")
    application.run_polling()

if __name__ == '__main__':
    main()
