import telebot
from telebot.types import Message

token = '6692494644:AAG-gdl5Mt7ukwVM7vynKRD9uDHHE_03Kxs'

bot = telebot.TeleBot(token)

def if_hello(message):
    return 'привет' in message.text.lower()


@bot.message_handler(content_types=['text'], func=if_hello)
def hello(message: Message):
    bot.send_message(message.from_user.id, f'Привет. \n\nКак дела')


@bot.message_handler(content_types=['photo'])
def get_photo(message: Message):
    photo_id = message.photo[-1].file_id
    bot.send_photo(message.from_user.id, photo_id, caption='Вот она')
    bot.send_photo(message.from_user.id,
                   'AgACAgIAAxkBAAMSZXnapkW-RS21ZKpnbSWBsXKZ4IoAAk_SMRsRicBLrHZm1fYDC2ABAAMCAAN4AAMzBA',
                   caption='Такую фоточку я получил')


@bot.message_handler(commands=['get_photo3'])
def hello_start(message: Message):
    bot.send_message(message.from_user.id, 'Привет в нашем боте!')
    bot.send_photo(message.from_user.id,
                   'AgACAgIAAxkBAAMtZXni4b4MsfAkOlahtrDQsvpK7PsAAlHSMRsRicBLE86XdTlSxSYBAAMCAAN4AAMzBA',
                   caption='Такую фоточку я получил')


@bot.message_handler(commands=['get_photo2'])
def get_photo2(message: Message):
    img_foto = open(r'media/img.png', 'rb')
    bot.send_document(message.from_user.id, img_foto)
    img_foto.close()


@bot.message_handler(content_types=['text'])
def i_dont_khow(message: Message):
    print(message.from_user.id)
    bot.send_message(message.from_user.id, 'Не знаю что ты написал')


@bot.message_handler(content_types=['voice'])
def get_voice(message: Message):
    print(message)

bot.polling()

