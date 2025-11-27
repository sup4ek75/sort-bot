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

def dec(x):
    if x == "стекло":
        return "Стекло разлагается более 1000 лет, но точный срок может достигать миллиона лет. В отличие от биоразлагаемых материалов, стекло не разлагается полностью, а постепенно разрушается на всё более мелкие осколки. Поэтому лучшим способом утилизации является переработка. "
    elif x == "пластик":
        return "от нескольких десятилетий до 1000 лет. Пластиковые пакеты и стаканчики разлагаются от 20 до 400 лет, бутылки — около 450 лет, а одноразовые подгузники и другие гигиенические средства могут занимать до 500 лет, а некоторые виды пластика — до 1000 лет. "
    elif x == "бумага":
        return "газетная и тонкая бумага разлагается от 1 до 4 месяцев, а вот офисная бумага, из-за своей плотности и состава, разлагается до 2 лет"
    elif x == "картон":
        return "Картон разлагается от 2 месяцев до 1 года, в зависимости от условий. В среднем, при попадании в природу, картон можно считать быстро разлагаемым материалом, хотя точные сроки могут варьироваться."
    else:
        return "Я не знаю сколько это разлагается"

@bot.message_handler(commands=['decay'])
def decayy(message):
    a = message.text.split()[1]
    b = dec(a)
    bot.send_message(message.chat.id, b)



bot.infinity_polling()


