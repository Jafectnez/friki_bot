import logging
import requests
import telegram
import random

from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def start(update, context):
    logger.info('Start command')
    update.message.reply_text('Wazup, Soy el FrikiBot 2.0: Ahora es personal!')

def get_image(update, context):
    logger.info('getImage command')

    image_number = random.randint(1, 19)
    image_url = 'https://storage.googleapis.com/assets-friki-bot/ImagenesRandom/random{}.jpeg'.format(image_number)
    
    logger.info('sending image: {}'.format(image_url))

    context.bot.send_photo(chat_id=update.message.chat_id, photo=image_url)

def init_bot():
    logger.info('Init bot')
    updater = Updater(token='596162081:AAEKkptlt5UxhxOEHKZ08sDyMOk8VB63Wak', use_context=True)
    dispatcher = updater.dispatcher
    
    start_handler = CommandHandler('start', start)
    meme_handler = CommandHandler('meme', get_image)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(meme_handler)

    updater.start_polling()
    logger.info('Bot listening')
