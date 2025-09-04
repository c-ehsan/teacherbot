from telegram.ext import Updater,CommandHandler
from handlers import start
from database import init_db
import os 


Token = os.environ.get("BOT_TOKEN")
def main():
    init_db()
    updater=Updater(Token,use_context=True)
    dp=updater.dispatcher
    # ثبت دستورات 
    dp.add_handler(CommandHandler("start",start))
    updater.start_polling()
    updater.idle()

if __name__=="__main__":
    main()


