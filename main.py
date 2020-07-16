import logging
import requests
import telegram
import random

from telegram.ext import Updater, CommandHandler

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Init bot')
friki_bot = telegram.Bot(token='596162081:AAEKkptlt5UxhxOEHKZ08sDyMOk8VB63Wak')

updater = Updater(token='596162081:AAEKkptlt5UxhxOEHKZ08sDyMOk8VB63Wak', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    logger.info('Start command')
    update.message.reply_text('Wazup, Soy el FrikiBot 2.0: Ahora es personal!')

def get_image(update, context):
    logger.info('getImage command')

    image_number = random.randint(0, 19)
    image = 'random{}.jpeg'.format(image_number)
    update.message.reply_to_message.sendPhoto('https://storage.googleapis.com/assets-friki-bot/ImagenesRandom/{}'.format(image))


start_handler = CommandHandler('start', start)
get_image_handler = CommandHandler('meme', get_image)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(get_image_handler)

updater.start_polling()