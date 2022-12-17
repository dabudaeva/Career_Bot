import os
import logging
from aiogram import Dispatcher, Bot, executor, types

from buttons import kb, keyboard, keyboard1, markup5
logging.basicConfig(level=logging.INFO,
                    filename='logfile.log',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S')

# TOKEN = os.getenv('TOKEN')
TOKEN = '5522470947:AAH8E3dr59tGtaxt1iw5nH0Rvyg5z0BM8gY'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен!')

# @dp.message_handler(commands=['start'])
# async def starter(message: types.Message):
#     logging.info(f'{message.from_user.full_name}: {message.text}')
#     # await bot.send_photo(message.from_id, photo=open('static/start.jpg', 'rb'))
#     await message.reply("Пятое - добавляем ряды кнопок",
#                         reply_markup=kb.markup5)
#     # await message.answer("Чем я могу помочь?", reply_markup=markup5)

import buttons as kb

@dp.message_handler(commands=['start'])
async def process_hi5_command(message: types.Message):
    await bot.send_photo(message.from_id, photo=open('static/start.jpg', 'rb'))
    # await message.reply("Могу я помочь чем-то еще?",
                        # reply_markup=kb.markup5)
    await message.answer("Чем я могу помочь?", reply_markup=kb.markup5)
@dp.message_handler(lambda message: message.text == "Скачать схему")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Отличный выбор! Сейчас приготовлю файлы 🏃🏻')
    job = 'static/job.pdf'
    negotiation = 'static/negotiation.pdf'
    await bot.send_document(message.from_id, document=open(job, 'rb'))
    await bot.send_document(message.from_id, document=open(negotiation, 'rb'))
    await bot.send_message(message.from_id, text="🚨🚨🚨 *[Ссылка на miro](https://miro.com/app/board/uXjVP4s6vpQ=/)*", parse_mode='MarkdownV2')
  
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться! Вот тебе мотивационный пингвин 🐧")
    await bot.send_animation(message.from_id, animation='https://media2.giphy.com/media/OZbGrdp7FiDiE/giphy.gif')
    await message.answer("Могу я помочь чем-то еще?", reply_markup=kb.markup5)
@dp.message_handler(commands=["test"])
async def any_message(message: types.Message):
    await message.answer("Hello, <b>world</b>!", parse_mode="HTML")
    await message.answer("Hello, *world*\!", parse_mode="MarkdownV2")
    await message.answer("Сообщение с <u>HTML-разметкой</u>", parse_mode="HTML")

@dp.message_handler(lambda message: message.text == "Написать коучу")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_photo(message.from_id, photo=open('static/couch.png', 'rb'), 
    caption='Надя Крутикова отличный специалист, она тебе точно поможет!')
    
    await message.answer("Что делаем?", reply_markup=keyboard1)

@dp.message_handler(lambda message: message.text == "Написать в личку")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "Надя Крутикова отличный специалист, она тебе точно поможет!")
    await bot.send_message(message.from_id, text="❤️ *[Вот ссылка на аккаунт Нади](https://t.me/krutikovanad)* ❤️", parse_mode='MarkdownV2')
    await message.answer("Что-то ещё?", reply_markup=kb.markup5)

@dp.message_handler(lambda message: message.text == "Выбрать трэк")
async def track(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Отличный выбор!')
    await message.answer("Какой трэк вы выбираете?", reply_markup=kb.markup5)


@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
