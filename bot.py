from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

TOKEN = "8929108765:AAEpt_OZIrSAa9djKKz4JJRHV4X0IUyNA1w"

ROLE, AGE, REASON = range(3)

ADMIN_ID = -1004389081655

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Для подачи заявки ответь на несколько вопросов.\n\n🎭 Какая у тебя роль?")
    return ROLE
