from config import * #importamos el token del codigo config.py
import telebot
import time
import threading

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
    elif message.text in papa:
        bot.send_message(message.chat.id, "no te preocupes todo esta bien")
        archivo = open("help.jpg", "rb")
        bot.send_photo(message.chat.id, archivo, "Imagen enviada")
    elif message.text in estadocritico:
        bot.send_message(message.chat.id, "nivel de estado mental critico, se enviaran recomendaciones")
    elif message.text in estadoestable:
        bot.send_message(message.chat.id, "nivel de estado mental estable, dentro de los niveles estandars")
    elif message.text in estadopositivo:
        bot.send_message(message.chat.id, "nivel de estado mental positivo, comparte esta felicidad a otros")
    else:
        x = bot.send_message(message.chat.id, "<b>Describe exactamente lo que quieres</b>", parse_mode="html")
        time.sleep(3)
        bot.edit_message_text("<b>Recuerda que soy un bot con una capacidad limitada</b>", message.chat.id, x.message_id, parse_mode="html")
  

@bot.message_handler(content_types=["sticker"])
def bot_sticker(message):
    bot.send_message(message.chat.id, "Que lindo sticker")

@bot.message_handler(content_types=["photo"])
def bot_photo(message):
    bot.send_message(message.chat.id, "Photo recibida")
    


#main ##########
#if __name__ == '__main__':
    #print('iniciando bot')
    #bot.infinity_polling()  
    #print('fin')  

def recibir_mensajes():
    bot.infinity_polling()

if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "da la bienvnida"), 
        telebot.types.BotCommand("/linkstart", "inicio de session"),
        telebot.types.BotCommand("/systemcall", "llamada al sistema"),
    ])
    print('Starting...')
    hilo_bot = threading.Thread(name="hilo_bot", target=recibir_mensajes)
    hilo_bot.start()
    print('bot iniciado')
    a = bot.send_message(id_chat, "Hola soy YUI tu asistente de Autoayuda")
    time.sleep(3)
    bot.edit_message_text("<b>Del 1 al 10 como describirias tu salud mental</b>", id_chat, a.message_id, parse_mode="html")
 
