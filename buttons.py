from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import types

kb = [
    [
        types.KeyboardButton(text="Выбрать трэк"),
        types.KeyboardButton(text="Скачать схему"),
        types.KeyboardButton(text="Получить мотивацию"),
        types.KeyboardButton(text="Написать коучу")
    ],
]
couch = [
    [
        types.KeyboardButton(text="Написать в личку"),
        types.KeyboardButton(text="Написать тут"),
    ],
]
keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )
keyboard1 = types.ReplyKeyboardMarkup(
        keyboard=couch,
        resize_keyboard=True,
        input_field_placeholder="Выберите один из вариантов:"
    )

# button1 = KeyboardButton(text="Выбрать трэк"),
# button2 = KeyboardButton(text="Скачать схему"),
# button3 = KeyboardButton(text="Получить мотивацию"),
# button4 = KeyboardButton(text="Написать коучу!")

# markup5 = ReplyKeyboardMarkup().row(
#     button1, button2)

# markup5.row(button3, button4)
# # markup5.insert(button6)
# keyboard12 = types.ReplyKeyboardMarkup(
#         keyboard=markup5,
#         resize_keyboard=False,
#         input_field_placeholder="Выберите один из вариантов:"
#     )

button1 = KeyboardButton('Выбрать трэк')
button2 = KeyboardButton('Скачать схему')
button3 = KeyboardButton('Получить мотивацию')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup4 = ReplyKeyboardMarkup().row(
    button1, button2, button3
)

markup5 = ReplyKeyboardMarkup().row(
    button1, button2
)

button4 = KeyboardButton('Написать коучу')
button5 = KeyboardButton('5️⃣')
button6 = KeyboardButton('6️⃣')
markup5.row(button3, button4)
# markup5.insert(button6)