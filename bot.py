import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 أهلاً بك!\n"
        "أرسل رابط فيديو وسأقوم بتحميله 🎬"
    )

async def download(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text
    await update.message.reply_text("⏳ جاري التحميل...")

    try:
        os.system(f"yt-dlp -o video.mp4 {url}")
        await update.message.reply_video(video=open("video.mp4", "rb"))
        os.remove("video.mp4")
    except:
        await update.message.reply_text("❌ حدث خطأ أثناء التحميل")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, download))
app.run_polling()
