from config import * #importamos el token del codigo config.py
import telebot

bot = telebot.TeleBot(mi_token) #creamos la variable bot y dentro usamos el objeto telebot y el metodo telebot de la libreria
                            
#cuando usemos el comando /start, en los parametros agregamos una lista de comandos osea dependiendo el comando que usemos
#realizara cierta accion o mensaje
@bot.message_handler(commands=["start", "help", "ayuda"])
def cmd_start(message):
    #da la bienvenida al usuario
    bot.reply_to(message, "Hola en que puedo ayudarte")

#responde a los mensajes que no son comandos:
#text, audio, document, photo, sticker, video, video_note, voice, location
#contact, new_chat_members, left_chat_member, new_chat_title, new_chat_photo,
#delete_chat_photo, group_chat_created, supergroup_chat_created, channel_chat_created
#migrete_to_chat_id, migrate_from_chat_id, pinned_message

#dependiendo del contenido a lo que queremos que respondah hara tal accion

@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "este comando no existe")
    elif message.text == "Hola mundo":
         bot.send_message(message.chat.id, "hello")
    else:
        bot.send_message(message.chat.id, "Describe exactamente lo que quieres")
        


@bot.message_handler(content_types=["sticker"])
def bot_sticker(message):
    bot.send_message(message.chat.id, "Que lindo sticker")

@bot.message_handler(content_types=["photo"])
def bot_photo(message):
    bot.send_message(message.chat.id, "Photo recibida")
    


#main ##########
if __name__ == '__main__':
    print('iniciando bot')
    bot.infinity_polling()  
    print('fin')  
