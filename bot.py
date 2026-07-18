from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    ConversationHandler,
    filters,
)

TOKEN = "СЮДА_ВСТАВЬ_ТОКЕН_ОТ_BOTFATHER"

ROLE, AGE, REASON = range(3)

ADMIN_ID = 123456789

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Привет! Для подачи заявки ответь на несколько вопросов.\n\n🎭 Какая у тебя роль?")
    return ROLE
