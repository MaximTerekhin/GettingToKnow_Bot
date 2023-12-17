import telebot
from info import dict_project

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
     bot.send_message(message.chat.id,".....Привет!\n"
                                     f"Моё имя - Стрибот!\n"
                                     f"Приятен в общении,\n"
                                     f"Могу рассказать какие проекты ты писал.")


# def bird(message):
#     return "стань попугаем".lower() in message.text
# @bot_2modul_1project.message_handler(content_types=['text'],func=bird)
# def pirett(message):
#     bot_2modul_1project.send_message(message.chat.id,'Приделываю клюв....разноцветный окрас...крылья....Готово!Я попугай')
#     @bot_2modul_1project.message_handler(content_types=['text'])
#     def pirr(message):
#         bot_2modul_1project.send_message(message.chat.id, message.text)
#
# def not_bird(message):
#     return "попугай стоп" in message.text
# @bot_2modul_1project.message_handler(content_types=['text'],func=not_bird)
# def notbird(message):
#     bot_2modul_1project.send_message(message.chat.id,'Попугай приостанолен')
#     #@bot_2modul_1project.message_handler(content_types=['text'])
#     bot_2modul_1project.send_message(message.chat.id,"я готов работать дальше")

@bot.message_handler(commands=['my_projects'])
def prjcts(message):
      bot.send_message(message.chat.id,f"Пока ты написал 3 работы\n :"
                                    f"1) Игра - лабиринт\n"
                                     f"2) Обработка текста\n"
                                     f"3) Обработка изображений")
def filter1(message):
    return "1 проект первого модуля".lower() in message.text
@bot.message_handler(content_types=['text'],func=filter1)
def fltr1 (message):
    bot.send_message(message.chat.id,dict_project['project1'])

def filter2(message):
    return "2 проект первого модуля".lower() in message.text
@bot.message_handler(content_types=['text'],func=filter2)
def fltr2 (message):
    bot.send_message(message.chat.id,dict_project['project2'])

def filter3(message):
    return "3 проект первого модуля".lower() in message.text
@bot.message_handler(content_types=['text'],func=filter3)
def fltr3 (message):
    bot.send_message(message.chat.id,dict_project['project3'])

@bot.message_handler(content_types=['photo'])
def pht(message):
    bot.send_photo(message.chat.id,'AgACAgIAAxkBAAICsmV7UKqOJtxydufg4-pniW86peGQAALm1zEb8'
                                   'RLZS0yaGQ6KBtTtAQADAgADcwADMwQ')
    bot.send_message(message.chat.id,"Прям как у тебя. Совпадение? Не думаю)✌")

@bot.message_handler(content_types=['video'])
def vd(message):
     bot.send_message(message.chat.id,"Что-то слишком тяжело(😒")

@bot.message_handler(content_types=['audio'])
def aud(message):
    bot.send_message(message.chat.id,"Потанцуем!😎")
def bye(message):
    return "пока".lower() in message.text
@bot.message_handler(content_types=["text"],func=bye)
def say_bye(message):
    bot.send_message(message.chat.id,"....пока!")
    bot.stop_bot()

bot.polling()



