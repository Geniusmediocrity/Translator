import asyncio

from translate import Translator

from aiogram.methods import DeleteWebhook
from aiogram import types
from aiogram.filters import Command

from configs import dp, bot
from utils.messages import Messages
from logs.events_logging import setup_logger


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.reply(Messages.START_MESSAGE)

@dp.message()
async def echo(message: types.Message):
    ru_letters = "\"'[]{},.<\\/>%^:;&?()-_=+!@#№$`~абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    en_letters = "\"'[]{},.<\\/>%^:;&?()-_=+!@#№$`~abcdefghijklmnopqrstuvwxyz"
    
    process_mes = await message.reply(text=Messages.ANSWER_PROCESSING.format(message.from_user.username, "5"), parse_mode="HTML")
    text = message.text
    if text[0].lower() in ru_letters:
        translator = Translator(from_lang="ru", to_lang="en")
    elif text[0].lower() in en_letters:
        translator = Translator(from_lang="en", to_lang="ru")
    
    result = translator.translate(text=text)
    
    await process_mes.delete()
    await message.answer(result)
    
    

async def main():
    setup_logger()
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())