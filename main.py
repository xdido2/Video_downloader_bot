from aiogram import Dispatcher, Bot, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import Message
from dowloader import yt, tk, ig, pn, spotify

API_TOKEN = 'YOUR TOKEN'

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def hello(message: Message):
    await message.answer('Hello,this bot can download all medias from YouTube,Instagram,Pinterest,TikTok!')
    await message.answer('Send me a link,and i download you the media from this social media!')


@dp.message_handler(Text(startswith='https://youtu.be/'))
async def main_menu(message: types.Message):
    print(message.text.split('/')[-1])
    res = yt(message.text.split('/')[-1])
    print(message.text)
    print(res['video'])

    await message.answer_video(res['video'])
    print('\nVideo sent ' + str(data))


@dp.message_handler(Text(startswith='https://vt.tiktok.com/'))
async def main_menu(message: types.Message):
    res = tk(message.text)
    print(message.text)
    print(res['video'])
    await message.answer_video(res['video'])
    print('\nVideo sent ' + str(data))


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def main_menu(message: types.Message):
    res = ig(message.text)
    print(message.text)
    print(res['video'])
    await message.answer_video(res['video'])
    print('\nVideo sent ' + str(data))


@dp.message_handler(Text(startswith='https://pin.it/6Jtu9Oh'))
async def main_menu(message: types.Message):
    res = pn(message.text)
    print(message.text)
    print(res['video'])
    await message.answer_video(res['video'])
    print('\nVideo sent ' + str(data))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
