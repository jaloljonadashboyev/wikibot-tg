from aiogram import Bot, Dispatcher, executor, types
import wikipedia

# wikipedia.set_lang("eng")

api_token = "5683790171:AAH6HuLcQ8iYeHED7T1KMFicXkniNNvf5bU"
bot = Bot(token=api_token)
dp = Dispatcher(bot)


@dp.message_handler(commands='start')
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    # ID = message.from_user.id
    await message.answer(f"Welcome <b>{user_name}</b>. You can use this bot as an alternative to en.wikipedia.org.", parse_mode="HTML")

# Temporary
@dp.message_handler()
async def send_wikipedie(message: types.Message):
    search = message.text
    try:
        await message.answer(f"<i>{wikipedia.summary(search)}</i>", parse_mode="HTML")
    except Exception as excp:
        await message.answer(f"Information about \"{search}\" is not found in en.wikipedia.org site")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
