from telegram.ext import  CommandHandler, MessageHandler, Application, filters, CallbackQueryHandler
import handlears
import config

def main():
    TOKEN = config.get_token()

    dp = Application.builder().token(TOKEN).build()
    
    dp.add_handler(CommandHandler('start', handlears.start))
    dp.add_handler(CallbackQueryHandler(handlears.type_clasification, pattern='type:'))

    dp.add_handler(MessageHandler(filters=filters.TEXT, callback=handlears.send_message))
    dp.add_handler(MessageHandler(filters=filters.PHOTO, callback=handlears.covid_classification))

    dp.run_polling()
if __name__ == '__main__':
    main()
