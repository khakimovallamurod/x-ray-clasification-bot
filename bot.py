from telegram.ext import CommandHandler, Updater,MessageHandler, Filters
import handlears
import config

def main():
    TOKEN = config.get_token()
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', handlears.start))

    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=handlears.send_message))
    dispatcher.add_handler(MessageHandler(filters=Filters.photo, callback=handlears.covid_clasification))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
