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
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Далее", callback_data="next1")
    )
    await query.message.edit_text('Вам звонит/пишет HR  и сообщает, '
                                  'что работодатель готов сделать оффер!', reply_markup=keyboard1)


@dp.callback_query_handler(text="next1")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
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
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next1"),
        types.InlineKeyboardButton(text="Далее", callback_data="next3"),
    )
    await query.message.edit_text('Не говорите сразу же "да, я согласен", '
                                  'попросите выслать оффер в письменном виде, '
                                  'чтобы вы могли подробно в спокойной обстановке '
                                  'ознакомиться с информацией', reply_markup=keyboard1)

@dp.callback_query_handler(text="next3")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next2"),
        types.InlineKeyboardButton(text="Далее", callback_data="next4"),
        types.InlineKeyboardButton(text="Важно", callback_data="next4_alt"),
    )
    await query.message.edit_text('Вы получили письменный оффер (обычно по '
                                  'имейлу в приложении отдельным файлом)', reply_markup=keyboard1)

@dp.callback_query_handler(text="next4_alt")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next3"),
    )
    await query.message.edit_text('Если вы получили оффер - для "поднятия" '
                                  'своего рейтинга у других работодателей, '
                                  'не забудьте сообщить всем компаниям, от которых ждете '
                                  'ответ по собеседованиям (особенно тем, в '
                                  'которые очень хотите), что вы получили оффер:'
                                  '"Добрый день, __имя рекрутера__,'
                                  'Хотел(а) бы сделать апдейт по процессу рекрутинга - '
                                  'я на днях  получил(а) оффер, однако ваша компания '
                                  'для меня приоритетна и я бы хотел(а) пройти дальнейшие '
                                  'этапы/получить обратную связь по собеседованию как можно '
                                  'скорее. Подскажите, пожалуйста, сможете ли вы до (свой день '
                                  'недели) вернуться с ответом по моей кандидатуре?"'
                                  'Сообщать от какой компании оффер и на какую сумму не нужно.', reply_markup=keyboard1)


@dp.callback_query_handler(text="next4")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next3"),
        types.InlineKeyboardButton(text="Далее", callback_data="next5"),
        types.InlineKeyboardButton(text="Важно", callback_data="next5_alt"),
    )
    await query.message.edit_text('Скажите, что вам нужно время обдумать их '
                                  'предложение и назовите срок, когда вы вернетесь '
                                  'с ответом (в идеале не больше 3-4 рабочих дней). '
                                  'Не принимайте оффер сразу же так как первый оффер '
                                  'от любой компании ВСЕГДА минимален по сумме, он '
                                  'только открывает пространство переговоров по зарплате. '
                                  'помните, что  зарплата разработчика прежде всего зависит '
                                  'от суммы, в которую он сам себя оценивает.'
                                  '"Добрый день, __имя рекрутера__, Благодарю, документ получил(а).'
                                  'Я внимательно ознакомлюсь с оффером и вернусь к вам до день '
                                  'недели/дата. Большое спасибо, что поделились со мной '
                                  'хорошими новостями, будем на связи!"', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_alt")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next4"),
    )
    await query.message.edit_text('Если вы получили оффер, на который просят ответить за короткое время (24/48/72 часа), '
                                  'а вы не готовы так быстро принять решение/ждете информации от других работодателей. Не ведитесь на '
                                  'срочность и не переживайте - это просто способ работодателя надавить и поскорее закрыть вакансию. Напишите ответ HR в таком ключе:'
                                  '"Добрый день, _имя рекрутера__,'
                                  'Благодарю, документ получил(а). К сожалению, принять решение по данному предложению в такой короткий срок/за 24-48-72 часа/1 день/2 дня я не имею возможности, так как нахожусь на финальной стадии переговоров с другими компаниями и этот процесс займет еще примерно неделю. Мне понадобится больше времени, чтобы принять взвешенное решение".'
                                  'Если компания возвращается с ответом, что это единственный вариант и они не могут предложить других опций по времени, напишите им:'
                                  '"Очень жаль, мне нравится ваша компания, проект и команда. Решение о выборе работодателя для меня очень важное и ответственное и я никак не могу его принять за такой короткий срок"'
                                  'Большинство компаний на этом этапе продлят срок или начнут торговаться по сроку. Если этого не происходит - возможно, это не твоя компания.', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next4"),
        types.InlineKeyboardButton(text="Так и есть", callback_data="next6"),
        types.InlineKeyboardButton(text="Не совсем так", callback_data="next5_no"),
    )
    await query.message.edit_text('Вам сделали отличное предложение, оффер на большую зарплату, '
                                  'чем вы рассчитывали?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_no")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next5"),
        types.InlineKeyboardButton(text="Да", callback_data="next6"),
        types.InlineKeyboardButton(text="Нет", callback_data="next5_no_again"),
    )
    await query.message.edit_text('Вам сделали хорошее предложение, оффер на среднюю зарплату?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_no_again")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next5_no"),
        types.InlineKeyboardButton(text="Да", callback_data="next6_alt"),
    )
    await query.message.edit_text('Вам сделали предложение с низкой зарплатой?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next6")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next5"),
        types.InlineKeyboardButton(text="Соглашусь на оффер", callback_data="next7"),
        types.InlineKeyboardButton(text="Попытаю еще удачу", callback_data="next7_alt1"),
    )
    await query.message.edit_text('Прежде чем согласиться, вспомните про то, что первый оффер всегда '
                                  'минимальный - обдумайте и  решите, хотите ли попробовать поднять '
                                  'сумму - это возможно!', reply_markup=keyboard1)


