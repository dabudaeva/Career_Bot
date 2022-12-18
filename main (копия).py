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
    await bot.send_photo(message.from_id, photo=open('static/start.png', 'rb'))
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



@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться! Вот тебе мотивационный пингвин 🐧")
    await bot.send_animation(message.from_id, animation='https://media2.giphy.com/media/OZbGrdp7FiDiE/giphy.gif')
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)



@dp.message_handler(lambda message: message.text == "Написать коучу")
async def pdf(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_photo(message.from_id, photo=open('static/hr.jpg', 'rb'), 
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
        types.InlineKeyboardButton(text="В вакансии не указана ЗП", callback_data="salary"),
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
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="salary"),
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
async def jobs5(query: types.CallbackQuery):
    logging.info(f'{query.message.from_user.full_name}: {query.message.text}')
    keyboard1 = types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(text="◀️ Назад", callback_data="salary"),
    )
    text1 = f'Как спросить про заработную плату, если она не указана в вакансии?'
    text2 = f'Здравствуйте <u>(Имя HR-менеджера)</u>.\n' \
            f'Спасибо за интересное предложение. Я ознакомился\(лась) с условиями, готов(а) начать общение и рассказать о своем опыте работы.\n\n' \
            f'Пожалуйста уточните размер оклада (на руки) на данной позиции?\n' \
            f'Спасибо за понимание.\n' \
            f'С уважением, <u>(Ваше имя)</u>.'
    await query.message.edit_text(f'<b>{text1}</b>\n\n<i>{text2}</i>', parse_mode="HTML", reply_markup=keyboard1)










@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.id} {message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, 'К сожалению, я пока не понимаю текст 🥸, попробуй кнопкой')


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
