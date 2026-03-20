import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "8722370651:AAHzNBdo9rba8GDsMX8n3zwG7IpTGfem7fU"

def start(update, context):
    update.message.reply_text("سلام")

def message(update, context):
    update.message.reply_text("سلام خوب هستین")

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text, message))

updater.start_polling()
updater.idle()
