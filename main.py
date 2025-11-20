import telebot
from settings import TG_API_TOKEN

bot = telebot.TeleBot(TG_API_TOKEN)
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nЯ бот, который помогает людям сортировать отходы. Подсказывает, какие предметы можно выбрасывать в обычную урну, а какие стоит отдавать на переработку.')

def sort(x):
    rec = ["пластик", "стекло", "бумага", "картон", "металл"]
    if x in rec:
        return "На переработку"
    else:
        return "В мусорку"

@bot.message_handler(commands=['sort'])
def sortt(message):
    musor = message.text.split()[1]
    b = sort(musor)
    bot.send_message(message.chat.id, b)





bot.infinity_polling()


