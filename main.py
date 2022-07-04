import logging
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, executor, types

load_dotenv()
chat_id = os.environ['TG_CHAT_ID']
API_TOKEN = os.environ['TG_API_TOKEN']

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


@dp.message_handler(content_types=['photo'])
async def photo_handler(message: types.Message):
    photo = message.photo.pop()
    await photo.download(destination_dir='')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
