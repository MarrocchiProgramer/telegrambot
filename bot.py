import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton



def start (update, context):

    mensaje=update.message.reply_text(
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Go to the bot', url='https://youtube.com')]
        ])
    )
    
    if update.message.text.__contains__('hola'):
        context.bot.send_message(
           chat_id='-1001734611459',
           text=mensaje
        )

  


if __name__ == '__main__':
    updater = Updater(token='5772798648:AAELl54LNmwV2bg12CR8ugiyTDln_l2aLsE', use_context=True)

    dp = updater.dispatcher
    dp.add_handler(
        CommandHandler('start', start)
    )

    updater.start_polling() 
    print('El bot se inicio')
    updater.idle()
    






#PARA MANDAR COSAS 
# dp.add_handler(CommandHandler('start', start))
# dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))   


# if __name__ == '__main__':
#     updater = Updater(token='5772798648:AAELl54LNmwV2bg12CR8ugiyTDln_l2aLsE', use_context=True)   

#     dp = updater.dispatcher   
#     dp.add_handler(MessageHandler(filters=Filters.all, callback='start'))  

#     updater.start_polling()
#     print('El bot se inicio')
#     updater.idle()




# def process_message(update, context):
#     text = update.message.text

#     if str(text).__contains__('#channel'):
#         context.bot.send_message(
#             chat_id='-1001734611459',
#             text=str(text).replace('#channel', '')
#         )

#     print(str(text))