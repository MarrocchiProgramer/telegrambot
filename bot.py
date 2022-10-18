import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton



def process_message(update, context):
    #espero el ultimo texto enviado del usuario
    text = update.message.text

    #"si el texto contiene #channel" envio el mensaje a el grupo especificado en chat_id, 
    # el mensaje llegara a grupo sin el #channel dejando solo el mensaje
    if str(text).__contains__('#channel'):
        context.bot.send_message(
            chat_id='-1001734611459',
            text=str(text).replace('#channel', '')
        )
    #muestro el mensaje del usuario en consola
    print(str(text))


#esto significa que el programa empezara a ejecutarse por aca
if __name__ == '__main__':
    
    #recibe las peticiones del usuario hacia el bot(por ejemplo un mensaje)
    updater = Updater(token='5772798648:AAELl54LNmwV2bg12CR8ugiyTDln_l2aLsE', use_context=True)   

    #una vez que el updater recibe la peticion es el dispatcher quien se encarga de manejar los comandos
    dispatcher = updater.dispatcher   
    #el comandhandler nos permite usar las funciones que tenemos declaradas, en este caso espera texto y recibe la funcion process_message
    dispatcher.add_handler(MessageHandler(filters=Filters.text, callback=process_message))   


    #nos permite escuchar infinitamente hasta que el usuario envie un comando
    updater.start_polling()
    print('El bot se inicio')
    updater.idle()



    






#PARA MANDAR COSAS 
# dp.add_handler(CommandHandler('start', start))
# dp.add_handler(MessageHandler(filters=Filters.text, callback=process_message))   



# def start (update, context):

#     mensaje=update.message.reply_text(
#         reply_markup=InlineKeyboardMarkup([
#             [InlineKeyboardButton(text='Go to the bot', url='https://youtube.com')]
#         ])
#     )
    
#     if update.message.text.__contains__('hola'):
#         context.bot.send_message(
#            chat_id='-1001734611459',
#            text=mensaje
#         )

  


# if __name__ == '__main__':
#     updater = Updater(token='TOKEN', use_context=True) #TOKEN es una variable de entorno

#     dp = updater.dispatcher
#     dp.add_handler(
#         CommandHandler('start', start)
#     )

#     updater.start_polling() 
#     print('El bot se inicio')
#     updater.idle()