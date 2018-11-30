from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import ephem
from datetime import datetime
from cfg import bot_api_key, PROXY

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
def main():
    mybot = Updater(bot_api_key, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", planet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()

def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)

def planet_user(bot, update):
    user_text = update.message.text.split()
    try:
        if len(user_text) != 2:
            user_text = "/planet 'Название планеты'"
        else:
            panet = getattr(ephem, user_text[1])(datetime.strftime(datetime.now(), "%Y/%m/%d"))
            user_text = ephem.constellation(panet)
    except AttributeError:
        user_text = "Название планет: Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune, Pluto, Sun"
    update.message.reply_text(user_text)


#if __name__ == "__name__":
main()
