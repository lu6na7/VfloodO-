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
    await update.message.reply_text("👋☺️ Привет! Для подачи заявки ответь на несколько вопросов.")
    return ROLE
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("1️⃣ За какую роль хотите вступить?")
    return ROLE


async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["role"] = update.message.text
    await update.message.reply_text(
        "2️⃣ Сколько вам лет?\n📎 Пришлите доказательство возраста."
    )
    return AGE


async def username(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text
    await update.message.reply_text("3️⃣ Ваш Telegram-юз (@username)?")
    return REASON


async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["username"] = update.message.text

    text = (
        "📩 Новая заявка\n\n"
        f"🎭 Роль: {context.user_data['role']}\n"
        f"🎂 Возраст: {context.user_data['age']}\n"
        f"👤 Юз: {context.user_data['username']}"
    )

    await context.bot.send_message(chat_id=ADMIN_ID, text=text)
    await update.message.reply_text("✅ Ваша заявка успешно отправлена!")
    return ConversationHandler.END
