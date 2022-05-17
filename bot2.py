import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


def greet_user(update, context):
    print("Вызван /start")
   # print(update)
    update.message.reply_text("Здравствуй пользователь!")


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    # Cоздаем бота и передаем ему ключ для авторизации в Telegram
    mybot = Updater(settings.API_KEY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Bot started')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать пока мы его не остановим принудительно
    mybot.idle()


if _name_ == "_main_":
    main()
