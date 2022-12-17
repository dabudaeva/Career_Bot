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

@dp.message_handler(commands=['start'])
@dp.message_handler(lambda message: message.text == "В начало")
async def starter(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    # await bot.send_message(message.from_id, f'Привет, {message.from_user.first_name}! '
    #                                         f'Меня зовут Elbrus Career Bot! 💫')
    await bot.send_photo(message.from_id, photo=open('static/start.jpg', 'rb'))
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
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться! Вот тебе мотивационный пингвин 🐧")
    await bot.send_animation(message.from_id, animation='https://media2.giphy.com/media/OZbGrdp7FiDiE/giphy.gif')
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Написать коучу")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "Надя Крутикова отличный специалист, она тебе точно поможет!")
    await bot.send_message(message.from_id, text="❤️ *[Вот ссылка на аккаунт Нади](https://t.me/krutikovanad)* ❤️", parse_mode='MarkdownV2')





start_text = "Тест"

@dp.message_handler(lambda message: message.text == "Выбрать трэк")
async def track(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    start_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="Переговоры с работодателем", callback_data="negotiation"),
        types.InlineKeyboardButton(text="Поиск работы", callback_data="job")
    )
    await message.answer("Какой трэк вы выбираете?", reply_markup=start_keyboard)


@dp.callback_query_handler(text="negotiation")
async def negotiations(query: types.CallbackQuery):
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Далее", callback_data="next1")
    )
    await query.message.edit_text('Вам звонит/пишет HR  и сообщает, '
                                  'что работодатель готов сделать оффер!', reply_markup=keyboard1)


@dp.callback_query_handler(text="next1")
async def negotiations(query: types.CallbackQuery):
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="negotiation"),
        types.InlineKeyboardButton(text="Далее", callback_data="next2"),
    )
    await query.message.edit_text('Запишите все, что HR рассказал по телефону/сравните '
                                  'текст сообщения с текстом вакансии - информация может '
                                  'немного отличаться от опубликованной в вакансии, то, что '
                                  'озвучил/написал  HR  имеет большую силу.', reply_markup=keyboard1)

@dp.callback_query_handler(text="next2")
async def negotiations(query: types.CallbackQuery):
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next1"),
        types.InlineKeyboardButton(text="Далее", callback_data="next3"),
    )
    await query.message.edit_text(''
                                  'Не говорите сразу же "да, я согласен", '
                                  'попросите выслать оффер в письменном виде, '
                                  'чтобы вы могли подробно в спокойной обстановке '
                                  'ознакомиться с информацией', reply_markup=keyboard1)







@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