@dp.callback_query_handler(text="next7")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next6"),
    )
    await query.message.edit_text('Ок, не забудьте про юридическое оформлени!', reply_markup=keyboard1)

@dp.callback_query_handler(text="next7_alt1")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next7"),
    )
    await query.message.edit_text('"Я внимательно ознакомился(лась) с вашим предложением. '
                                  'Должен(а) признать, что оно привлекательно и конкурентоспособно. '
                                  'Мне нравится ваша компания/проект/команда и я заинтересован в '
                                  'сотрудничестве с вами.'
                                  '1. Поднимаем сумму'
                                  'Однако на днях у меня завершились переговоры с другой компанией и я получил(а) оффер привлекательнее по размеру заработной платы. Предлагаю пересмотреть размер зарплаты до (сумма)."'
                                  '2.Улучшаем условия, которые не устраивают'
                                  'Однако я хотел(а) бы обсудить возможность удаленной работы (работы в офисе), возможность получить ДМС со стоматологией (перечислить условия, которые для вас идеальны). Подскажите, пожалуйста, есть ли возможность обсудить варианты обновления оффера?"', reply_markup=keyboard1)


@dp.callback_query_handler(text="next6_alt")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next5_no_again"),
        types.InlineKeyboardButton(text="Далее", callback_data="next7_alt"),
    )
    await query.message.edit_text('Не соглашайтесь, не попробовав поднять сумму, даже если отчаялись и считаете это первым и последним оффером. Самое страшное, что может произойти, если вы попробуете договориться о повышении - работодатель ответит, что это финальный оффер и дальнейшие переговоры невозможны.', reply_markup=keyboard1)

@dp.callback_query_handler(text="next7_alt")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Назад", callback_data="next6_alt"),
    )
    await query.message.edit_text('"Я внимательно ознакомился(лась) с вашим предложением. Мне нравится ваша компания/проект/команда и я заинтересован в сотрудничестве с вами, однако меня смущает уровень заработной платы. В других компаниях, с которыми я веду переговоры, предлагается более высокий уровень дохода. Давайте обсудим\предлагаю пересмотреть размер зарплаты до (сумма)."', reply_markup=keyboard1)





@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
