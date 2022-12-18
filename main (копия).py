import os
import datetime
import logging
from aiogram import Dispatcher, Bot, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO,
                    filename='logfile.log',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S')

# TOKEN = os.getenv('TOKEN')
TOKEN = '5522470947:AAH8E3dr59tGtaxt1iw5nH0Rvyg5z0BM8gY'
ADMIN='1081686891'
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


async def on_startup(_):
    print('Бот запущен!')
couch = [
    [
        types.KeyboardButton(text="Написать в личку"),
        types.KeyboardButton(text="Написать тут"),
    ],
]
keyboard1 = types.ReplyKeyboardMarkup(
        keyboard=couch,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )
# kb = [
#     [
#         types.KeyboardButton(text="Выбрать трэк"),
#         types.KeyboardButton(text="Скачать схему"),
#         types.KeyboardButton(text="Получить мотивацию"),
#         types.KeyboardButton(text="Написать коучу")
#     ],
# ]
# keyboard = types.ReplyKeyboardMarkup(
#     keyboard=kb,
#     resize_keyboard=True,
#     # input_field_placeholder="Выберите один из вариантов:"
# )
button1 = KeyboardButton('Выбрать трэк')
button2 = KeyboardButton('Скачать схему')
button3 = KeyboardButton('Получить мотивацию')
button4 = KeyboardButton('Написать коучу')

keyboard = ReplyKeyboardMarkup().row(
    button1, button2
)
keyboard.row(button3, button4)

@dp.message_handler(commands=['start'])
@dp.message_handler(lambda message: message.text == "В начало")
async def starter(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_photo(message.from_id, photo=open('static/media_files/start.png', 'rb'))
    await bot.send_message(message.from_id, text="Чтобы со мной общаться, в помощь кнопки 😉")
    await message.answer("Чем я могу помочь?", reply_markup=keyboard)


######################################## Main Menu ########################################

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



import random
@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться!")
    dir = 'static/motiv'
    path = random.choice(os.listdir(dir))
    path=dir+'/'+path
    if path[-3:]=='gif':
        photo = open(path, 'rb')
        await bot.send_animation(message.from_id, photo)
    else:
        await bot.send_photo(message.from_id, photo=open(path, 'rb'))
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Написать коучу")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_photo(message.from_id, photo=open('static/media_files/hr.jpg', 'rb'),
    caption='Надя Крутикова отличный специалист, она тебе точно поможет!')
    await message.answer("Что делаем?", reply_markup=keyboard1)

@dp.message_handler(lambda message: message.text == "Написать в личку")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "Надя Крутикова отличный специалист, она тебе точно поможет!")
    await bot.send_message(message.from_id, text="❤️ *[Вот ссылка на аккаунт Нади](https://t.me/krutikovanad)* ❤️", parse_mode='MarkdownV2')
    await message.answer("Что-то ещё?", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "Написать тут")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.username} {message.from_user.full_name}: {message.text[-1]}')
    await bot.send_message(message.from_id, "Чтобы написать Наде напиши /to_coach и далее свое сообщение")
    # await message.answer("Чтобы написать Наде напиши /to_coach и далее свое сообщение", reply_markup=keyboard1)
    # f = open('logfile.log')

@dp.message_handler(commands=['to_coach'])
async def any_message(message: types.Message):
    if len(message.text)>10:
        logging.info(f'{message.from_user.full_name}: {message.text}')
        now = datetime.datetime.now()
        time = now.strftime("%d-%m-%Y %H:%M")
        text=f'@{message.from_user.username} в {time} написал вам: {message.text[10:]} '
        await bot.send_message(chat_id = '-1001636312840', text=text)
        await message.answer("Отправил", reply_markup=keyboard)

    else:
        await message.answer("Попробуй снова :( Ты забыл написать текст", reply_markup=keyboard)
        await bot.send_message(message.from_id, 'Должно выглядить так: "/to_coach Привет!"')
    

start_text = "Тест"
@dp.message_handler(lambda message: message.text == "Выбрать трэк")
async def track(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    start_keyboard = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="Переговоры с работодателем", callback_data="negotiation"),
        types.InlineKeyboardButton(text="Поиск работы", callback_data="job")
    )
    await message.answer(f"Какой трэк вы выбираете?\n\n", parse_mode="HTML", reply_markup=start_keyboard)





######################################## Track 1 ########################################

@dp.callback_query_handler(text="negotiation")
async def negotiations(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next1")
    )
    await query.message.edit_text(f'🏁 Вам звонит/пишет HR  и сообщает, что работодатель готов сделать оффер! ☎️\n\n', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="next1")
