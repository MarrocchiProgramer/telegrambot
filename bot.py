import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

def process_message(update, context):
    text = update.message.text

    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='-1001734611459',
            text=str(text).replace('#channel', '')
        )

    print(str(text))


if __name__ == '__main__':
    updater = Updater(token='5772798648:AAELl54LNmwV2bg12CR8ugiyTDln_l2aLsE', use_context=True)   

    dp = updater.dispatcher   
    dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))     

    updater.start_polling()
    print('El bot se inicio')
    updater.idle()

# https://t.me/+P1X0RU5CLjliMDhh
# dp.add_handler(CommandHandler('start', start))

# def start (update, context):
#     update.message.reply_text('Hola como estas')
#     boton1 = InlineKeyboardButton( 
#         text='Que dia faltara',
#         url='https://youtube.com'
#     )
#     update.message.reply_text(
#         text='Hace click en el boton',
#         reply_markup=InlineKeyboardMarkup([
#         [boton1]
#         ])
#     )
