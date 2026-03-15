from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = "8676916478:AAG7ylzVf4N6UyvbbZQ2QW7kGj8avmVKkXs"
ADMIN_IDS = [6316039013]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("⭐ Stars sotib olish", callback_data="stars")],
        [InlineKeyboardButton("🤖 Bot haqida", callback_data="about")],
        [InlineKeyboardButton("📞 Aloqa", callback_data="contact")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Assalomu Aleykum. Xush kelibsiz! 👋\nQuyidagi tugmalardan birini tanlang:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "📌 *Mavjud komandalar:*\n\n"
        "/start — Botni ishga tushirish\n"
        "/help — Yordam\n"
        "/admin — Admin panel\n"
    )
    await update.message.reply_text(help_text, parse_mode="Markdown")

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "stars":
        await query.edit_message_text("⭐ Stars sotib olish uchun @Shakxrom ga murojaat qiling!")
    elif query.data == "about":
        await query.edit_message_text("🤖 Bot @Shakxrom tomonidan yaratilgan!")
    elif query.data == "contact":
        await query.edit_message_text("📞 Aloqa: @Shakxrom")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("❌ Sizda admin huquqi yo'q!")
        return
    await update.message.reply_text("🔧 *Admin panel*\n\nSiz admin huquqiga egasiz!", parse_mode="Markdown")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("admin", admin))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