async def negotiations1(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="negotiation"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next2"),
    )
    await query.message.edit_text(f'📝 Запишите все, что HR рассказал по телефону/сравните '
                                  'текст сообщения с текстом вакансии - информация может '
                                  'немного отличаться от опубликованной в вакансии, то, что '
                                  'озвучил/написал  HR  имеет большую силу.\n\n', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="next2")
async def negotiations2(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next1"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next3"),
    )
    await query.message.edit_text(f'⛔️ Не говорите сразу же <i>"да, я согласен"</i>, '
                                  'попросите выслать оффер в письменном виде, '
                                  'чтобы вы могли подробно в спокойной обстановке '
                                  'ознакомиться с информацией\n\n', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="next3")
async def negotiations3(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next2"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next4"),
        types.InlineKeyboardButton(text="Важно ❗️", callback_data="next4_alt"),
    )
    await query.message.edit_text(f'💌 Вы получили письменный оффер (обычно по имейлу в приложении отдельным файлом)\n\n', parse_mode="HTML", reply_markup=keyboard1)

import html
@dp.callback_query_handler(text="next4_alt")
async def negotiations4(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next3"),
    )
    text1 = f'🌟 Если вы получили оффер - для "поднятия" своего рейтинга у других работодателей, не забудьте сообщить всем компаниям, от которых ждете ответ по собеседованиям (особенно тем, в которые очень хотите), что вы получили оффер:'
    text2 = f'Добрый день, <u>имя рекрутера</u>, \n\nХотел(а) бы сделать апдейт по процессу рекрутинга - я на днях  получил(а) оффер, однако ваша компания для меня приоритетна и я бы хотел(а) пройти дальнейшие этапы/получить обратную связь по собеседованию как можно скорее. Подскажите, пожалуйста, сможете ли вы до <u>(свой день недели)</u> вернуться с ответом по моей кандидатуре?'
    text3 = f'Сообщать от какой компании оффер и на какую сумму не нужно.'
    await query.message.edit_text(f'{text1}\n\n<i>{text2}</i>\n\n{text3}\n\n', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="next4")
