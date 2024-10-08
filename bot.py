from telegram.ext import  CommandHandler, MessageHandler, Application, filters
import handlears
import config

def main():
    TOKEN = config.get_token()

    dp = Application.builder().token(TOKEN).build()
    
    dp.add_handler(CommandHandler('start', handlears.start))

    dp.add_handler(MessageHandler(filters=filters.text, callback=handlears.send_message))
    dp.add_handler(MessageHandler(filters=filters.photo, callback=handlears.covid_clasification))

    dp.run_polling()
if __name__ == '__main__':
    main()
