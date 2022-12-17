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
    await bot.send_message(message.from_id, f'Привет, {message.from_user.first_name}! '
                                            f'Меня зовут Elbrus Career Bot! 💫')
    kb = [
        [
            types.KeyboardButton(text="Выбрать трэк"),
            types.KeyboardButton(text="Скачать схему"),
            types.KeyboardButton(text="Получить мотивацию"),
            types.KeyboardButton(text="Написать коучу")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )
    await message.answer("Чем я могу помочь?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Скачать схему")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Отличный выбор! Сейчас приготовлю файлы 🏃🏻')
    job = 'static/job.pdf'
    negotiation = 'static/negotiation.pdf'
    await bot.send_document(message.from_id, document=open(job, 'rb'))
    await bot.send_document(message.from_id, document=open(negotiation, 'rb'))
    await bot.send_message(message.from_id, text="🚨🚨🚨 *[Ссылка на miro](https://miro.com/app/board/uXjVP4s6vpQ=/)*", parse_mode='MarkdownV2')
    kb = [[types.KeyboardButton(text="Выбрать трэк"),
           types.KeyboardButton(text="Скачать схему"),
           types.KeyboardButton(text="Получить мотивацию"),
           types.KeyboardButton(text="Написать коучу")],]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder="Выбери один из вариантов:")
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться! Вот тебе мотивационный пингвин 🐧")
    await bot.send_animation(message.from_id, animation='https://media2.giphy.com/media/OZbGrdp7FiDiE/giphy.gif')
    kb = [[types.KeyboardButton(text="Выбрать трэк"),
           types.KeyboardButton(text="Скачать схему"),
           types.KeyboardButton(text="Получить мотивацию"),
           types.KeyboardButton(text="Написать коучу")], ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder="Выбери один из вариантов:")
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Написать коучу")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "Надя Крутикова отличный специалист, она тебе точно поможет!")
    await bot.send_message(message.from_id, text="❤️ *[Вот ссылка на аккаунт Нади](https://t.me/krutikovanad)* ❤️", parse_mode='MarkdownV2')
    kb = [[types.KeyboardButton(text="Выбрать трэк"),
           types.KeyboardButton(text="Скачать схему"),
           types.KeyboardButton(text="Получить мотивацию"),
           types.KeyboardButton(text="Написать коучу")], ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder="Выбери один из вариантов:")




@dp.message_handler(lambda message: message.text == "Выбрать трэк")
async def track(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Отличный выбор!')
    kb = [
        [
            types.KeyboardButton(text="Переговоры с работодателем"),
            types.KeyboardButton(text="Поиск работы"),
            types.KeyboardButton(text="Назад"),
            types.KeyboardButton(text="Вперед"),
            types.KeyboardButton(text="В начало")
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
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