async def negotiations5(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next3"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next5"),
        types.InlineKeyboardButton(text="Важно ❗️", callback_data="next5_alt"),
    )
    text1 = f'⏱ Скажите, что вам нужно время обдумать их предложение и назовите срок, когда вы вернетесь с ответом (в идеале не больше 3-4 рабочих дней). Не принимайте оффер сразу же так как первый оффер от любой компании ВСЕГДА минимален по сумме, он только открывает пространство переговоров по зарплате. помните, что  зарплата разработчика прежде всего зависит от суммы, в которую он сам себя оценивает.'
    text2 = f'Добрый день, <u>имя рекрутера</u>,'
    text3 = f'Благодарю, документ получил(а). Я внимательно ознакомлюсь с оффером и вернусь к вам <u>до день недели/дата</u>. Большое спасибо, что поделились со мной хорошими новостями, будем на связи!'
    await query.message.edit_text(f'{text1}\n\n<i>{text2}\n\n{text3}</i>\n\n', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_alt")
async def negotiations6(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next4"),
    )
    text1 = f'⚠️ Если вы получили оффер, на который просят ответить за короткое время (24/48/72 часа), а вы не готовы так быстро принять решение/ждете информации от других работодателей. Не ведитесь на срочность и не переживайте - это просто способ работодателя надавить и поскорее закрыть вакансию. Напишите ответ HR в таком ключе:'
    text2 = f'"Добрый день, <u>имя рекрутера</u>,\n\nБлагодарю, документ получил(а). К сожалению, принять решение по данному предложению в такой короткий срок/за 24-48-72 часа/1 день/2 дня я не имею возможности, так как нахожусь на финальной стадии переговоров с другими компаниями и этот процесс займет еще примерно неделю. Мне понадобится больше времени, чтобы принять взвешенное решение.'
    text3 = f'Если компания возвращается с ответом, что это единственный вариант и они не могут предложить других опций по времени, напишите им:'
    text4 = f'Очень жаль, мне нравится ваша компания, проект и команда. Решение о выборе работодателя для меня очень важное и ответственное и я никак не могу его принять за такой короткий срок'
    text5 = f'Большинство компаний на этом этапе продлят срок или начнут торговаться по сроку. Если этого не происходит - возможно, это не твоя компания.'
    await query.message.edit_text(f'{text1}\n\n<i>{text2}</i>\n\n{text3}\n\n<i>{text4}</i>\n\n{text5}\n\n', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="next5")
async def negotiations7(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next4"),
        types.InlineKeyboardButton(text="Да 💪", callback_data="next6"),
        types.InlineKeyboardButton(text="Нет 👎", callback_data="next5_no"),
    )
    await query.message.edit_text('💰 Вам сделали отличное предложение, оффер на большую зарплату, '
                                  'чем вы рассчитывали?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_no")
async def negotiations8(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next5"),
        types.InlineKeyboardButton(text="Так и есть 👍", callback_data="next6"),
        types.InlineKeyboardButton(text="Не совсем так 👎", callback_data="next5_no_again"),
    )
    await query.message.edit_text('💵 Вам сделали хорошее предложение, оффер на среднюю зарплату?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next5_no_again")
async def negotiations9(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next5_no"),
        types.InlineKeyboardButton(text="Да 🗿", callback_data="next6_alt"),
    )
    await query.message.edit_text('💸 Вам сделали предложение с низкой зарплатой?', reply_markup=keyboard1)

@dp.callback_query_handler(text="next6")
async def negotiations10(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next5"),
        types.InlineKeyboardButton(text="Соглашусь на оффер 🤝", callback_data="next7"),
        types.InlineKeyboardButton(text="Попытаю еще удачу 🍀", callback_data="next7_alt1"),
    )
    await query.message.edit_text('🤔 Прежде чем согласиться, вспомните про то, что первый оффер всегда '
                                  'минимальный - обдумайте и  решите, хотите ли попробовать поднять '
                                  'сумму - это возможно!', reply_markup=keyboard1)


@dp.callback_query_handler(text="next7")
async def negotiations11(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next6"),
    )
    await query.message.edit_text('👩‍💻 Ок, не забудьте про юридическое оформлени! 👨‍💻', reply_markup=keyboard1)

@dp.callback_query_handler(text="next7_alt1")
async def negotiations12(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next6"),
    )
    text1 = f'🚀 Я внимательно ознакомился(лась) с вашим предложением. Должен(а) признать, что оно привлекательно и конкурентоспособно. Мне нравится ваша компания/проект/команда и я заинтересован в сотрудничестве с вами.'
    text2 = f'1. Поднимаем сумму'
    text3 = f'Однако на днях у меня завершились переговоры с другой компанией и я получил(а) оффер привлекательнее по размеру заработной платы. Предлагаю пересмотреть размер зарплаты до (сумма).'
    text4 = f'2. Улучшаем условия, которые не устраивают'
    text5 = f'Однако я хотел(а) бы обсудить возможность удаленной работы (работы в офисе), возможность получить ДМС со стоматологией <u>(перечислить условия, которые для вас идеальны)</u>. Подскажите, пожалуйста, есть ли возможность обсудить варианты обновления оффера?"'
    await query.message.edit_text(f'<i>{text1}</i>\n\n<b>{text2}</b>\n<i>{text3}</i>\n\n<b>{text4}</b>\n<i>{text5}</i>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="next6_alt")
async def negotiations13(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next5_no_again"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="next7_alt"),
    )
    await query.message.edit_text('⛔️ Не соглашайтесь, не попробовав поднять сумму, даже если отчаялись и считаете это первым и последним оффером. Самое страшное, что может произойти, если вы попробуете договориться о повышении - работодатель ответит, что это финальный оффер и дальнейшие переговоры невозможны.', reply_markup=keyboard1)

@dp.callback_query_handler(text="next7_alt")
async def negotiations14(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="next6_alt"),
    )
    text1 = '🚀 Я внимательно ознакомился(лась) с вашим предложением. Мне нравится ваша компания/проект/команда и я заинтересован в сотрудничестве с вами, однако меня смущает уровень заработной платы. В других компаниях, с которыми я веду переговоры, предлагается более высокий уровень дохода. Давайте обсудим\предлагаю пересмотреть размер зарплаты до (сумма).'
    await query.message.edit_text(f'<i>{text1}</i>', parse_mode="HTML", reply_markup=keyboard1)


######################################## Track 2 ########################################

@dp.callback_query_handler(text="job")
async def jobs(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text='HR сама написала с предложением созвониться', callback_data='then1'),
        types.InlineKeyboardButton(text='Вы сами откликнулись и получили отказ', callback_data="then1_alt"),
        types.InlineKeyboardButton(text='Вы сами откликнулись и получили приглашение', callback_data="then2")
    )
    text1 = f'🏁 Вы выложили резюме в открытом доступе на HH\Habr Career и пр.'
    text2 = f'‼️ Присоединяем сопроводительное письмо + одностраничное резюме отдельным файлом!'
    await query.message.edit_text(f'{text1}\n\n<b>{text2}</b>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then1")
async def jobs1(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="job"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="then2"),
    )
    await query.message.edit_text(f'🥳 Поздравляю! Резюме работает! ', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then1_alt")
async def jobs2(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="job"),
    )
    text1 = f'Поблагодарите HR и напишите емкое сообщение, налаживая коммуникацию с первого касания. Например:'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n\nБлагодарю Вас за внимание, проявленное к моей кандидатуре. Буду рад(а) оставаться с вами на связи и получить приглашение на собеседование.\n\nС уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'{text1}\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then2")
async def jobs3(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="job"),
        types.InlineKeyboardButton(text="Нет 👎", callback_data="then3_no"),
        types.InlineKeyboardButton(text="Да 👍", callback_data="then3_yes"),
        types.InlineKeyboardButton(text="В вакансии не указана ЗП ", callback_data="salary"),
    )
    await query.message.edit_text(f'🎉 Ура! Вас заметили!\n\nВы хотите продолжить общение по вакансии?', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="salary")
async def jobs4(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then2"),
        types.InlineKeyboardButton(text="Нет 👎", callback_data="salary_no"),
        types.InlineKeyboardButton(text="Да 👍", callback_data="salary_yes"),
    )
    await query.message.edit_text(f'У вас есть оффер?', reply_markup=keyboard1)

@dp.callback_query_handler(text="salary_yes")
async def jobs5(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="salary"),
        types.InlineKeyboardButton(text="Не хочу продолжать общение", callback_data="then3_no"),
        types.InlineKeyboardButton(text="Хочу продолжить общение", callback_data="then3_yes"),
    )
    text1 = f'Как спросить про заработную плату, если она не указана в вакансии?'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n' \
            f'Спасибо за интересное предложение. Я ознакомился\(лась) с условиями, готов(а) начать общение и рассказать о своем опыте работы.\n\n' \
            f'Пожалуйста уточните размер оклада (на руки) на данной позиции?\n' \
            f'Дело в том, что я сейчас в процессе оформления документов в другой компании и хочу понимать есть ли смысл менять ситуацию или нет.\n\n' \
            f'Спасибо за понимание.\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<b>{text1}</b>\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="salary_no")
