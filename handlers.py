from telegram import Update
from telegram.ext import callbackcontext

def start(update:Update,context:callbackcontext):
    user=update.effective_user
    update.message.reply_text(f"hello {user.first_name}!\n im teacher bot i like to teach and study")
