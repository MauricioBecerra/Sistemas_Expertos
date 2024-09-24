 # Mauricio Becerra Guzman - 21310105

import json
import random
import logging
import nltk
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from nltk.tokenize import word_tokenize

nltk.download('punkt')

nltk.download('punkt_tab')


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#responses = {}


# Función para agregar nuevas palabras clave y respuestas al diccionario
def add_response(update, context):
    try:
        keywords = context.args[:-1]
        response2 = context.args[-1]
        response = str(response2).replace('_', ' ')

        if not keywords:
            update.message.reply_text("Por favor, proporciona al menos una palabra clave.")
            return

        for keyword in keywords:
            if keyword in responses:
                responses[keyword].add(response)
            else:
                responses[keyword] = {response}

        update.message.reply_text("¡Palabra clave y respuesta agregadas!")
        save_responses()

    except IndexError:
        update.message.reply_text("Error: Asegúrate de proporcionar palabras clave y una respuesta.")
    except Exception as e:
        update.message.reply_text(f"Se produjo un error: {e}")


# Función para manejar mensajes recibidos por el bot
def handle_message(update, context):
    # Tokenizar texto recibido
    message = update.message.text
    words = word_tokenize(message)

    bot_name = "Botsi"
    if bot_name in message:
        # Buscar palabras clave en el texto
        match = None
        for keyword, response_set in responses.items():
            if keyword in message:
                match = random.sample(list(response_set), 1)[0]
                break
        if match:
            context.bot.send_message(chat_id=update.effective_chat.id, text=match)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Lo siento, no entiendo lo que estás preguntando.")

    bot_name2 = "botsi"
    if bot_name2 in message:
        # Buscar palabras clave en el texto
        match = None
        for keyword, response_set in responses.items():
            if keyword in message:
                match = random.sample(list(response_set), 1)[0]
                break
        if match:
            context.bot.send_message(chat_id=update.effective_chat.id, text=match)
        else:
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text="Lo siento, no entiendo lo que estás preguntando.")


# Función para remover respuestas del diccionario
def remove_response(update, context):
    keyword = context.args[0]
    response2 = context.args[1]
    response = str(response2).replace('_', ' ')
    if keyword in responses and response in responses[keyword]:
        responses[keyword].remove(response)
        update.message.reply_text("Respuesta eliminada!")
    else:
        update.message.reply_text("La palabra clave o la respuesta no se encuentra en la memoria del bot.")


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def start(update, context):
    user = update.effective_user['username']
    """Send a message when the command /start is issued."""
    update.message.reply_text(f'Hola @{user}, soy Botsi :D')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Este es un bot de conversacion y de apoyo de comunicacion con otros usuarios')

def save_responses():
    with open('responses.txt', 'w') as f:
        for keyword, responses_set in responses.items():
            for response in responses_set:
                f.write(f"{keyword}::{response}\n")  # Usamos "::" como delimitador

def load_responses():
    global responses
    responses = {}
    try:
        with open('responses.txt', 'r') as f:
            for line in f:
                keyword, response = line.strip().split('::', 1)  # Divide por el delimitador
                if keyword in responses:
                    responses[keyword].add(response)
                else:
                    responses[keyword] = {response}
    except FileNotFoundError:
        responses = {}  # Si el archivo no existe, inicializa como diccionario vacío

def main():
    load_responses()
    # Inicializar bot
    updater = Updater("5015528233:AAETYuuWQsEeFKIcTf3122d_0vPk_cFROQA", use_context=True)
    dp = updater.dispatcher

    # Agregar manejadores de comandos
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("add", add_response))
    dp.add_handler(CommandHandler("remove", remove_response))

    # Agregar manejador de mensajes
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Registrar manejador de errores
    dp.add_error_handler(error)

    # Iniciar el bot
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    
    main()