async def jobs6(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="salary"),
        types.InlineKeyboardButton(text="Не хочу продолжать общение", callback_data="then3_no"),
        types.InlineKeyboardButton(text="Хочу продолжить общение", callback_data="then3_yes"),
    )
    text1 = f'Как спросить про заработную плату, если она не указана в вакансии?'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n' \
            f'Спасибо за интересное предложение. Я ознакомился\(лась) с условиями, готов(а) начать общение и рассказать о своем опыте работы.\n\n' \
            f'Пожалуйста уточните размер оклада (на руки) на данной позиции?\n' \
            f'Спасибо за понимание.\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<b>{text1}</b>\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then3_no")
async def jobs7(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then2"),
    )
    text1 = f'Как отказаться от вакансии.'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n' \
            f'Благодарю Вас за внимание, проявленное к моей кандидатуре и предложение о сотрудничестве. К сожалению, в настоящее время я вынужден(а)  отказаться от вашего предложения, так как:\n\n' \
            f'• не рассматриваю позицию Front\Back\Fullstack или стэк....' \
            f'• рассматриваю только удаленный формат работы\n' \
            f'• завершил(а) поиски работы\n'\
            f'• Ваш вариант _______\n\n' \
            f'Буду рад(а) оставаться с вами на связи и сообщу вам, если возобновлю поиск работы.\n\n' \
            f'Желаю вам успехов в поиске подходящего кандидата на эту должность. Всего наилучшего вам и <u>(название компании)</u>!\n\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<b>{text1}</b>\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then3_yes")
async def jobs8(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then2"),
        types.InlineKeyboardButton(text="Вопросы для подготовки к собесу", callback_data="then4"),
    )
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n' \
            f'Спасибо за интересное предложение. Я ознакомился\(лась) с условиями, готов(а) начать общение и рассказать о своем опыте работы.\n\n' \
            f'Когда вам будет удобно созвониться?\n\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then4")
