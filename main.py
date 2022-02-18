from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from api import api_req

TOKEN = "Qovuncha"
bot = Bot(token=TOKEN)
dp  = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def get_image(message:types.Message):
    chat_id = message.from_user.id
    first_name = message.from_user.first_name
    text = f"Assalomu alaykum {first_name}!"
    await bot.send_message(chat_id=chat_id, text=text)

@dp.message_handler(content_types=types.ContentTypes.PHOTO)
async def sand_message(message:types.Message):
    message_id = (await message.answer("Yuklanmoqda...🚀")).message_id
    photo_id = message.photo[-1].file_id
    photo_info = await bot.get_file(photo_id)
    file_path = photo_info["file_path"]
    photo_url = f"https://api.telegram.org/file/bot{TOKEN}/{file_path}"
    
    data = await api_req(photo_url)

    if data is not None:
        await bot.delete_message(chat_id=message.from_user.id, message_id=message_id)
        await message.answer_photo(photo=data)
    else:
        await message.answer("Iltimos yuz qiyofasini aniq ko'ringan rasm yuboring!")

    print(data) 

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)