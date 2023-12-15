import telebot

token = "6812828339:AAFzRcCi8vMseLsWRvK6TRMLv-4dXLlEipE"

bot = telebot.TeleBot(token=token)

chat_id = 5255568104



@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id,f"1: Для запуска нажми /start\n"
                                     f"2: Моё имя - Стрибот!\n"
                                     f"3: Приятен в общении, могу стать попугаем,для этого напиши стань попугаем, а чтобы выключить его - попугай стоп")
bot.polling(none_stop=True)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.send_message(message.chat.id,".....Привет! Это тестовый бот, надеюсь у тебя останется хорошее впечатление.\n"
                                     f"Моё имя - Стрибот!\n"
                                     f"Приятен в общении, "
                                     f"могу стать попугаем,для этого напиши стань попугаем,"
                                     f" а чтобы выключить его - попугай стоп\n"
                                     f"Теперь могу немного работать с изображениями"
                                     f" и другими видами информации")

def bird(message):
    return "стань попугаем".lower() in message.text
@bot.message_handler(content_types=['text'],func=bird)
def pirett(message):
    bot.send_message(message.chat.id,'Приделываю клюв....разноцветный окрас...крылья....Готово!Я попугай')
    @bot.message_handler(content_types=['text'])
    def pirr(message):
        bot.send_message(message.chat.id, message.text)

def not_bird(message):
    return "попугай стоп" in message.text
@bot.message_handler(content_types=['text'],func=not_bird)
def notbird(message):
    bot.send_message(message.chat.id,'Попугай приостанолен')
    #@bot.message_handler(content_types=['text'])
    bot.send_message(message.chat.id,"я готов работать дальше")


@bot.message_handler(content_types=['photo'])
def pht(message):
    bot.send_photo(message.chat.id,'AgACAgIAAxkBAAICsmV7UKqOJtxydufg4-pniW86peGQAALm1zEb8'
                                   'RLZS0yaGQ6KBtTtAQADAgADcwADMwQ')
    bot.send_message(message.chat.id,"Прям как у тебя. Совпадение? Не думаю)✌")

# @bot.message_handler(content_types=['video'])
# def vd(messdge):
#     bot.send_audio()
def bye(message):
    return "пока".lower() in message.text
@bot.message_handler(content_types=["text"],func=bye)
def say_bye(message):
    bot.send_message(message.chat.id,"....пока!")
    bot.stop_bot()

bot.polling()



