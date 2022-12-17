import os
import logging
from aiogram import Dispatcher, Bot, executor, types


logging.basicConfig(level=logging.INFO,
                    filename='logfile.log',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S')

# TOKEN = os.getenv('TOKEN')
TOKEN = '5865671919:AAGRIya9qE9f_IoBsu6Qu-geMnD_QZ9h6YU'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Привет, {message.from_user.first_name}! Меня зовут Elbrus Career Bot! 💫')
    kb = [
        [
            types.KeyboardButton(text="Выбрать трэк"),
            types.KeyboardButton(text="Скачать схему"),
            types.KeyboardButton(text="Получить мотивацию"),
            types.KeyboardButton(text="Написать коучу Наде")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )
    await message.answer("Что бы вы хотели от меня?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Выбрать трэк")
async def track(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Отличный выбор!')
    kb = [
        [
            types.KeyboardButton(text="Переговоры с работодателем"),
            types.KeyboardButton(text="Поиск работы")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )
    await message.answer("Какой трэк вы выбираете?", reply_markup=keyboard)



@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'Еще раз:')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
