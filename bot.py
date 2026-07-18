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

ROLE, AGE, USERNAME = range(3)

ADMIN_ID = -1004389081655


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋☺️ Привет!\n\n"
        "Для подачи заявки ответь на несколько вопросов.\n\n"
        "1️⃣ За какую роль хотите вступить?"
    )
    return ROLE


async def role(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["role"] = update.message.text

    await update.message.reply_text(
        "2️⃣ Сколько вам лет?\n"
        "📎 Пришлите доказательство возраста."
    )

    return AGE


async def age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["age"] = update.message.text

    await update.message.reply_text(
        "3️⃣ Ваш Telegram-юз (@username)?"
    )

    return USERNAME


async def finish(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["username"] = update.message.text

    text = (
        "📩 Новая заявка!\n\n"
        f"🎭 Роль: {context.user_data['role']}\n"
        f"🎂 Возраст: {context.user_data['age']}\n"
        f"👤 Юз: {context.user_data['username']}"
    )

    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=text
    )

    await update.message.reply_text(
        "✅ Ваша заявка успешно отправлена!"
    )

    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "❌ Заявка отменена."
    )
    return ConversationHandler.END
    
def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, role))

    app.run_polling()


if __name__ == "__main__":
    main()
