
import random
@dp.message_handler(lambda message: message.text == "Получить мотивацию")
async def motivation(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, "У тебя все получится, главное не сдаваться!")
    dir = 'static/motiv'
    path = random.choice(os.listdir(dir))
    path=dir+'/'+path
    try:
        photo = open(path, 'rb')
        await bot.send_animation(message.from_id, photo)
    except:
        await bot.send_photo(message.from_id, photo=open(path, 'rb'))
    await message.answer("Могу я помочь чем-то еще?", reply_markup=keyboard)
