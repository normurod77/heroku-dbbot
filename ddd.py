from aiogram import Bot, Dispatcher, executor, types
import psycopg2

bot = Bot(token='5495640903:AAF0xm-QHCmQ-0UzSLiGY-PWRuJbZo5vqbs')
dp = Dispatcher(bot)
chat_id = -1001663008779
r = "postgres://lwbkvxcerxpduj:51206444bf4c270144e7ca2ba273cba68fc2123d0f9767af745399a8ed988300@ec2-176-34-215-248.eu-west-1.compute.amazonaws.com:5432/da6sulg3fmtql5"

db = psycopg2.connect(r, sslmode='require')
sql = db.cursor()
@dp.message_handler(commands=['reg'], commands_prefix='/')
async def rrrr(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == 1262601986  or message.reply_to_message.from_user.id == 674473647 or message.reply_to_message.from_user.id == 1232883508:
            f = message.reply_to_message.text
            sql.execute(f"SELECT id FROM users WHERE id = '{f}'")
            if not sql.fetchone():
                if any(ch.isdigit() for ch in f) is True:
                    f = message.reply_to_message.text
                    g = message.text
                    df = g[5:]
                    #sql.execute(f"INSERT INTO users(id, comp) VALUES (%s, %s)", (f, df))
                    #db.commit()
                    await bot.send_message(message.chat.id, "Клиент успешно зарегистрован")
                else:
                    await bot.send_message(message.chat.id, 'вы ввели что-то другое')
                    return
            else:
                await bot.send_message(message.chat.id, 'клиент уже есть')
                return
        else:
            return
    else:
        await bot.send_message(message.chat.id, 'Это сообщение должно быть ответом на сообщения')
        return
@dp.message_handler(commands=['del'], commands_prefix='/')
async def rrrr(message: types.Message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.id == 1262601986 or message.reply_to_message.from_user.id == 674473647 or message.reply_to_message.from_user.id == 1232883508:
            f = message.reply_to_message.text
            sql.execute(f"SELECT id FROM users WHERE id = '{f}'")
            if sql.fetchone():
                if any(ch.isdigit() for ch in f) is True:
                    sql.execute(f"DELETE FROM users WHERE id = '{f}'")
                    db.commit()
                    g = message.text
                    df = g[4:]
                    await bot.send_message(message.chat.id, "Клиент успешно удалён")
                else:
                    await bot.send_message(message.chat.id, 'вы ввели что-то другое')
                    return
            else:
                await bot.send_message(message.chat.id, 'такого клиента нет')
                return
        else:

            return
    else:
        await bot.send_message(message.chat.id, 'Это сообщение должно быть ответом на сообщения')
        return
executor.start_polling(dp, skip_updates=True)