async def jobs9(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then3_yes"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="then5"),
    )
    await query.message.edit_text(f'👉 *[Ссылка на вопросы](https://docs.google.com/document/d/1fRN77t5175Df4fTns0qULSKE4eK5Ecy4AS6qeSY_o1U/edit)*', parse_mode='MarkdownV2', reply_markup=keyboard1)


@dp.callback_query_handler(text="then5")
async def jobs10(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then4"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data="then6"),
    )
    text1 = f'Вы договорились о звонке и в концы Звонка вы задаете рекрутеру\HR вопросы:'
    text2 = f'• Какой следующий этап общения с компанией?\n' \
            f'• Когда рекрутер\HR даст об этом знать?\n' \
            f'• Не возражает ли рекрутер\HR, если вы напомните о себе?\n' \
            f'• Какие этапы собеседований (сколько всего этапов)?\n\n'
    await query.message.edit_text(f'{text1}\n\n{text2}', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then6")
async def jobs11(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then5"),
        types.InlineKeyboardButton(text="Да, и это отказ 💔", callback_data="then7_alt1"),
        types.InlineKeyboardButton(text="Да, и это оффер 🥳", callback_data="then7_alt2"),
        types.InlineKeyboardButton(text="Нет, она пропала 😰", callback_data="then7_alt3"),
    )
    await query.message.edit_text(f'Рекрутер вышла к вам с фидбэком?', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then7_alt1")
async def jobs12(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then6"),
    )
    text1 = f'Не расстраивайтесь!  Поблагодарите рекрутера за уделенное время и внимание к вам. Например:'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n\n' \
            f'Спасибо за обратную связь, уделенное моей кандидатуре время и приятный опыт собеседования!\n\n' \
            f'Жаль, что не получится посотрудничать по данной вакансии. Но я продолжаю искать работу в этой сфере. И мне был бы очень полезен ваш взгляд как профессионала, почему я получил(а) отказ. Хочу разобраться, над чем стоит поработать, какие навыки подтянуть.\n\n' \
            f'Я сейчас активно ищу работу и буду благодарен\(на), если вы порекомендуете мою кандидатуру коллегам.\n\n' \
            f'Буду признателен(льна), если сможете ответить.\n' \
            f'<u>(Ваше имя)</u>.'
    text3 = f'В случае если с hr случилась "взаимная любовь" написать:'
    text4 = f'Хочу поделиться с вами положительным впечатлением. После собеседования я понял(а), что ваша компания - это та самая компания мечты. Если у вас что-то изменится или откроется еще одна вакансия, то я буду очень счастлив(а) принять участие в отборе на вакансию и пройти собеседование.\n\n' \
            f'<u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<b>{text1}</b>\n\n<i>{text2}</i>\n\n<b>{text3}</b>\n\n<i>{text4}</i>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then7_alt3")
async def jobs13(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then6"),
        types.InlineKeyboardButton(text="Если вы очень хотите в эту компанию ❤️", callback_data="then8_alt1"),
        types.InlineKeyboardButton(text="Если вы очень торопитесь 🏃‍", callback_data="then8_alt2"),
    )
    text1 = f'Здравствуйте _____.\n' \
            f'Уточните пожалуйста есть ли уже решение по моей кандидатуре?'
    text2 = f'Если решения нет, то уточните когда вам можно будет вернуться за обратной связью.\nНапример:'
    text3 = f'Благодарю за ответ. Сообщите пожалуйста когда мне ожидать обратной связи по моей кандидатуре?'
    text4 = f'NOTE: если рекрутер обещал вам дать ответ в четверг, не надо писать в середине рабочего дня четверга что-то вроде: «Неужели даже отрицательного фидбэка не заслуживаю?”'
    await query.message.edit_text(f'<i>{text1}</i>\n\n<b>{text2}</b>\n\n<i>{text3}</i>\n\n<b>{text4}</b>', parse_mode="HTML", reply_markup=keyboard1)



@dp.callback_query_handler(text="then8_alt1")
async def jobs14(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then7_alt3"),
    )
    text1 = f'Здравствуйте _____.\n' \
            f'Дело в том, что до <u>(день недели или число)</u> я должен дать ответ по офферу, который получил на днях, однако ваша компания для меня приоритетна и я бы хотел пройти дальнейшие этапы как можно скорее.'
    text2 = f'А дальше:'
    text3 = f'Подскажите получится с ближайшее время провести со мной (техническое) собеседование?'
    text4 = f'или'
    text5 = f'Подскажите сможете ли вы до пятницы  вернуться с ответом по моей кандидатуре?'
    await query.message.edit_text(f'<i>{text1}</i>\n\n<b>{text2}</b>\n\n<i>{text3}</i>\n\n<b>{text4}</b>\n\n<i>{text5}', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then8_alt2")
async def jobs15(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then7_alt3"),
    )
    text1 = f'Здравствуйте _____.\n'
    text2 = f'Пожалуйста уточните какие дальнейшие этапы собеседования? Мне сегодня сделали оффер, нужно дать ответ до  <u>(день недели или число)</u>, хотел бы успеть сравнить вакансии.'
    await query.message.edit_text(f'<i>{text1}</i>\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then7_alt2")
async def jobs16(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then6"),
        types.InlineKeyboardButton(text="Далее ▶️", callback_data='then8'),
    )
    text1 = f'<b>NOTE</b>: коуч поможет вам понять, <b>что ОК или НЕ ОК в оффере</b>, подскажет, как поторговаться по условиям и, конечно, <b>разделит с вами вашу победу</b>.'
    await query.message.edit_text(f'Cрочно писать вашему карьерному коучу‼️\n\n{text1}', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then8")
async def jobs17(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then7_alt2"),
        types.InlineKeyboardButton(text="Да 🎉", callback_data='then9_yes'),
        types.InlineKeyboardButton(text="Да, но не устраивают условия 🤷‍", callback_data='then9_yes_alt'),
        types.InlineKeyboardButton(text="Нет 👎", callback_data='then9_no'),
    )
    await query.message.edit_text(f'Вы  решили принять оффер?', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then9_yes")
async def jobs18(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then8"),
    )
    text1 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n\n' \
            f'Спасибо за предложение присоединиться к команде (название компании). Ознакомившись с условиями найма, я с радостью принимаю ваше предложение.\n' \
            f'Размер оплаты труда и прочие условия, указанные в оффере, полностью меня устраивают.\n' \
            f'Готов(а) приступить к работе с (число\месяц) и с нетерпением жду своего первого дня в вашей компании.\n' \
            f'Если у вас есть ко мне дополнительные вопросы готов(а) ответить в удобное вам время.\n\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<i>{text1}</i>', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then9_yes_alt")
async def jobs19(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then8"),
        types.InlineKeyboardButton(text="Перейти к переговорам", callback_data="negotiation"),
    )
    await query.message.edit_text(f'СМОТРИ БЛОК-СХЕМУ ПО ПЕРЕГОВОРАМ', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then9_no")
async def jobs20(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then8"),
        types.InlineKeyboardButton(text="Отказать (с объяснением причины)", callback_data="then10_alt1"),
        types.InlineKeyboardButton(text="Отказать (без объяснения причин)", callback_data="then10_alt2"),
    )
    text1 = f'<b>NOTE</b>: чем дольше вы общаетесь с компанией, тем более обоснованным должен быть ваш отказ. Главное ― избегать исчезновения из коммуникации с компанией без объяснения причин. Это может сыграть во вред вашей репутации на рынке труда.'
    await query.message.edit_text(f'{text1}', parse_mode="HTML", reply_markup=keyboard1)


@dp.callback_query_handler(text="then10_alt1")
async def jobs21(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then9_no"),
    )
    text1 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n\n' \
            f'Спасибо за предложение стать частью <u>(название компании)</u> в роли <u>(название позиции)</u>. Я ценю предоставленную возможность и ваш интерес к моей кандидатуре.\n\n' \
            f'К сожалению, я выбрал(а) позицию в другой компании. На данном этапе она лучше всего соответствует моим карьерным ожиданиям и целям.\n\n' \
            f'Еще раз спасибо за ваше время и приятный опыт собеседования!\n\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<i>{text1}</i>', parse_mode="HTML", reply_markup=keyboard1)

@dp.callback_query_handler(text="then10_alt2")
async def jobs22(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup(row_width=1).add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="then9_no"),
    )
    text1 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n\n' \
            f'Спасибо за предложение присоединиться к команде <u>(название компании)</u>. Я ценю время, которое вы потратили на то, чтобы провести собеседование и ответить на все мои вопросы.\n\n' \
            f'Мне нелегко далось это решение, но я вынужден(а) отказаться от вашего предложения.\n\n' \
            f'Желаю вам успехов в поиске подходящего кандидата на эту должность. Всего наилучшего вам и <u>(название компании)</u>!\n\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<i>{text1}</i>', parse_mode="HTML", reply_markup=keyboard1)




@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.id} {message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст 🥸, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
